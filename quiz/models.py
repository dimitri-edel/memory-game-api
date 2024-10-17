from django.db import models
from django.core.validators import FileExtensionValidator
from category.models import Category

# Class for a quiz model that is related to category model using foreign key one category to one quiz relationship
class Quiz(models.Model):
    # Fields
    '''This class represents a quiz model.'''
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    '''category of the quiz'''
    
    # field quiz contain a json file that contain the quiz questions and answers
    json = models.FileField(upload_to='json/', validators=[FileExtensionValidator(['json'])])
    '''json file of the quiz'''
    

    # Metadata
    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    # Methods
    def __str__(self):
        return self.title
