===========
Deform Demo
===========

Example of how to make a CMS with Deform, Colander, Peppercorn and Pyramid.

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

1. Done - Display a form for a recipe

2. Save a recipe (to the DB)
 - make into a recipe
 - custom validation error
 - check for unique on form
 - can we have custom html? (Deform Retail like Rob suggested)

3. Edit a recipe

4. Delete a recipe

5. Use different model for RecipeIngredients (drop-down).

6. Use different model for ingredients (auto-complete)

8. Add users form with custom validation. Double email

9. Do alternative version with jinja2 instead of chameleon

10. Password protect CMS

11. use postgres DB
 - Add alelmbic

12. Tests
