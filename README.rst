This is a static site generator for my personal online page.
It is built with the help of *docutils* and *jinja2*.

Installation
~~~~~~~~~~~~

.. code::

   python3 -m pip install --user -e .


Usage
~~~~~

Write your content as ``.rst`` files in the ``content/`` folder.
Then, run ``perso build`` from the main directory. It should create a ``build/`` folder and produce everything needed.

If you're working on the template and want to build files that weren't modifiers since the last build, you can pass an additional flag:

.. code::

   perso build --force

To view the result, and in order for the CSS to work properly, it is advised to launch a local server at the root of ``build/``.

.. code::

   cd build
   python -m http.server


About ReST
~~~~~~~~~~

Since this tool is built upon ``docutils``, the default syntax of ReST has been extended a bit.

What you define with the ``meta`` directive will be given to the template being used.
Note that the ``:template:`` attribute allows you to specify which view of the template you want to render your content in.

For example:

.. code:: rst

   .. meta::
      :template: single

This content will be rendered in *a single-column view*.

A few new directives are aivailable to take math notes:

.. code:: rst

   .. lemma:: Some Lemma

      A named lemma entitled *Some Lemma*.


   .. theorem::

      The content of some unnamed theorem.


   .. proof::

      We can write proofs too.


   .. definition:: A definition block

      A named definition.


   .. note:: Some note about the content.

   .. remark:: An additional remark about the content
