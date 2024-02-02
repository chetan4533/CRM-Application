import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRM.settings')
import django
django.setup()
from faker import Faker
f = Faker()
from random import *
from testapp.models import CRM

def phonenogen():
    r1 = randint(6,9)
    num = ''+str(r1)
    for i in range(9):
        num += str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fno = f.random_int(min=1, max=999)
        ffname = f.first_name()
        flname = f.last_name()
        fphone = phonenogen()
        fmail = f.email()
        fcity = f.city()
        fzip = f.postcode()
        CRM.objects.get_or_create(no = fno, first_name=ffname,last_name=flname,email=fmail,phone=fphone,address=fcity,zipcode=fzip)

n = int(input('enter number of records : '))
populate(n)
print(f"{n} Records inserted successfully...")