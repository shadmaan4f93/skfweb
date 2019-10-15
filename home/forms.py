from django import forms
from .models import Subject, UploadedWork


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('subject',)
        labels = {
            'subject': 'Select subject' 
        }
        help_texts = {
            'Subject_name': 'Please select subject that we can explain better'
        }

class UploadedWorkForm(forms.ModelForm):
    class Meta:
        model = UploadedWork
        fields = ('name', 'email', 'srsdoc', 'descriptions')
        labels = {
            'name': 'Enter your name',
            'email': 'Enter your email',
            'srsdoc': 'Upload SRS Document',
            'descriptions': 'Description about work'
        }

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    comments = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'rows': 4, 'cols': 40, 'placeholder': 'Comments'}))