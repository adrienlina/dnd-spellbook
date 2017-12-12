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

WIZARDS OF THE COAST, DUNGEONS &amp; DRAGONS, AND THEIR LOGOS ARE TRADEMARKS
OF WIZARDS OF THE COAST LLC IN THE UNITED STATES AND OTHER COUNTRIES.
© 2016 WIZARDS. ALL RIGHTS RESERVED. THIS WEBSITE IS NOT AFFILIATED
WITH, ENDORSED, SPONSORED, OR SPECIFICALLY APPROVED BY WIZARDS OF THE
COAST LLC. THIS WEBSITE MAY USE THE TRADEMARKS AND OTHER INTELLECTUAL
PROPERTY OF WIZARDS OF THE COAST LLC, WHICH IS PERMITTED UNDER WIZARDS'
FAN SITE POLICY. FOR EXAMPLE, DUNGEONS &amp; DRAGONS® IS A TRADEMARK[S] OF
WIZARDS OF THE COAST. FOR MORE INFORMATION ABOUT WIZARDS OF THE COAST OR
ANY OF WIZARDS' TRADEMARKS OR OTHER INTELLECTUAL PROPERTY, PLEASE VISIT
THEIR WEBSITE AT (WWW.WIZARDS.COM).
