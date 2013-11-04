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

This uses an MySQL DB called deform_demo.

To Run
======
::

    pserve development.ini --reload


TODO
====

#. Done - Display a form for a recipe

#. Done - Save a recipe (to the DB)

#. Done - List recipes

#. Done - Add recipe instructions

#. Done - Edit a recipe

#. Edit recipe instructions

#. Done - Delete a recipe

#. Add extra models, add to CMS with minimal code (with-in reason)

#. Pagnation

#. Search

#. check for unique on form (Colander and SQLAlchemy)

#. Custom validation error (matching fields)

#. Custom html? (Deform Retail like Rob suggested)

#. Add Alembic

#. Add extra fields

#. Use different model for RecipeIngredients (drop-down).

#. Use different model for ingredients (auto-complete)

#. PW Protect. Add users form with custom validation.

#. Use Postgres DB

#. Tests

#. Prompt on delete
