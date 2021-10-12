# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'lambeq'
copyright = '2021, Cambridge Quantum Computing Ltd.'
author = 'Cambridge Quantum QNLP Dev Team'

version = '0.1.0'
release = '0.1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'm2r2',
    'nbsphinx',
    'numpydoc',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

autodoc_default_options = {
    'members': True,
    'inherited-members': True,
    'undoc-members': True,
    'special-members': '__init__, __call__',
}

# This disables the need to document methods in the class docstring.
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


def autodoc_skip_member(app, what, name, obj, skip, options):
    if name == 'Symbol':
        options['inherited-members'] = False
        return False
    return skip


def setup(app):
    app.connect('autodoc-skip-member', autodoc_skip_member)


numfig = True