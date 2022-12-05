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

class PostForm(forms.ModelForm):

    title = forms.CharField(help_text='maksymalnie 200 znaków')
    class Meta:
        model=Post
        fields=['title','text','image']

