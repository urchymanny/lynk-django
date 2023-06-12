from django import forms
from .models import User, Element


class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    bio = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image',
                  'bio', 'email', 'username', 'password')


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')


class UpdateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    bio = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image',
                  'bio', 'email', 'username', 'password', 'instagram', 'tiktok', 'twitter', 'linkedin')

    def clean(self):
        cleaned_data = super().clean()
        instagram = cleaned_data.get('instagram')
        tiktok = self.cleaned_data['tiktok']
        twitter = self.cleaned_data['twitter']
        linkedin = self.cleaned_data['linkedin']

        def run_cleaner(url, field):
            if url and not url.startswith(('https://', 'http://')):
                cleaned_data[field] = f'https://{url}'

        run_cleaner(instagram, 'instagram')
        run_cleaner(tiktok, 'tiktok')
        run_cleaner(twitter, 'twitter')
        run_cleaner(linkedin, 'linkedin')


class CreateElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ('item_type', 'text_header', 'text_body',
                  'yt_link', 'web_link', 'web_link_header')

    def clean(self):
        cleaned_data = super().clean()
        url = cleaned_data.get('yt_link')
        if url:
            base_url, video_id = url.split("https://youtu.be/")
            cleaned_data['yt_link'] = f"https://youtube.com/embed/{video_id}"


class UpdateElementForm(forms.ModelForm):

    class Meta:
        model = Element
        fields = ('text_header', 'text_body',
                  'yt_link', 'web_link', 'web_link_header')

    def clean(self):
        cleaned_data = super().clean()
        url = cleaned_data.get('yt_link')
        if url:
            base_url, video_id = url.split("https://youtu.be/")
            cleaned_data['yt_link'] = f"https://youtube.com/embed/{video_id}"
