"""
ASGI config for UnivyxApi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
import sys

# Add entertainment to path so `shared` can be imported globally


from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "core"))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.UnivyxApi.settings')
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'core', 'entertainment'))

application = get_asgi_application()
