===============================
Univyx Api
===============================

Welcome to **Univyx API**! This project uses `Poetry <https://python-poetry.org/>;`_ for dependency management and packaging.

.. contents:: Table of Contents
   :depth: 2

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

-------------------------------
🔧 Running the Project
-------------------------------

Activate the Poetry environment and start using the project:

.. code-block:: sh

   poetry shell

To run the application:

.. code-block:: sh

   poetry run python manage.py runserver

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