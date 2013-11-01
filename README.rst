===========
Deform Demo
===========

Example of how to make a CMS with Deform, Colander and Pyramid.

To Setup the Project
====================
::

    mkvirtualenv deform_demo
    python setup.py develop
    initialize_deform_demo_db development.ini

This will set-up an sqlite DB.

To Run
======
::

    pserve development.ini --reload


TODO
====

#. Done - Display a form for a recipe

#. Done - Save a recipe (to the DB)

#. List recipes

#. Edit a recipe

#. Delete a recipe

#. check for unique on form (Colander and SQLAlchemy)

#. Custom validation error (matching fields)

#. Custom html? (Deform Retail like Rob suggested)

#. Use different model for RecipeIngredients (drop-down).

#. Use different model for ingredients (auto-complete)

#. PW Protect. Add users form with custom validation.

#. Use Postgres DB

#. Tests
