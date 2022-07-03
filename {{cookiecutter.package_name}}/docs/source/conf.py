# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import sys

from datetime import datetime

from sphinx.ext import apidoc

# sys.path.insert(0, os.path.abspath('.'))

# Get the version from the pyproject.toml configuration
regexp = re.compile(r'.*version = [\'\"](.*?)[\'\"]', re.S)
repo_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
init_file = os.path.join(repo_root, 'pyproject.toml')
with open(init_file, 'r') as f:
    module_content = f.read()
    match = regexp.match(module_content)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError(
            'Cannot find version in {}'.format(init_file))


# -- Project information -----------------------------------------------------

project = '{{cookiecutter.package_display_name}}'
copyright = '{% now "utc", "%Y" %}, {{cookiecutter.author_name}}'
author = '{{cookiecutter.author_name}}'
release = version # The full version, including alpha/beta/rc tags.
version = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# Suppress nonlocal image warnings
suppress_warnings = ['image.nonlocal_uri']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'description': '{{cookiecutter.package_description}}',
    'show_powered_by': False,
    # 'logo': 'my-logo.png',
    'logo_name': False,
    'page_width': '80%',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
