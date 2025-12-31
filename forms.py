from django import forms 
from .models import *

class formHistory(forms.ModelForm):
    class Meta:
        model = History
        fields = [
            'headline',
            'text',           
        ]
        
        
        
class formNews(forms.ModelForm):
    class Meta:
        model = News 
        fields = [
            'headline',
            'title',
            'summary',
            'display',
            'date',
            'time',
            'image',
            'text',      
        ]
        
        
class formProject(forms.ModelForm):
    class Meta:
        model = Project 
        fields = [
            'headline',
            'date',
            'image',
            'text',          
        ]
        
        
class formCouncils(forms.ModelForm):
    class Meta:
        model =  Councils
        fields = [
            'headline',
            'date',
            'image',
            'text',    
        ]
        
        
class formMayor(forms.ModelForm):
    class Meta:
        model = Mayor 
        fields = [
            'headline',
            'date',
            'image',
            'text',          
        ]


class formCelebrities(forms.ModelForm):
    class Meta:
        model =  Celebrities
        fields = [
            'headline',
            'image',
            'text',          
        ]


class formMartyrs(forms.ModelForm):
    class Meta:
        model =  Martyrs
        fields = [
            'headline',
            'image',
            'text',          
        ]


class formPersonnel(forms.ModelForm):
    class Meta:
        model = Personnel 
        fields = [
            'headline',
            'image',
            'semat',          
        ]


class formMunicipality(forms.ModelForm):
    class Meta:
        model = Municipality 
        fields = [
            'masahat',
            'population',      
        ]