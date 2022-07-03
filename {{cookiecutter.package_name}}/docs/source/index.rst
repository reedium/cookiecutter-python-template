{{cookiecutter.package_display_name}}
{{cookiecutter.package_display_name|length * '#' }}

{{cookiecutter.package_description}}

.. toctree::
   :maxdepth: 2
   :numbered:
   :hidden:

   user/index
   dev/index


Quick Start
===========

{{cookiecutter.package_display_name}} is not yet available on PyPI.

.. code-block:: console

    $ pip install .

After installing {{cookiecutter.package_display_name}} you can use it like any other Python module.

Here is a simple example:

.. code-block:: python

    import {{cookiecutter.package_name}}
