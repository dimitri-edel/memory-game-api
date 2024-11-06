from django.db import models
from django.core.validators import FileExtensionValidator
from category.models import Category
from django.db.models.signals import pre_delete
from django.dispatch import receiver

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
    
    # Override delete method to delete the json file from the storage
    def delete(self, *args, **kwargs):
        self.json.delete()
        super().delete(*args, **kwargs)

    # Override save method to delete the json file from the storage
    def save(self, *args, **kwargs):
        try:
            this = Quiz.objects.get(id=self.id)
            if this.json != self.json:
                this.json.delete()
        except: pass
        super(Quiz, self).save(*args, **kwargs)

# Signal to delete associated files when a Category is deleted
@receiver(pre_delete, sender=Category)
def delete_related_files(sender, instance, **kwargs):
    quizzes = Quiz.objects.filter(category=instance)
    for quiz in quizzes:
        quiz.json.delete()

