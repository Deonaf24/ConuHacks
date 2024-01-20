import pandas as pd
import random
import pickle

myFile = '/home/ubuntu/ConuHacks/worldcities.csv'
read = pd.read_csv(myFile)

# Convert the DataFrame to a Dictionary
data_dict = read.to_dict(orient='records')

cities = {}

for i in data_dict:

  if i['city'] in cities.keys():
    if float(i['population']) < cities[i['city']][2]:
      continue

  cities[i['city']] = [float(i['lat']),float(i['lng']), float(i['population']) ]

new_list = list(cities.keys())

random_choice = random.choice(new_list)


print(random_choice)

pickle.dump(cities, open("save.p", "wb"))