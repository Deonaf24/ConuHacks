import pickle

filename = "save.p"

with open(filename, 'rb') as file:
    data = pickle.load(file)

def getCoordinates(city):
    lat = data[city][0]
    long = data[city][1]
    return (lat, long)

print(getCoordinates('Paris'))

#
