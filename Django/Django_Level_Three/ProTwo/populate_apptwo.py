import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):        

        # create the fake data for that entry
        fake_fname = fakegen.first_name_nonbinary()
        fake_lname = fakegen.last_name()
        fake_emailid = fakegen.email()

        # create the new user entry
        webpg = User.objects.get_or_create(emailid=fake_emailid,first_name=fake_fname, 
                                           last_name=fake_lname)[0]
                                           


if __name__ == '__main__':
    print("Populating script!")
    populate(20) # Number of entries
    print("Populating complete!")