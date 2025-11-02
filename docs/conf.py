# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
"""
Configuration file for building documentation.

Sphinx builds the docs using couple of external modules: napoleon and nbsphinx.

The overall format is controlled by `.rst` files. The top level file is `index.rst`

`napoleon` builds the API in HTML assuming that the code is documented with
docstrings that follow the Google docstring format.

`nbsphinx` convert the Jupyter notebooks to html with nbsphinx, will
"""
import os.path
import sys

# Add parent directory to path to import RigolWFM
here = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(here, '..'))

import RigolWFM

project = 'rigolwfm-dho800'
internal_package = 'RigolWFM'
master_doc = 'index'

release = RigolWFM.__version__
author = RigolWFM.__author__
copyright = RigolWFM.__copyright__

# Sphinx extension modules
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx_automodapi.automodapi',
    'nbsphinx',
]
numpydoc_show_class_members = False
napoleon_use_param = False
napoleon_use_rtype = False

# List of patterns, relative to source directory, of files to ignore
exclude_patterns = ['_build',
                    '**.ipynb_checkpoints',
                    'first_version',
                    'sources',
                    'manuals',
                    ]

# I execute the notebooks manually in advance. 
nbsphinx_execute = 'never'
nbsphinx_allow_errors = True

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_scaled_image_link = False
html_sourcelink_suffix = ''
