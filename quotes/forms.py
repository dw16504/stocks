from django import forms
from .models import watchListItem

class watchListForm(forms.ModelForm):
	class Meta:
		model = watchListItem
		fields = ["symbol"]