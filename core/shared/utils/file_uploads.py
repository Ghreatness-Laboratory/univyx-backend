# file/image upload helpers
import base64
import uuid
from io import BytesIO
from PIL import Image, UnidentifiedImageError
from django.core.files.base import ContentFile
from rest_framework import serializers


class Base64ImageField(serializers.ImageField):
    """
    Accepts base64-encoded image strings as well as normal image files.
    Uses Pillow for image validation.
    """

    def to_internal_value(self, data):
        # Handle normal image file upload
        if isinstance(data, ContentFile) or hasattr(data, 'read'):
            return super().to_internal_value(data)

        # Handle base64 string
        if isinstance(data, str) and data.startswith("data:image"):
            try:
                # Parse base64 header
                format_str, base64_str = data.split(";base64,")
                file_ext = format_str.split("/")[-1]

                decoded_img = base64.b64decode(base64_str)
                file_name = f"{uuid.uuid4()}.{file_ext}"

                #  Validate image using Pillow
                try:
                    img = Image.open(BytesIO(decoded_img))
                    img.verify()  # Raises if image is not valid
                except UnidentifiedImageError:
                    raise serializers.ValidationError("Uploaded file is not a valid image")

                return super().to_internal_value(ContentFile(decoded_img, name=file_name))

            except Exception:
                raise serializers.ValidationError("Invalid base64 image string")

        raise serializers.ValidationError("Unsupported image format")
