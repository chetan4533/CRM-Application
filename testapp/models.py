from django.db import models



class CRM(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    # auto_now_add --->  when we create new record django will put that time stamp on there
    no = models.IntegerField(default = True)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 40)
    phone = models.CharField(max_length = 40)
    address = models.CharField(max_length = 40)
    zipcode = models.CharField(max_length = 40)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")

