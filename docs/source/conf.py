# -*- coding: utf-8 -*-
#
# jsonextended documentation build configuration file, created by
# sphinx-quickstart on Sat Jun  3 02:06:22 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
     'sphinx.ext.napoleon',
     'sphinx.ext.autosummary']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'jsonextended'
copyright = u'2017, Chris Sewell'
author = u'Chris Sewell'
description = 'Extending the python json package functionality'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.0.1'
# The full version, including alpha/beta/rc tags.
release = u'0.0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'jsonextendeddoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'jsonextended.tex', u'jsonextended Documentation',
     u'Chris Sewell', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'jsonextended', u'jsonextended Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'jsonextended', u'JSON Extended',
     author, 'jsonextended', description,
     'Miscellaneous'),
]


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# Napoleon settings
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True

# adapted from https://github.com/markovmodel/PyEMMA/blob/devel/doc/source/conf.py#L285
# and discussed here: https://stackoverflow.com/questions/20569011/python-sphinx-autosummary-automated-listing-of-member-functions
def setup(app):
    #app.connect('autodoc-skip-member', skip_deprecated)
    try:
        from sphinx.ext.autosummary import Autosummary
        #from sphinx.ext.autosummary import get_documenter
        from docutils.parsers.rst import directives
        #from sphinx.util.inspect import safe_getattr
        #import re
        import inspect
        from types import FunctionType

        class AutoFunctionSummary(Autosummary):

            option_spec = {
                'functions': directives.unchanged,
                'classes': directives.unchanged,
                'toctree': directives.unchanged,
                'nosignatures':directives.unchanged
            }

            required_arguments = 1
                
            @staticmethod
            def get_functions(mod):

                def is_function_local(obj):
                    return isinstance(obj, FunctionType) and obj.__module__ == mod.__name__

                members = inspect.getmembers(mod, predicate=is_function_local)
                return [name for name,value in members if not name.startswith('_')]

            @staticmethod
            def get_classes(mod):

                def is_class_local(obj):
                    return inspect.isclass(obj) and obj.__module__ == mod.__name__

                members = inspect.getmembers(mod, predicate=is_class_local)
                return [name for name,value in members if not name.startswith('_')]

            def run(self):
                
                mod_path = self.arguments[0]
                
                (package_name, mod_name) = mod_path.rsplit('.', 1)
                pkg = __import__(package_name, globals(), locals(), [mod_name])
                mod = getattr(pkg, mod_name)
            
                if 'classes' in self.options:
                    klasses = self.get_classes(mod)
                    self.content = ["~%s.%s" % (mod_path, klass) for klass in klasses if not klass.startswith('_')]
                if 'functions' in self.options:                    
                    functions = self.get_functions(mod)
                    content = ["~%s.%s" % (mod_path, func) for func in functions if not func.startswith('_')]
                    if self.content:
                        self.content += content
                    else:
                        self.content = content
                try: 
                    pass                   
                finally:
                    return super(AutoFunctionSummary, self).run()

        app.add_directive('autofuncsummary', AutoFunctionSummary)
    except BaseException as e:
        raise e
