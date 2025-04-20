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
        __init__.py          
        academics/           
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
        entertainment/       
            Repository/
            Services/
            models/
                __init__.py
                models.py
                articles.py
                news.py
                events.py
            views/
                __init__.py
                views.py
            __init__.py
            apps.py
            urls.py 
        shared/       
            Engagements/
                repository/
                services/
                views/
                __init__.py
                serializers.py
                utils.py
            Repository/
                __init__.py
                base_repository.py
                base_toggle_repository.py
            Services/
                __init__.py
                base_service.py
            utils/
                __init__.py
                file_uploads.py
            views/
                __init__.py
                base_view.py
            __init__.py
            apps.py
            consumers.py   
            models.py      
            permissions.py   
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
            settings/
                __init__.py
                base.py
                development.py
                production.py
            __init__.py
            wsgi.py
            asgi.py
            urls.py
        manage.py            

Getting Started
===============

To get started with this project, ensure you have `Poetry` installed. Install it using:

.. code-block:: sh

   curl -sSL https://install.python-poetry.org | python3 -

   pip install poetry

After installing Poetry, set up the project dependencies:

.. code-block:: sh

   poetry install

This will:
- Install all dependencies locked in **'poetry.lock'**.
- Automatically create a virtual environment unless configured otherwise.

Installation Guide
==================

1. Clone the Repository:

   .. code-block:: sh

       git clone <your-repo-url>
       cd univyx_backend

2. Create a Virtual Environment (Recommended):

   .. code-block:: sh

       poetry env use python

3. Activate the Virtual Environment:

   .. code-block:: sh

       poetry shell

4. Install Dependencies:

   .. code-block:: sh

       poetry install

Running the Project
===================

To run the project:

.. code-block:: sh

    poetry run py -m core.manage runserver

To specify a settings file:

.. code-block:: sh

    poetry run py -m core.manage runserver --settings=univyxApi.settings.development

*(Navigate to the UnivyxApi folder first before running this.)*

Development Quickstart
======================

Running Django Commands Easily
-------------------------------

We use a custom `dev.bat` script to streamline local development.

Features of `dev.bat`:
- Automatically kills any running Django `runserver` processes.
- Activates the virtual environment (`venv\Scripts\activate.bat`).
- Handles app creation:
  - Running `dev.bat startapp app_name` creates the app inside `core/`.
- Executes any other `manage.py` commands via Poetry.

Usage Examples:

.. code-block:: sh

    dev.bat runserver
    dev.bat startapp blog
    dev.bat makemigrations
    dev.bat migrate

How It Works Internally:
- Kills any running Django dev servers.
- Activates the virtual environment.
- Creates apps inside `core/` if `startapp` command used.
- Otherwise forwards commands to `poetry run py -m core.manage`.

Required Packages
=================

- **asgiref**
- **django**
- **django-cors-headers**
- **django-split-settings**
- **djangorestframework**
- **python-dotenv**
- **sqlparse**
- **tzdata**

Managing Dependencies
=====================

Add a new dependency:

.. code-block:: sh

   poetry add package-name

Add a development dependency:

.. code-block:: sh

   poetry add --dev package-name

Remove a dependency:

.. code-block:: sh

   poetry remove package-name

Update dependencies:

.. code-block:: sh

   poetry update

Model Architecture
==================

Overview
--------

Univyx follows a hybrid model architecture combining:
- Traditional Django app layout
- Service and Repository layers
- Functional model files split by purpose

Model File Structure
--------------------

+----------------------+---------------------+
| File                 | Models              |
+======================+=====================+
| articles.py          | Article             |
| news.py              | News                |
| events.py            | Event               |
| shared/              | Comment, Bookmark, Like, View |
+----------------------+---------------------+

How Models Interact
--------------------

- Views → Services → Repositories → Models
- Models expose data; services encapsulate business logic
- Repositories perform CRUD with Django ORM

Lifecycle Flow
--------------

::

   User Request
      ↓
   [APIView]
      → [Service Layer]
          → [Repository]
              → [Model]

Adding New Models
-----------------

1. Create `models/my_new_model.py`.
2. Inherit from `ContentBaseModel` or `models.Model`.
3. Set `Meta.app_label = "<your_app>"` if needed.
4. Register in `models/__init__.py`.
5. Add Service, Repository, APIView, and Serializer.

Why GenericRelation?
--------------------

Allows models to link flexibly to any model without defining static `ForeignKey` fields.

Example:

.. code-block:: python

   class Article(ContentBaseModel):
       comments = GenericRelation(Comment)
       bookmarks = GenericRelation(Bookmark)

   article.comments.all()
   article.bookmarks.count()

Shared App Structure
====================

Inside `shared/engagements/`:
- Like functionality
- Bookmark functionality
- Comment functionality
- View functionality (work in progress)

Shared Models
-------------

| Model | Purpose |
|---|---|
| `BaseTimestampModel` | Adds `UUID id`, `public_id`, `slug`, and `date_created` automatically. |
| `ReadableContentModel` | Calculates `read_time` and generates `excerpt` from content. |
| `ContentBaseModel` | Combines timestamp and readable models for articles, posts, etc. |
| `AbstractContentTypeCBLV` | Base for user-driven actions on any model using the Django ContentType framework. |
| `Comment`, `Bookmark`, `Like`, `View` | Generic models linked to any object dynamically. |

Shared Utilities
----------------

**Base64ImageField** (`shared/utils/fields.py`)

Custom DRF field to handle Base64-encoded images.

.. code-block:: python

   class Base64ImageField(serializers.ImageField):
       def to_internal_value(self, data):
           if isinstance(data, str) and data.startswith('data:image'):
               format, imgstr = data.split(';base64,')
               ext = format.split('/')[-1]
               data = ContentFile(base64.b64decode(imgstr), name='upload.' + ext)
           return super().to_internal_value(data)

Usage:

.. code-block:: python

   class ArticleSerializer(serializers.ModelSerializer):
       image = Base64ImageField()

       class Meta:
           model = Article
           fields = '__all__'

Core Backend Structure
=======================

Repositories
------------

Repositories abstract database access logic.

| Repository | Purpose |
|---|---|
| `BaseRepository` | Basic CRUD operations. |
| `BaseToggleRepository` | Toggle actions (like/bookmark/view) tied to a user and object. |

Services
--------

Services contain business logic and call repositories.

| Service | Purpose |
|---|---|
| `BaseService` | Generic service layer supporting CRUD operations. |

Views
-----

Views handle request/response, no business logic inside.

| View | Purpose |
|---|---|
| `BaseContentAPIView` | Abstract DRF `APIView` with CRUD operations using services. |

How BaseContentAPIView Works:
- **GET**: List or retrieve based on `pk`
- **POST**: Create an object
- **PUT**: Update an object
- **DELETE**: Delete an object

Why This Architecture?
-----------------------

| Benefit | Description |
|---|---|
| Separation of Concerns | Views, services, repositories each have clear roles. |
| Easier Testing | Unit test services and repositories separately. |
| Scalable and Maintainable | Easier to add new features or change the database. |
| Clean Code | Easier for new developers to understand. |
