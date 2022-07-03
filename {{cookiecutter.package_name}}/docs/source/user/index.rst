User Guide
##########

This section of the documentation provides user focused information such as
installing and quickly using this package.

.. _install-guide-label:

Install Guide
=============

.. note::

    It is best practice to install Python projects in a virtual environment,
    which can be created and activated as follows using Python 3.6+.

    .. code-block:: console

        $ python -m venv venv --prompt myvenv
        $ source venv/bin/activate
        (myvenv) $

The simplest way to install {{cookiecutter.package_display_name}} is using Pip from the local directory's path.

.. code-block:: console

    $ pip install .

This will install ``{{cookiecutter.package_name}}`` and all of its dependencies.

**Note:** This package is not yet on pypi


{% if cookiecutter.github_repo_user|length %}
.. _report-bugs-label:

Report Bugs
===========

Report bugs at the `issue tracker <https://github.com/{{cookiecutter.github_repo_user}}/{{cookiecutter.github_repo_name}}/issues>`_.

Please include:

  - Operating system name and version.
  - Any details about your local setup that might be helpful in troubleshooting.
  - Detailed steps to reproduce the bug.
{% endif %}
