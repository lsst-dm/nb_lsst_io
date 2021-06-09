#!/usr/bin/env python3
"""Linting script for rsp-environments.yaml."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Sequence

import requests
import yaml


def main() -> None:
    args = parse_args()

    found_issues = False

    for p in args.file_paths:
        path = Path(p)
        if not path.is_file():
            sys.exit(f"Could not find a file at {path}.")

        issues = lint_file(path=path)
        report_issues(path=path, issues=issues)
        if len(issues) > 0:
            found_issues = True

    if found_issues:
        sys.exit(1)
    else:
        sys.exit(0)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Lint data in the rsp-environments.yaml file"
    )
    parser.add_argument(
        "file_paths", nargs="+", help="Path of the YAML file to check"
    )

    return parser.parse_args()


def lint_file(*, path: Path) -> List[Issue]:
    """Lint an RSP environemnts file (rsp-envrionments.yaml)."""
    rsp_envs = yaml.safe_load(path.read_text())

    issues: List[Issue] = []

    for env_key, env_data in rsp_envs.items():
        issues.extend(
            lint_science_platform_values(
                path=path, env_key=env_key, env_data=env_data
            )
        )
        issues.extend(
            lint_gafaelfawr_values(
                path=path, env_key=env_key, env_data=env_data
            )
        )

    return issues


def lint_science_platform_values(
    *, path: Path, env_key: str, env_data: Dict[str, Any]
) -> List[Issue]:
    """Lint data that can be found in the science-platform/values-<env>.yaml
    Helm values file.
    """
    issues: List[Issue] = []
    values_url = (
        "https://raw.githubusercontent.com/lsst-sqre/phalanx/master/"
        f"science-platform/values-{env_data['phalanx']}.yaml"
    )
    r = requests.get(values_url)
    if r.status_code != 200:
        issues.append(
            GeneralIssue(
                path=path,
                keys=[env_key, "phalanx"],
                message=f"{env_data['phalanx']} is not in the phalanx "
                "repository.",
            )
        )
        return issues

    values_data = yaml.safe_load(r.text)

    fqdn = values_data["fqdn"]
    issues.extend(
        lint_url(
            path=path,
            env_key=env_key,
            env_data=env_data,
            url_key="squareone",
            expected_url=f"https://{fqdn}/",
        )
    )
    issues.extend(
        lint_url(
            path=path,
            env_key=env_key,
            env_data=env_data,
            url_key="nb",
            expected_url=f"https://{fqdn}/nb",
        )
    )

    return issues


def lint_url(
    *,
    path: Path,
    env_key: str,
    env_data: Dict[str, Any],
    url_key: str,
    expected_url: str,
) -> List[Issue]:
    issues: List[Issue] = []

    try:
        url = env_data["urls"][url_key]
    except KeyError:
        issues.append(
            GeneralIssue(
                path=path,
                keys=[env_key, "urls", url_key],
                message="Key is missing. " f"Value should be {expected_url}",
            )
        )
    if url != expected_url:
        issues.append(
            KeyValueIssue(
                path=path,
                keys=[env_key, "urls", url_key],
                existing=url,
                correct=expected_url,
            )
        )
    return issues


def lint_gafaelfawr_values(
    *, path: Path, env_key: str, env_data: Dict[str, Any]
) -> List[Issue]:
    """Lint data that can be found in the services/gafaelfawr/values-<env>.yaml
    Helm values file.
    """
    issues: List[Issue] = []

    if "github_teams" not in env_data.keys():
        # Nothing to check against
        return issues

    values_url = (
        "https://raw.githubusercontent.com/lsst-sqre/phalanx/master/"
        f"services/gafaelfawr/values-{env_data['phalanx']}.yaml"
    )
    r = requests.get(values_url)
    if r.status_code != 200:
        issues.append(
            GeneralIssue(
                path=path,
                keys=[env_key, "github_teams"],
                message=f"A gafaelfwar values file is not available for "
                f"{env_data['phalanx']} in phalanx ",
            )
        )
        return issues

    values_data = yaml.safe_load(r.text)

    try:
        notebook_exec_configs = values_data["gafaelfawr"]["config"][
            "groupMapping"
        ]["exec:notebook"]
    except KeyError:
        try:
            notebook_exec_configs = values_data["gafaelfawr"]["config"][
                "group_mapping"
            ]["exec:notebook"]
        except KeyError:
            issues.append(
                GeneralIssue(
                    path=path,
                    keys=[env_key, "github_teams"],
                    message=f"A gafaelfwar exec:notebook group mapping is not "
                    f"available for {env_data['phalanx']} in phalanx. "
                    f"Check {values_url}",
                )
            )
            return issues

    if len(notebook_exec_configs) != len(env_data["github_teams"]):
        issues.append(
            GeneralIssue(
                path=path,
                keys=[env_key, "github_teams"],
                message=f"Number of teams does not match that in {values_url}",
            )
        )

    for team in env_data["github_teams"]:
        gafaelfawr_team_name = team.replace("/", "-")
        if gafaelfawr_team_name not in notebook_exec_configs:
            issues.append(
                GeneralIssue(
                    path=path,
                    keys=[env_key, "github_teams"],
                    message=f"Team {team} does not match one of "
                    f"{notebook_exec_configs}",
                )
            )

    return issues


def report_issues(*, path: Path, issues: Sequence[Issue]) -> None:
    if len(issues) == 0:
        print(f"✨ {path.name} looks right ✨")
        return

    print(f"\n🚨 Found {len(issues)} issues in {path.name}.")
    for issue in issues:
        print(issue)


@dataclass
class Issue:

    path: Path

    keys: List[str]

    @property
    def key_path(self) -> str:
        return ".".join(self.keys)


@dataclass
class GeneralIssue(Issue):

    message: str

    def __str__(self) -> str:
        return f"{self.path}: {self.key_path} - {self.message}"


@dataclass
class KeyValueIssue(Issue):

    existing: Any

    correct: Any

    def __str__(self) -> str:
        return (
            f"{self.path}: {self.key_path} is '{self.existing}', but should "
            f"be '{self.correct}'"
        )


if __name__ == "__main__":
    main()
