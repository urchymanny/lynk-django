from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    image = models.CharField(max_length=1024, blank=True,
                             null=True, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')
    email = models.EmailField(max_length=254, unique=True)
    email_confirmed = models.BooleanField(default=False)
    phone = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=128, blank=True)
    instagram = models.CharField(max_length=250, blank=True)
    tiktok = models.CharField(max_length=250, blank=True)
    twitter = models.CharField(max_length=250, blank=True)
    linkedin = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    objects = models.Manager()


class Element(models.Model):
    ELEMENT_TYPES = [
        ('', 'Select an Element Type'),
        ('text', 'Text Element'),
        ('link', 'Website Link'),
        ('youtube', 'Youtube Video'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=50, choices=ELEMENT_TYPES)
    text_header = models.CharField(max_length=50, blank=True)
    text_body = models.TextField(blank=True, null=True)
    yt_link = models.CharField(max_length=50, blank=True)
    web_link = models.CharField(max_length=50, blank=True)
    web_link_header = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.item_type}'

    objects = models.Manager()
