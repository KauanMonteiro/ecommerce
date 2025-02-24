from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile

class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}), 
        required=False
    )

    class Meta:
        model = Profile
        fields = ('phone',)

class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = '''
            <ul class="form-text text-muted small">
                <li>Sua senha não pode ser muito similar a outras informações pessoais.</li>
                <li>Sua senha precisa conter pelo menos 8 caracteres.</li>
                <li>Sua senha não pode ser uma senha comum.</li>
                <li>Sua senha não pode ser inteiramente numérica.</li>
            </ul>
        '''

        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar Senha'
        })
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = '''
            <span class="form-text text-muted">
                <small>Digite a mesma senha para verificação.</small>
            </span>
        '''

class UpdateUserForm(UserChangeForm):
    password = None
    email = forms.EmailField(
        label="", 
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}), 
        required=False
    )
    first_name = forms.CharField(
        label="", 
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'nome'}), 
        required=False
    )
    last_name = forms.CharField(
        label="", 
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'sobrenome'}), 
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nome de Usuário'
        })
        self.fields['username'].label = ''
        self.fields['username'].help_text = '''
            <span class="form-text text-muted">
                <small>Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.</small>
            </span>
        '''

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="", 
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'})
    )
    first_name = forms.CharField(
        label="", 
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'})
    )
    last_name = forms.CharField(
        label="", 
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sobrenome'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nome de Usuário'
        })
        self.fields['username'].label = ''
        self.fields['username'].help_text = '''
            <span class="form-text text-muted">
                <small>Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.</small>
            </span>
        '''

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Senha'
        })
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '''
            <ul class="form-text text-muted small">
                <li>Sua senha não pode ser muito similar a outras informações pessoais.</li>
                <li>Sua senha precisa conter pelo menos 8 caracteres.</li>
                <li>Sua senha não pode ser uma senha comum.</li>
                <li>Sua senha não pode ser inteiramente numérica.</li>
            </ul>
        '''

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar Senha'
        })
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '''
            <span class="form-text text-muted">
                <small>Digite a mesma senha para verificação.</small>
            </span>
        '''