import sphinx_theme
html_theme = 'stanford_theme'
html_theme_path = [sphinx_theme.get_html_theme_path()]

# Project information
project = 'VSAs and Cognition'
master_doc = 'index'

# Extensions
extensions = [
    "nbsphinx",
    "sphinxcontrib.bibtex",
]

# Customization
html_static_path = ["_static"]
html_css_files = ["custom.css"]
bibtex_bibfiles = ["ref.bib"]
