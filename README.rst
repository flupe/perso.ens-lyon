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


About ReST
~~~~~~~~~~

Since this tool is built upon ``docutils``, the default syntax of ReST has been extended a bit.
A few new directives are aivailable to take math notes:

.. code::

   .. lemma:: some lemma

      a named lemma

   .. theorem::

      the content of some unnamed theorem

   .. proof::

      a proof too

   .. definition:: a definition block

      a named definition



   .. note:: some note about the content

   .. remark:: an additional remark about the content
