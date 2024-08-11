from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Логин')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Подтверждение пароля')
    address = forms.CharField(label='Адрес', required=True)


class RegisterLibrian(forms.Form):
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Подтверждение пароля')
    personnel_number = forms.CharField(label='Персональный номер работника', required=True)


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')
