======================================
Univyx Backend - Django & Poetry Setup
======================================

.. contents:: Table of Contents
   :depth: 2

Overview
========
Univyx Backend is a Django-based backend for handling academic and entertainment modules.
It is structured using a **modularized architecture** and managed using **Poetry**.

The applications follow a **hybrid structure**, combining both the **traditional Django structure** and a **service-repository pattern** for better scalability and maintainability.

Additionally, the project uses **split settings**, allowing better configuration management by separating different settings files (e.g., `development.py`, `production.py`).

Project Structure
=================

::

    core/
        __init__.py          # Marks core as a Python module
        academics/           # Hybrid-structured app (Django + Service-Repository Pattern)
            Repository/
            Services/
            models/
                __init__.py
                models.py
            views/
                __init__.py
                views.py
            __init__.py
            apps.py
            urls.py
        entertainment/       # Hybrid-structured app
            Repository/
            Services/
            models/
                __init__.py
                models.py
                articles.py   # Article model
                news.py       # News model
                events.py     # Events model
            views/
                __init__.py
                views.py
            __init__.py
            apps.py
            urls.py
        accounts/
            models/
                __init__.py
                models.py
            views/
                __init__.py
                views.py
            __init__.py
            apps.py
            urls.py
        univyxApi/
            settings/        # Split settings implementation
                __init__.py
                base.py
                development.py
                production.py
            __init__.py
            wsgi.py
            asgi.py
            urls.py
        manage.py            # Django's management script
-------------------------------
🚀 Getting Started
-------------------------------

To get started with this project, ensure you have `Poetry` installed. If you don't have Poetry, install it using:

.. code-block:: sh

   curl -sSL https://install.python-poetry.org | python3 -

   pip install poetry

After installing Poetry, set up the project dependencies by running:

.. code-block:: sh

   poetry install

This will create a virtual environment and install all required dependencies.

This project includes a **'poetry.lock'** file, ensuring that all dependencies are 
installed exactly as specified.

To set up the project, simply run:
.. code-block:: sh
poetry install

This will:
- install all dependencies exactly as locked in **'poetry.lock'**, ensuring consistency.
- Automatically create a virtual environment (unless Poetry is set to use the system interpreter).


Installation Guide
==================

1. **Clone the Repository** (if using Git)::

       git clone <your-repo-url>
       cd univyx_backend

2. **Create a Virtual Environment (Recommended)**::

       poetry env use python

3. **Activate the Virtual Environment** (if needed)::

       poetry shell

4. **Install Dependencies**::

       poetry install

Running the Project
===================

After setting up, run the project using::

    poetry run py -m core.manage runserver

To specify a settings file, use::

    poetry run py -m core.manage runserver --settings=univyxApi.settings.development



*(Navigate to the UnivyxApi Folder first before running this.)*



=================
Required Packages 
=================

To run this project, you need to install the following packages

- asgiref               3.8.1  ASGI specs, helper code, and adapters
- django                5.1.6  A high-level Python web framework that encourages rapid development and clean, pragmat...
- django-cors-headers   4.7.0  django-cors-headers is a Django application for handling the server headers required f...
- django-split-settings 1.3.2  Organize Django settings into multiple files and directories. Easily override and modi...
- djangorestframework   3.15.2 Web APIs for Django, made easy.
- dotenv                0.9.9  Deprecated package
- python-dotenv         1.0.1  Read key-value pairs from a .env file and set them as environment - variables
- sqlparse              0.5.3  A non-validating SQL parser.
- tzdata

-------------------------------
📦 Managing Dependencies
-------------------------------

To add a new dependency:

.. code-block:: sh

   poetry add package-name

To add a development dependency:

.. code-block:: sh

   poetry add --dev package-name

To remove a dependency:

.. code-block:: sh

   poetry remove package-name

To update dependencies:

.. code-block:: sh

   poetry update

-------------------------------
📜 License
-------------------------------






This project is licensed under the MIT License - see the `LICENSE` file for details.