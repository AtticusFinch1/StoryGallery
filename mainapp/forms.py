from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Postman, Publisher

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostmanForm(ModelForm):
    class Meta:
        model = Postman
        fields = '__all__'
        exclude=['user']

    def __init__(self, *args, **kwargs):
        super(PostmanForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control title-name'
        self.fields['phone'].widget.attrs['class'] = 'form-control phone-field'
        self.fields['profile_pic'].widget.attrs['class'] = 'form-control profile_pic-field'
        self.fields['email'].widget.attrs['class'] = 'form-control email-field'

class PublishForm(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        exclude=['postman']
        labels = {
            'publisher_name':'Name of the Author',
            'publisher_title':'Post Title',
            # 'postman': 'Contributor Name'
        }
    def __init__(self, *args, **kwargs):
        super(PublishForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select"
        self.fields['country'].required = False
        self.fields['publisher_name'].widget.attrs['class']='form-control title-field'
        self.fields['publisher_title'].widget.attrs['class']='form-control descr-field'
        self.fields['country'].widget.attrs['class'] = 'form-control country-field'
