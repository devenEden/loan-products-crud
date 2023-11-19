from django import forms

from loan_products.models import LoanProduct

class LoanProductForm(forms.ModelForm):
    class Meta:
        model = LoanProduct
        fields = "__all__"