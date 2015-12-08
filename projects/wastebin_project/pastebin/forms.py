import hashlib
from django import forms
from pastebin.models import Paste

class PasteForm(forms.ModelForm):
    title = forms.CharField(max_length=64, help_text="Title", required=False)
    owner = forms.CharField(max_length=32, required=False, help_text="Name")
    content = forms.CharField(help_text="Paste",
                    widget=forms.Textarea(attrs={"rows":20, "cols": 80}))
    hash = forms.CharField(widget=forms.HiddenInput(), required=False) 
    

    class Meta:
        model = Paste
        fields = ('title', 'owner', 'content')

    def save(self):
        instance = super(PasteForm, self).save(commit=False)
        mash = hashlib.md5(instance.content.encode('utf-8')).hexdigest()[:8]
        instance.hash = mash
        instance.save()
       # return instance
    
