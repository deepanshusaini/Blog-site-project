from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete = models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    
    def publish(self):

        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment = True)



    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    

    def __str__(self):
        return self.title
    




class Comments(models.Model):
    post = models.ForeignKey('app_one.post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length =50)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    approved_comment = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse ('post_list')
    
    def __str__(self):
        return self.text
    
    def approve(self):
        self.approved_comment = True
        self.save()












