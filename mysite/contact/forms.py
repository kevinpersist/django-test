from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail address')
    #message = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self): #prefix: clean_ field: message, auto check
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("not enough words!")
        return message
