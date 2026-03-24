from django.db import models


class todolist(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class item(models.Model):
    todolist=models.ForeignKey(todolist, on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    complete=models.BooleanField()
    def __str__(self):
        return self.text
