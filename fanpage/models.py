from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.

class Fanpage(models.Model):
    name = models.CharField(max_length=45, default="Anonymous")
    date_added = models.DateTimeField(default=timezone.now)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    last_updated = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)


class FanpageForms(ModelForm):
    class Meta:
        model = Fanpage
        fields = "__all__"
        exclude = ['date_added', 'last_updated', 'is_active']