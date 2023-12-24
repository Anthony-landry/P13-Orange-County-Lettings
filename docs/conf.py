# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

import django

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'P13 Orange County Lettings’s'
copyright = '2023, Landry Anthony'
author = 'Landry Anthony'
release = 'v1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

sys.path.insert(0, os.path.abspath(".."))  # For discovery of Python modules

# Note: You may need to change the path to match
# your project's structure
sys.path.insert(0, os.path.abspath(".."))  # For discovery of Python modules
sys.path.insert(0, os.path.abspath("."))  # For finding the django_settings.py file

# This tells Django where to find the settings file
os.environ["DJANGO_SETTINGS_MODULE"] = "django_settings"
# This activates Django and makes it possible for Sphinx to
# autodoc your project
django.setup()
