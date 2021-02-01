from django import forms
from .models import WebsiteModel

class ModelFormWithSubmit(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', "Valider", css_class="btn btn-lg btn-primary btn-block bg_main"))
    helper.form_method = 'POST'

class UrlForm(ModelFormWithSubmit):

    class Meta:
        model = WebsiteModel
        fields = ('name','website',)