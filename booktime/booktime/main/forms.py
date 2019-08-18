from django import forms

class ContactForm(forms.form):
    name = form.CharField(label='Your Name', max_length=100)
    message = form.CharField(max_length=600, widget=forms.Textarea)