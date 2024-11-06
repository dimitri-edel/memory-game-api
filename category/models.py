from django.db import models
from django.core.validators import FileExtensionValidator
from quiz.models import Quiz
from playlist.models import Playlist  # Import Playlist model

# Model class for category
class Category(models.Model):
    # Fields
    '''This class represents a category model.'''
    name = models.CharField(max_length=100)
    '''name of the category'''
    description = models.TextField()
    '''description of the category'''
    image = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'webp'])])
    '''image of the category'''

    # Metadata
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    # Methods
    def __str__(self):
        return self.name
    
    # Override the delete method to delete the image file from the storage
    def delete(self, *args, **kwargs):
        # Delete related quizzes
        quizzes = Quiz.objects.filter(category=self)
        for quiz in quizzes:
            quiz.delete()
        
        # Delete related playlists
        playlists = Playlist.objects.filter(category=self)
        for playlist in playlists:
            playlist.delete()
        
        self.image.delete()
        super().delete(*args, **kwargs)

    # Override the save method to delete the old image file from the storage
    def save(self, *args, **kwargs):
        try:
            this = Category.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except: pass
        super(Category, self).save(*args, **kwargs)