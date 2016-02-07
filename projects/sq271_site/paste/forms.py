import hashlib
from django import forms
from paste.models import Paste

class PasteForm(forms.ModelForm):
    title = forms.CharField(max_length=64, required=False, widget=forms.TextInput(attrs={'placeholder':'Title'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Paste','rows':20, 'cols':60}))
    hash = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Paste
        fields = ('title','body')

    def save(self):
        instance = super(PasteForm, self).save(commit=False)
        mash = hashlib.md5(instance.body.encode('utf-8')).hexdigest()[:8]
        instance.hash = mash
        instance.save()
        return mash
