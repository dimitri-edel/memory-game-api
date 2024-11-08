from django.db import models
from django.core.validators import FileExtensionValidator
from category.models import Category

# Class for stroing styles for a category
class Style(models.Model):
    # Fields
    primary_color = models.CharField(max_length=9)
    '''primary color of the style'''
    secondary_color = models.CharField(max_length=9)
    '''secondary color of the style'''
    complementary_color = models.CharField(max_length=9)
    '''complementary color of the style'''
    background_image = models.ImageField(upload_to="styles", validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])])
    '''background image of the style'''
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    '''category of the style'''
    
    
    # Metadata
    class Meta:
        verbose_name = 'Style'
        verbose_name_plural = 'Styles'
    
    # Methods
    def __str__(self):
        return "style for " + self.category.name
    
    # Override the delete method to delete the image file from the storage
    def delete(self, *args, **kwargs):
        self.background_image.delete()
        super().delete(*args, **kwargs)

    # Override the save method to delete the old image file from the storage
    def save(self, *args, **kwargs):
        try:
            this = Style.objects.get(id=self.id)
            if this.background_image != self.background_image:
                this.background_image.delete()
        except: pass
        super(Style, self).save(*args, **kwargs)