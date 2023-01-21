from django.db import models

# Create your models here.
class Registry(models.Model):
    """Model definition for container registry."""

    reg_code = models.CharField(max_length=6, blank=False, null=False)
    name = models.CharField(max_length=120, blank=False, null=False)

    class Meta:
        """Meta definition for registry."""

        verbose_name = "registry"
        verbose_name_plural = "registrys"

    def __str__(self):
        """Unicode representation of registry."""
        pass


class Image(models.Model):
    """Model definition for image."""

    image_tag = models.CharField(max_length=10, blank=False, null=False)
    registry = models.ForeignKey(
        Registry, related_name="ImageRegistry", on_delete=models.CASCADE
    )

    class Meta:
        """Meta definition for image."""

        verbose_name = "image"
        verbose_name_plural = "images"

    def __str__(self):
        """Unicode representation of image."""
        pass
