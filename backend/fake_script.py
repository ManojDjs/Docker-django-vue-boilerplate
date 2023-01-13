# assigning env variables from django project
import sys
import os
import pandas as pd
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Setting up django configurations
import django
django.setup()

# python libraries for creating fake data
import random
from faker import Faker

# django app models for which data has to be populated
from Aggregator.models import Course,Sites


k=pd.read_csv('data.csv')
k=k[['course_name', 'course url','course image','course description']]
print(k.dtypes)

# for index, row in k.iterrows():
#     print(row['course_name'], row['course url'])
# Initializing fake generator
fakegen = Faker()

def create_entities(N=10):
    '''
    Populate multiple entities here
    '''
    # get lists of all users in django db 
    # NOTE : Make sure at least one user exists, superuser will also work
    Category_s=['Accouting','Computers','Business Management','Medecine','Cloud','Networking','Personality Management']
    site_name=['Byjus','Edex','Open Learn','Coursera','Online learn','I tutor','Learn Easy']
    course_Name=['Python',"Java","C++","R","Selenium","Testing","C",".Net","Medical coding","Machine Learning"]
    # creating N entries
    for index, row in k.iterrows():

        Name=row['course_name']
        Category=random.choice(Category_s)
        Description=row['course description']
        slug = row['course url']
        # image = row['course image']
        price=random.randrange(100,500)
        c=Course.objects.create(Name=Name,Category=Category,Description=Description,slug=slug,price=price)
        for i in site_name:
                Course_Name=c
                Site=i
                Price=price+random.randrange(100,500)
                Site_URL=fakegen.domain_name()
                Features=fakegen.text()
                Sites.objects.create(Course_Name=Course_Name,Site=Site,Price=Price,Site_URL=Site_URL,Features=Features)
        print(index, "is done")
    # finished
    print("Finished...{} entries populated.".format(N))

if __name__ == "__main__":
    
    # Verify the number of command line arguments
    print("Initializing... checking syntax...")

    try:
        if len(sys.argv) == 2:
            N = int(sys.argv[1])
            print("Found parameter N = {}".format(N))
            # calling method for data population
            create_entities(N)
        else:
            print("No additional parameter provided, populating default no. of entries.")
            create_entities()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Exception occurred at line : {}! {}".format(exc_tb.tb_lineno, e))
        sys.exit(1)