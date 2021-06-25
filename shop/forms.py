from django.forms import ModelForm
from .models import PlayList

class PlayListForm(ModelForm):
    class Meta:
        model = PlayList
        fields = ['artista', 'cancion', 'porque']
