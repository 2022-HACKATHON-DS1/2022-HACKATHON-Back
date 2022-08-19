from django import forms
from .models import Text,Image
from .widgets import PreviewFileWidget, PreviewFileWidget1

class TextModelForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['content']

        labels = {
            'content' : '',
        }

        widgets = {

            'content' : forms.Textarea(
                attrs={
                    'id': 'input-text',
					'onkeyup': 'printName()',
                    'placeholder': '텍스트를 입력하세요. ex)지은네컷',
                }
            ),
        }

class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

        widgets = {
            'image': PreviewFileWidget1(),
        }