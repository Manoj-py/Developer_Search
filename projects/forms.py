from dataclasses import field
from pyexpat import model
from django.forms import CheckboxSelectMultiple, ModelForm,widgets
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','descripition','demo_link','source_link','tags','featured_image']
        widgets = {
            'tags': CheckboxSelectMultiple(),
        }
    def __init__(self, *args,**kwargs):
        super(ProjectForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input',})

    