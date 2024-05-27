from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('upload',)

    def clean_upload(self):
        upload = self.cleaned_data.get('upload')
        if not upload.name.endswith('.docx'):
            raise forms.ValidationError("Invalid file type: only .docx files are allowed.")
        return upload
