from django import forms
from pf_home.models import ClientMessage

class ContactForm(forms.ModelForm):

    class Meta:
        model = ClientMessage
        fields = "__all__"
        widgets={
            "name" : forms.TextInput(attrs={'class':'input-name','name':'name','required':'True'}),
            "code" : forms.TextInput(attrs={'class':'input-code','name':'code','required':'True'}),
            "phone" : forms.TextInput(attrs={'class':'input-phone','name':'phone','required':'True'}),
            "email" : forms.EmailInput(attrs={'class':'input-email','name':'email','required':'True'}),
            "message" : forms.Textarea(attrs={'class':'input-message','name':'message','required':'True'}),
           
        }
