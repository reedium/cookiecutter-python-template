# Python Start Project with Cookiecutter

This template allows you to easily setup new Python projects with the most important libraries and configuration files for managing dependencies and virtualenv, code formatting, debugging, testing, static code analysis and creating command-line interfaces.

This project is based on [python-new-project](https://github.com/stribny/python-new-project), with a heavy amount of changes


## What is included in the template

The template will:

- install [Pytest](https://docs.pytest.org/en/stable/) and [Pytest-sugar](https://pypi.org/project/pytest-sugar/) for tests
- install [pydantic](https://github.com/samuelcolvin/pydantic) for data validation
- install [Black](https://black.readthedocs.io/en/stable/) and [Flake8](https://flake8.pycqa.org/en/latest/) for standardization
- install [pre-commit](https://pre-commit.com/) to run Black, Flake8, etc before every commit
- install [sphinx](https://pypi.org/project/Sphinx/) and [sphinx-autobuild](https://pypi.org/project/sphinx-autobuild/) for documentation
- create `pyproject.toml` configuration file for managing project dependencies and virtual environments using [Poetry](https://python-poetry.org/)
- create `README.md` README file
- create `.gitignore` file
- initialize new Git repository


## How to use the template

This is a [cookiecutter](https://cookiecutter.readthedocs.io) template.

To use it, make sure you have at least Python 3.7 and git installed.

Then install `cookiecutter` and `poetry` via `pip`:

```
pip install poetry --user
pip install cookiecutter --user
```

You can now create a new Python project by running:

```
cookiecutter <git-url>
```

This will take you to a project setup asking for:
- `package_display_name` - The name that will be used in README, documentation, etc
- `package_name` - The Python package name and name of the project folder (will generate automatically)
- `package_description` - The Python package description
- `package_command` - This will configure poetry to allow calling the package, `package_name/console:entry_point`, via this command. Generally, this would be the same value as `package_name`
- `author_name` - The author of the package
- `author_email` - The email for the author
- `git_branch` - The branch to utilize when performing `git init -b <branch>`
- `github_repo_name` - For documentation, such as URLs to the issue tracker
- `github_user_name` - For documentation, such as URLs to the issue tracker
- `python_version`- The Python version that should be defined in `pyproject.toml`

The generated structure looks like this:

```
└── package_name/
    ├── docs
    │   ├── build
    │   ├── make.bat
    │   ├── Makefile
    │   └── source
    │       ├── conf.py
    │       ├── dev
    │       │   └── index.rst
    │       ├── index.rst
    │       └── user
    │           └── index.rst
    ├── poetry.lock
    ├── pyproject.toml
    ├── README.md
    ├── src
    │   └── package_name
    │       ├── console.py
    │       ├── __init__.py
    │       └── logger.py
    └── tests/
        ├── __init__.py
        └── test_project.py
```

From here, you can install the current dependencies, if needed running `poetry install` from within `package_name`. We can run `poetry shell` and `package_name` to run the script.


## Default Configs

The project includes [pydantic](https://github.com/samuelcolvin/pydantic) to help with configuration and settings for projects.

The provided example `console.py` allows for the following object:

```
>>> from package_name.console import Config
>>> config = Config()
>>> config
Config(api_key='EXAMPLEKEY', more_settings=SubModel(foo='bar'))
>>> config.more_settings.foo
'bar'
```

The config settings can be defined either through environment variables, such as the following:

```
API_KEY='MY_ACTUAL_KEY'
MORE_SETTINGS__FOO='OTHER'
```
