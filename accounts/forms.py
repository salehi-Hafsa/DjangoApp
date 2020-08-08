from django.forms import ModelForm
from django.contrib.auth import (
    authenticate,
    get_user_model
)




from .models import offres


class offresForm(ModelForm):
    class Meta:
        model = offres
        fields = '__all__'

