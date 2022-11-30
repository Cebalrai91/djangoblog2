from django import forms
from .models import *


# class ImgForm(forms.ModelForm):
#
#     class Meta:
#         model = Post
#         fields = ['image']


class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        fields = ['name', 'image']
