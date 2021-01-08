from django import forms
from .models import setboq


class SetboqForm(forms.ModelForm):

    class Meta:
        model = setboq
        fields=["project","category","material","objecttype","boqdescription","boqcodes","image"]


class GetboqForm(forms.ModelForm):

    class Meta:
        model = setboq
        fields = ["project","category","material","objecttype","schedulein","schtype","project","boqdescription"]



