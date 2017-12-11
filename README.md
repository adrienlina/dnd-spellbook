# DnD Spellbook

DnD Spellbook is a web app that aims to simplify tracking of known spells and prepared spells for a DnD character.

It is built with [Python][0] using the [Django Web Framework][1], and the [arocks/edge](https://github.com/arocks/edge) boilerplate.

This project has the following basic apps:

* TBC

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv dnd_spellbook`
    2. `$ . dnd_spellbook/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate
