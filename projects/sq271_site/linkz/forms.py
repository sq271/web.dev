import hashlib
from django import forms
from linkz.models import Linkz

class LinkzForm(forms.ModelForm):
    title = forms.CharField(max_length=64, help_text='Title', required=False)
    owner = forms.CharField(max_length=32, help_text='Name', required=False)
    body = forms.CharField(help_text='Paste', required=False,
                widget=forms.Textarea(attrs={'rows':20, 'cols':80}))
    hash = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Linkz
        fields = ('title','owner','body')

    def save(self):
        instance = super(LinkzForm, self).save(commit=False)
        mash = hashlib.md5(instance.body.encode('utf-8')).hexdigest()[:8]
        instance.hash = mash
        instance.save()
        return mash
