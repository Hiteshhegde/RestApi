import csv
import os 
import django 

#Django env settings loader
os.environ['DJANGO_SETTINGS_MODULE'] = 'marvel.settings'
django.setup()
 
#importing hero model
from hero.models import Hero

heroes = []

#Saving to database from csv file
with open( 'hero.csv', "rt", encoding="utf-8") as file:
    
	try:
		reader = csv.reader(file, delimiter=',')
		print("Data loaded successfully...")
		for row in reader:
			print("Grabbing each data")
			hero = Hero(
				name = row[0],
				alias = row[1]
				)
			print("Saving data .....")
			hero.save()
			print("Data saved in database successfully..")
	except:
		print("Failed to save the data to database..")
