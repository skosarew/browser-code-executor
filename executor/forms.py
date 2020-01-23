from django import forms


class UserForm(forms.Form):
    def clean_code_result(self):
        new1 = self.cleaned_data['code_result'] + '333'
        print('clean_code_result: ', new1)
        return new1

    def clean_user_code(self):
        new1 = self.cleaned_data['user_code']
        # print('clean_user_code: ', new1)
        return new1

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
