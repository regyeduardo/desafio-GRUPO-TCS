from django import forms


class Cadastro(forms.Form):
    username = forms.CharField(label='username', max_length=100, required=True)
    senha = forms.CharField(label="senha", max_length=20, required=True)