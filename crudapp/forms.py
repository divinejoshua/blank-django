from django import forms

from .models import NameList 


class CreateNameListForm(forms.ModelForm):

	class Meta:
		model = NameList
		fields = ['name']