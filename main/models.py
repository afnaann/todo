from django.db import models

# Create your models here.

    
class User(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
class TodoList(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title