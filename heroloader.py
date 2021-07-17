import csv
import os 
import django 

os.environ['DJANGO_SETTINGS_MODULE'] = 'marvel.settings'
django.setup()

from hero.models import Hero

heroes = []

with open( 'hero.csv', "rt", encoding="utf-8") as file:
    
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

