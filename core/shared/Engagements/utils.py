from django.apps import apps
from django.shortcuts import get_object_or_404

def get_object_from_url(model_name: str, public_id: int, app_label='entertainment'):
    model_name = model_name.lower()
    try:
        model = apps.all_models[app_label].get(model_name)
    except:
        raise LookupError(f"Model '{model_name}' not found in app '{app_label}'.")
    return get_object_or_404(model, public_id=public_id)

