from django import forms 
from entertainment.models import articlesModel

class myForm(forms.ModelForm):
	class Meta:
		model = articlesModel
		fields = ['title','content','category','image']