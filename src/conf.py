# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CodeSolid.com'
copyright = '2024, John Lockwood'
author = 'John Lockwood'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

extensions = ['myst_nb', 'nbsphinx']

myst_enable_extensions = [	
 "amsmath",
 "dollarmath",
]

source_suffix = {
    '.rst': 'restructuredtext'
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static', "../images"]
html_extra_path = ['extras', 'extras/favicon.ico', 'extras/*.js']
html_theme_path = ['../themes']

html_theme_options = {
    'analytics_id': 'G-3KNPRGQ15C'
}
