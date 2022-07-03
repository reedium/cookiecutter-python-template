Developers Guide
################

.. _testing-label:

Testing
=======

The {{cookiecutter.package_display_name}} project implements a regression
test suite that improves developer productivity by identifying capability
regressions early.

Developers implementing fixes or enhancements must ensure that they have
not broken existing functionality. The {{cookiecutter.package_display_name}}
project provides some convenience tools so this testing step can be quickly
performed.

.. code-block:: console

    ({{cookiecutter.package_name}}) $ pytest -v

Individual unit tests can be run also.

.. code-block:: console

    ({{cookiecutter.package_name}}) $ pytest -v test_name


Code Style
==========

Adopting a consistent code style assists with maintenance. This project uses
Black to format code, flake8, and isort to sort imports

.. _annotations-label:

Type Annotations
----------------

The code base contains type annotations to provide helpful type information
that can improve code maintenance.


.. _documentation-label:

Documentation
=============

To simplify testing and generation, give `sphinx-autobuild` a shot, which will build and start a server for testing:

.. code-block:: console

    ({{cookiecutter.package_name}}) $ sphinx-autobuild docs/source docs/build/html

In the future, we may integrate and automate doc autobuild as well.


.. _release-label:

Release Process
===============

The following steps are used to make a new software release.

The steps assume they are executed from within a development virtual
environment.

- Check that the package version label in ``pyproject.toml`` is correct.

- Create and push a repo tag to Github. As a convention use the package
  version number (e.g. YY.MM.MICRO) as the tag.

  .. code-block:: console

      $ git checkout master
      $ git tag YY.MM.MICRO -m "A meaningful release tag comment"
      $ git tag  # check release tag is in list
      $ git push --tags origin master

  - This will trigger Github to create a release at:

    ::

        https://github.com/{username}/{{cookiecutter.package_name}}/releases/{tag}
