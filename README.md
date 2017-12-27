# DnD Spellbook

DnD Spellbook is a web app that aims to simplify tracking of known spells and prepared spells for a DnD character.

It is built using the [Django Web Framework](https://www.djangoproject.com/) and the [arocks/edge](https://github.com/arocks/edge) boilerplate.

This project has the following basic apps:

* `spellbook`: containing the spells and user spellbooks

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

## A Note on the License

While the code produced here is MIT licensed, the D&D content is IP of Wizards.
The D&D content is used under the [Open Gaming License V1.0a](OGL.md) as available on the [Wizards website](https://media.wizards.com/2016/downloads/SRD-OGL_V1.1.pdf).
