import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'helloWorld'
author = 'YoussefMabrouk'
version = '1.0'
release = '1.0'
extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'sphinx_rtd_theme'
