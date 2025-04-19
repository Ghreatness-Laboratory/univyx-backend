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

Getting Started
===============

To get started with this project, ensure you have `Poetry` installed. If you don't have Poetry, install it using:

.. code-block:: sh

   curl -sSL https://install.python-poetry.org | python3 -

   pip install poetry

After installing Poetry, set up the project dependencies by running:

.. code-block:: sh

   poetry install

This will create a virtual environment and install all required dependencies.

This project includes a **'poetry.lock'** file, ensuring that all dependencies are installed exactly as specified.

To set up the project, simply run:

.. code-block:: sh

   poetry install

This will:
- Install all dependencies exactly as locked in **'poetry.lock'**, ensuring consistency.
- Automatically create a virtual environment (unless Poetry is set to use the system interpreter).

Installation Guide
==================

1. **Clone the Repository** (if using Git):

   .. code-block:: sh

       git clone <your-repo-url>
       cd univyx_backend

2. **Create a Virtual Environment (Recommended):**

   .. code-block:: sh

       poetry env use python

3. **Activate the Virtual Environment (if needed):**

   .. code-block:: sh

       poetry shell

4. **Install Dependencies:**

   .. code-block:: sh

       poetry install

Running the Project
===================

After setting up, run the project using:

.. code-block:: sh

    poetry run py -m core.manage runserver

To specify a settings file, use:

.. code-block:: sh

    poetry run py -m core.manage runserver --settings=univyxApi.settings.development

*(Navigate to the UnivyxApi Folder first before running this.)*

🚀 Development Quickstart
--------------------------

### Running Django Commands Easily

We use a custom `dev.bat` script to streamline local development.

**Features of `dev.bat`:**
- ✅ Automatically kills any running Django `runserver` processes.
- ✅ Activates the virtual environment (`venv\Scripts\activate.bat`).
- ✅ Handles app creation:
  - Running `dev.bat startapp app_name` automatically creates the app inside the `core/` directory.
- ✅ Executes any other manage.py commands via Poetry.

**Usage Examples:**

```bash
# Start the server
dev.bat runserver

# Create a new Django app inside core/
dev.bat startapp blog

# Make migrations
dev.bat makemigrations

# Apply migrations
dev.bat migrate
```

**How It Works Internally:**
1. Checks and kills any running Django dev servers.
2. Activates the virtual environment.
3. If `startapp` is passed, creates the app inside `core/`.
4. Otherwise, forwards commands to `poetry run py -m core.manage`.


Required Packages
=================

To run this project, you need to install the following packages:

- **asgiref** - ASGI specs, helper code, and adapters.
- **django** - A high-level Python web framework that encourages rapid development.
- **django-cors-headers** - Handles server headers required for Cross-Origin Resource Sharing (CORS).
- **django-split-settings** - Organize Django settings into multiple files and directories.
- **djangorestframework** - Web APIs for Django, made easy.
- **python-dotenv** - Read key-value pairs from a `.env` file and set them as environment variables.
- **sqlparse** - A non-validating SQL parser.
- **tzdata** - Time zone data.

Managing Dependencies
=====================

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

   poetry



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
| shared/              | Comment, Bookmark   |
|                      | Like, View etc      |
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

1. Create `models/my_new_model.py`
2. Inherit from `ContentBaseModel` or `models.Model`
3. Set `Meta.app_label = "<your_app>"` if needed
4. Register in `models/__init__.py`
5. Add Service, Repository, APIView, and Serializer

Why GenericRelation?
~~~~~~~~~~~~~~~~~~~~
Allows models to link flexibly to any other model without defining static `ForeignKey` fields.

Example:

.. code-block:: python

   class Article(ContentBaseModel):
       comments = GenericRelation(Comment)
       bookmarks = GenericRelation(Bookmark)

   article.comments.all()
   article.bookmarks.count()


🛠 Shared App Structure
--------------------------

A new `shared` app centralizes reusable code and core features.

**Inside `shared/engagements/`:**
- Like functionality
- Bookmark functionality
- Comment functionality
- View functionality (**work in progress**)

🧩 How `models.py` in `shared` Works
---------------------------------------

| Model | Purpose |
|---|---|
| `BaseTimestampModel` | Adds `UUID id`, `public_id`, `slug`, and `date_created` automatically. |
| `ReadableContentModel` | Calculates `read_time` and generates `excerpt` from content. |
| `ContentBaseModel` | Combines timestamp and readable models for articles, posts, etc. |
| `AbstractContentTypeCBLV` | Base for user-driven actions on any model (like, comment, bookmark, view) using the Django ContentType framework. |
| `Comment`, `Bookmark`, `Like`, `View` | Implementations tied to any object dynamically via `GenericForeignKey`. |

Shared Abstract Base Models
---------------------------

Located in `shared/models.py`.

**BaseTimestampModel**

- Fields: `id (UUID)`, `slug`, `date_created`

**ReadableContentModel**

- Fields: `content`, `read_time`, `excerpt`
- Methods: `calculate_read_time()`, `generate_excerpt()`

**ContentBaseModel**

- Combines `BaseTimestampModel` + `ReadableContentModel`
- Fields: `title`, `image`, `category`

Shared Utilities
----------------

**Base64ImageField** (`shared/utils/fields.py`)

Custom DRF field to handle Base64-encoded images (used in SPA/mobile apps).

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
           

🛠 Core Backend Structure (Repositories, Services, Views)
-----------------------------------------------------------

### 📦 Repositories

Repositories abstract and encapsulate database access logic.

**Why use it?**    
- Keeps database queries in one place.
- Easier to mock during tests.
- Reduces duplication across services.

| Repository | Purpose |
|---|---|
| `BaseRepository` | Basic CRUD operations (`get_all`, `get_by_id`, `create`, `update`, `delete`). |
| `BaseToggleRepository` | Special logic for toggle actions (like/bookmark/view) tied to a user and a generic object using ContentType. |

### 🛠 Services

Services contain business logic and use repositories under the hood.

**Why use it?**  
- Keeps views extremely thin.
- Business rules and database access are separated.
- Makes scaling and refactoring easier.

| Service | Purpose |
|---|---|
| `BaseService` | Generic service layer supporting `list`, `retrieve`, `create`, `update`, and `delete` operations by interacting with repositories. |

### 🖥 Views

Views only coordinate requests and responses — no business logic inside.

| View | Purpose |
|---|---|
| `BaseContentAPIView` | An abstract DRF `APIView` for generic GET, POST, PUT, DELETE operations. It uses a `service_class`, `model_class`, and `serializer_class` that you specify in each concrete view. |

**How BaseContentAPIView Works:**
- **GET**:
  - With `pk`: retrieve a single object.
  - Without `pk`: list all objects.
- **POST**: create an object.
- **PUT**: update an object.
- **DELETE**: delete an object.

🧠 Why This Architecture?
--------------------------

| Benefit | Description |
|---|---|
| Separation of Concerns | Views, services, repositories each do one job. |
| Easier Testing | You can unit test services and repositories without touching the views. |
| Scalable and Maintainable | Adding new features or changing database structure won't require touching everything. |
| Clean Code | Easier for any developer to pick up the project later. |



