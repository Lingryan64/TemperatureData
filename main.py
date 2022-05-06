from pandas import *
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
# reading csv file here
data = read_csv("TempData.csv")

# converting column data to a list
temperature = data['temperature'].tolist()
humidity = data['humidity'].tolist()
time = data['packetTimeStamp'].tolist()
# reversing lists because [0] is the last record
temperature.reverse()
humidity.reverse()
time.reverse()

# using 1 because reverse function seems to have put a ' ' at index 0
startStamp = time[1]
# -2 because of way temperature is saved in csv from Proteus
endStamp = time[int(len(time)) -2]

minutes = list(range(1, len(time) + 1))

plt.plot(minutes,temperature, 'g', label="Temperature")
plt.title('TLSSNJ IT Closet Temperature')
plt.ylabel("Temperature")
plt.xlabel("Minutes")
plt.xlabel(startStamp + " -----> " + endStamp)
plt.gca().invert_yaxis()
plt.show()

plt.plot(minutes,humidity, 'r', label="Humidity")
plt.title('TLSSNJ IT Closet humidity')
plt.ylabel("Humidity")
plt.xlabel("Minutes")
plt.xlabel(startStamp + " -----> " + endStamp)
plt.show()