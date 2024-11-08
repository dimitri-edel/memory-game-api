from django.db import models
from django.core.validators import FileExtensionValidator
from category.models import Category

# Class for storing images of faces
class Face(models.Model):    
    image = models.ImageField(upload_to="faces", validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return "face for " + self.category.name
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        try:
            this = Face.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except: pass
        super(Face, self).save(*args, **kwargs)