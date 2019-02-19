import os
import sys

from documenteer.sphinxconfig.utils import form_ltd_edition_name
import lsst_sphinx_bootstrap_theme


# Work around Sphinx bug related to large and highly-nested source files
sys.setrecursionlimit(2000)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'LSST Science Platform Notebook Aspect'
copyright = '2018 Association of Universities for Research in Astronomy'
author = 'LSST Data Management'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
if os.getenv('TRAVIS_BRANCH', default='master') == 'master':
    # Use the current release as the version tag if on master
    version = 'Current'
    release = version
else:
    # Use branch name as the version tag
    version = form_ltd_edition_name(
        git_ref_name=os.getenv('TRAVIS_BRANCH', default='master'))
    release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
    'README.rst'
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The reST default role cross-links Python (used for this markup: `text`)
default_role = 'py:obj'

# Intersphinx

intersphinx_mapping = {
    'python': ('http://docs.python.org/3/', None),
}

# -- Options for linkcheck builder ----------------------------------------

# The linkcheck build often failed when trying to check the actual LSP
# URLs, so we need to ignore those URLs here.
linkcheck_ignore = [r'^https://lsst-lsp-stable\.ncsa\.illinois\.edu',
                    # ignored because the homepage isn't present yet (in dev)
                    r'^https://nb\.lsst\.io$']
linkcheck_retries = 2

# -- Options for HTML output ----------------------------------------------

templates_path = [
    '_templates',
    lsst_sphinx_bootstrap_theme.get_html_templates_path()
]

html_theme = 'lsst_sphinx_bootstrap_theme'
html_theme_path = [lsst_sphinx_bootstrap_theme.get_html_theme_path()]


html_context = {
    # Enable "Edit in GitHub" link
    'display_github': True,
    # https://{{ github_host|default("github.com") }}/{{ github_user }}/
    #     {{ github_repo }}/blob/
    #     {{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}
    'github_user': 'lsst-dm',
    'github_repo': 'nb_lsst_io',
    # TRAVIS_BRANCH is available in CI, but master is a safe default
    'github_version': os.getenv('TRAVIS_BRANCH', default='master') + '/'
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {'logotext': project}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'LSP Notebook Aspect'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = '_static/lsst-logo-dark.svg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'
