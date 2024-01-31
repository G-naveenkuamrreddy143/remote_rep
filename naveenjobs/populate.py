import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'naveenjobs.settings')
import django
django.setup()

from faker import Faker
from random import *
from testapp.models import HydJobs
fake=Faker()
def phonumber():
    d1=randint(6,9)
    num=str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Team Lead','Software Engineer','System Analyst','Project Manager'))
        feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA','Phd'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonumber()
        job_recod=HydJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phone_number=fphonenumber)
    print(n,"Records added successfully to the database")
n=int(input("Enter number of records : "))
populate(n)