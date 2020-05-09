from django.db import models
from django.contrib.auth.models import User

USER_TYPE = (
    (1, "Admin"),
    (2 ,"User")
)

class userextender(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    profile_img = models.ImageField(upload_to="",blank=True,null=True)
    phone = models.CharField(max_length=10,blank=True,null=True)
    dob = models.DateField(auto_now=True)
    USER_TYPE = models.IntegerField(choices=USER_TYPE,default=2)
    user_ip = models.GenericIPAddressField()
    user_browser = models.TimeField()


