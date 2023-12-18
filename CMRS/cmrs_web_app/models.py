from django.db import models

# Create your models here.
class Jobs(models.Model):
    Title = models.CharField(_("Title"), max_length=50)
    id = models.IntegerField(_("ID"), primary_key=True)

    def __str__(self):
        return self.name
    pass

class Users(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    id = models.IntegerField(_("ID"), primary_key=True)

    def __str__(self):
        return self.name