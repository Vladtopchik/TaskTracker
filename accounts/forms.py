from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class CustomPasswordWidget(forms.PasswordInput):
    def render(self, name, value, attrs=None, renderer=None):
        input_html = super().render(name, value, attrs, renderer)

        return mark_safe(
            f'{input_html} <button type="button" class="password-visibility"><span '
            'class="material-symbols-outlined">visibility</span></button> ' + (
                f'<span class="warn hidden">This field is required!!!</span> <span class="warn hidden">This password is'
                ' to common, please follow next rules!</span> <span class="warn hidden">Passwords are different!</span>'
                if self.attrs.get('warns') else ''
            )
        )


class CustomUsernameWidget(forms.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        input_html = super().render(name, value, attrs, renderer)

        return mark_safe(
            f'{input_html}'
            f'<span class="warn hidden">This field is required!!!</span>'
        )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget = CustomPasswordWidget(attrs={
            'class': 'password-input',
            'placeholder': 'Enter your password',
            "required": True,
        })

        self.fields['password2'].widget = CustomPasswordWidget(attrs={
            'class': 'password-input',
            'placeholder': 'Enter your password',
            "required": True,
        })


class LabelBooleanField(forms.BooleanField):
    def get_bound_field(self, form, field_name):
        bound_field = super().get_bound_field(form, field_name)

        label = bound_field.label
        original_as_widget = bound_field.as_widget

        bound_field.label = ''

        def custom_as_widget(*args, **kwargs):
            kwargs['attrs'] = kwargs.get('attrs', {})
            rendered_widget = original_as_widget(*args, **kwargs)

            rendered_label = f'<label for="{bound_field.id_for_label}">{label}</label>'
            return mark_safe(f'{rendered_widget} {rendered_label}')

        bound_field.as_widget = custom_as_widget
        return bound_field


class CustomAuthenticationForm(AuthenticationForm):
    remember_me = LabelBooleanField(
        required=False,
        label="Remembers me",
        widget=forms.CheckboxInput(attrs={'class': 'remember'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = CustomPasswordWidget(attrs={
            'class': 'password-input',
            'placeholder': 'Enter your password',
            "required": True,
            'warns': False,
        })
