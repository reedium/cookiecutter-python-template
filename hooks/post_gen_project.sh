#!/bin/bash
poetry install && git init -b {{cookiecutter.git_branch}} && poetry run pre-commit install
