import csv
import googlemaps

master = []
lines = []
count = 0;
with open('centralBankData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        lineFILE = [row[2]]
        lineFILE.append(row[3])
        lineFILE.append([x.strip() + " " for x in row[:2]])
        master.append(lineFILE)
csvfile.close()
print(master)
gmaps = googlemaps.Client(key="AIzaSyCXO2FQu10Ru7KANRnVLcCJsVCmH5L33fM")

csvLines = []
for y in master:
    x = y[2]
    line = [y[0],y[1]]
    geocode_result = gmaps.geocode(x[0].strip()+ " " + x[1].strip("' "))
    # Geocoding an address
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    line.append([lat, lng])
    print(line)
    csvLines.append(line)


file1 = open("Newcode.txt", "w")
file1.writelines(["new google.maps.LatLng("+x[1]+", "+x[2]+"),\n" for x in master])
file1.close()

'''
new
google.maps.LatLng(37.783100, -122.441461),'''