import os.path
from pathlib import Path
from split_settings.tools import include, optional 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

print(BASE_DIR)

include(
	'settings.base.py',
)