from django import forms


class UserForm(forms.Form):
    code_console = forms.CharField(label="Code console", widget=forms.Textarea(
        attrs={'class': 'console-input', 'placeholder': "Input...",
               'cols': 5, 'rows': 1
               }),
                                   required=False)

    user_code = forms.CharField(label="Insert your code",
                                widget=forms.Textarea(
                                    attrs={'id': "code-container-hidden",
                                           'hidden': True}))

    stopped = forms.BooleanField(required=False)
