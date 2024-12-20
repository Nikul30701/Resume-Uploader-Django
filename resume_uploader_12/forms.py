from django import forms

from .models import Resume

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', "Female"),
    ('other', 'Others')
)

SKILLS = (
    ('py','Python'),
    ('js', 'JavaScript'),
    ('html','Html'),
    ('css','CSS'),
    ('c', 'C++'),
    ('java','JAVA')
)

class ResumeForms(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    skill = forms.MultipleChoiceField(choices=SKILLS, label="Job Skills", widget=forms.CheckboxSelectMultiple)

    class Meta:
        models = Resume
        fields = ['name','email','github','skill',
                  'role','city','state','image','documents']

        labels = {'name':'Name', "email":"Email", 'github':"GitHub",
                  'skill':'Skill','role':"Role", 'city':'City',
                  'state':'State', 'image':'Profile Image','documents':"Documents"}

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'github': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

