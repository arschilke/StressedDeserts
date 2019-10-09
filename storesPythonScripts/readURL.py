import csv
import googlemaps
import time
from bs4 import BeautifulSoup

import requests
master = []
urls = []

with open('convertcsv.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='|')
    for row in readCSV:
        #print(row)
        NameSplit = row[0].split("|");
        url = NameSplit[0]
        urls.append(url.strip())
        name = NameSplit[1].strip()
        num = row[1].strip()
        states = [x.strip() for x in row[2:]]
        brand = [url, name, num, states]
        master.append(brand)


    #  for x in range(len(states)):
     #       print(states[x])
for url in urls:
    locations = []
    if url == "URL":
        master[0].append(['locations'])
        continue
    else:
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        for table in soup.find_all('table'):
            for row in table.findAll("tr"):
                location = []
                cells = row.findAll("td")
                if cells[0].string == "Store #":
                    locations.append([''])
                    continue
                for cell in cells:
                    if cells.index(cell) == 0:
                        continue
                    location.append(cell.string)
                locations.append(location)
        master[urls.index(url)].append(locations)


arr = []
counter = 0;
for x in master:
    counter += 1
    arr.append(len(x[4]))


print(sum(arr))
print(len(master))

gmaps = googlemaps.Client(key="INSERT KEY HERE")

csvLines = []
for brand in master:
    for store in brand[4]:
        line = [brand[1]]
        address = ""
        if store == "locations" or store == ['']:
            continue
        for x in store[:2]:
            address += " " + x
        try:
            geocode_result = gmaps.geocode(address)
        # Geocoding an address
            lat = geocode_result[0]['geometry']['location']['lat']
            lng = geocode_result[0]['geometry']['location']['lng']
            line.append([lat, lng])
            csvLines.append(line)
        except IndexError:
            print(brand[1]+ " " + str(brand[4].index(store)))


with open('stores.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(csvLines)

writeFile.close()
