from django import forms
from Rango.models import Page, Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False, help_text="Please enter the slug")

    class Meta:
        model = Category
        fields = '__all__'


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        clean_data = self.cleaned_data
        url = clean_data.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
            clean_data['url'] = url
        return clean_data

    class Meta:
        model = Page
        exclude = ('category', )
