from django import forms
from crawler.models import Project

class ProjectForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    domain = forms.URLField(widget=forms.TextInput(attrs={'class':'form-control'}), help_text = "Ex : http://domain.com ou https://domain.com")
    

    class Meta:
        model = Project
        fields = ('name', 'domain',)
        