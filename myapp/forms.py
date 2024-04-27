from django import forms
from myapp.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie 
        fields='__all__'

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'director':forms.TextInput(attrs={'class':'form-control'}),
            'year':forms.TextInput(attrs={'class':'form-control'}),
            'geners':forms.TextInput(attrs={'class':'form-control'}),
            'poster':forms.FileInput(attrs={'class':'form-control'}),
            'actors':forms.TextInput(attrs={'class':'form-control'}),
            'run_time':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'writers':forms.TextInput(attrs={'class':'form-control'}),
            'language':forms.TextInput(attrs={'class':'form-control'}),
        }


        # if there is any mismatch in attribute model will raise error 


        
