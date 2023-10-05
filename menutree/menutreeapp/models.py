from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=150)
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# class OneLevelMenuItem(models.Model):
#     menu_item = models.ForeignKey(MenuItem, on_delete= models.CASCADE)
#     name = models.CharField(max_length=150)
#     link = models.CharField(max_length=150)

#     def __str__(self):
#         return self.name

    