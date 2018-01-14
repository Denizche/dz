from loginsys.models import *
from django import forms



class ImageForm(forms.Form):
    workers = forms.ModelChoiceField(queryset=User.objects.all())
    def label_from_instance(self, obj):
        return self.workers.__str__()


class UserServiceForm(forms.ModelForm):
    class Meta:
        model = UserService
        fields = ["user", "service", "description", "desc_picture"]


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["id", "title", "price", "picture"]