from django.db import models
from django.core.validators import FileExtensionValidator

# Model class for category
class Category(models.Model):
    # Fields
    '''This class represents a category model.'''
    name = models.CharField(max_length=100)
    '''name of the category'''
    description = models.TextField()
    '''description of the category'''
    image = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    '''image of the category'''

    # Metadata
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    # Methods
    def __str__(self):
        return self.name
    
# Model class for playlist that is related to category model using foreign key one category to many pllaylists relationship 
class Playlist(models.Model):
    # Fields
    '''This class represents a playlist model.'''
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    '''category of the playlist'''
    audio = models.FileField(upload_to='audio/', validators=[FileExtensionValidator(['mp3'])])
    '''audio file of the item in the playlist'''
    title = models.CharField(max_length=100)
    '''title of the item in the playlist'''
    description = models.TextField()
    '''description of the item in the playlist'''
    image = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    '''image of the item in the playlist'''
    

    # Metadata
    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'

    # Methods
    def __str__(self):
        return self.title

# # Model class for playlist
# class Playlist(models.Model):
#     # Fields
#     '''This class represents a playlist model.'''
#     category = models.CharField(max_length=100)
#     '''category of the playlist'''
#     audio = models.FileField(upload_to='audio/', validators=[FileExtensionValidator(['mp3'])])
#     '''audio file of the item in the playlist'''
#     title = models.CharField(max_length=100)
#     '''title of the item in the playlist'''
#     description = models.TextField()
#     '''description of the item in the playlist'''
#     image = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
#     '''image of the item in the playlist'''
    

#     # Metadata
#     class Meta:
#         verbose_name = 'Playlist'
#         verbose_name_plural = 'Playlists'

#     # Methods
#     def __str__(self):
#         return self.title
