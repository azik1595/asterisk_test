from django import forms

class CallBackForm(forms.Form):
    phone = forms.CharField(max_length=50, help_text=u'Введите номер телефона')