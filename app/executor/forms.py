from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


initial_code = \
"""print(1)
print([i for i in range(10)])
a, b = map(int, input().split())
print(a, b, a + b)
exec('print(123)')
import os
print(os.listdir("."))
"""

initial_inp = "100 10"

class UserForm(forms.Form):
    code_console = forms.CharField(label="Code console", widget=forms.Textarea(
        attrs={'class': 'console-input', 'placeholder': "Input...",
               'cols': 5, 'rows': 1
               }), required=False, initial=initial_inp)

    user_code = forms.CharField(label="Insert your code",
                                widget=forms.Textarea(
                                    attrs={'id': "code-container-hidden",
                                           'hidden': True}), initial=initial_code)

    timeout = forms.CharField(label="Timout", widget=forms.Textarea(
        attrs={'placeholder': "Timeout", 'cols': 5, 'rows': 1}),
                              required=False)
