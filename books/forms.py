from django.forms import ModelForm
from books import models

class RegisterForm(ModelForm):
    class Meta:
        model = models.BookModel
        fields = '__all__'