from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    """we creating a form that will allow us to create a room
    based on some values/fields in our table"""
    class Meta:
        model = Room
        fields = '__all__'
