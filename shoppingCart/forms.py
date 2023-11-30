from django import forms

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity', 'other_field']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        def clean_quantity(self):
            quantity = self.cleaned_data['quantity']
            if quantity <= 0:
                raise forms.ValidationError("Quantity must be greater than zero.")
            return quantity
