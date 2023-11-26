from django.conf import settings
from django.db import models
from django.utils import timezone

#This creates a class named Post that represents a database table using django models.
#The database elements are author(this is a foreign key which means it will link to another table),
#title (a character field with a maximum length of 200), text(a long text field with no character limit),
#created_date (a time field which represents when the date the entry was created),
#and published_date (a time field which represents when the entry was published. this field can be empty.)
#The publish function will set the published_date as the current time.
#The __str__ function will return the Post entry title when called as a string. It also allows the admin page
#to show the Post title for an entry instead of the Post entry primary key.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title