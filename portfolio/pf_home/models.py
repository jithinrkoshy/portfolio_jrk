from django.db import models

# Create your models here.


class ClientMessage(models.Model):
    name = models.CharField(max_length = 264, blank = True)
    code = models.CharField(max_length = 2,blank = True, default="91")
    phone = models.CharField(max_length = 15,blank = True)
    email = models.EmailField(blank = True)
    message = models.TextField(blank = True)

    def __str__(self):
        return str(self.email)

