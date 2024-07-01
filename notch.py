import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import iirnotch, filtfilt

fs = 100000
f0 = 2000
Q = 30

b, a = iirnotch(f0, Q, fs)

df = pd.read_csv('F0001CH2.csv')

time = df['time(s)']
Vin = df['Vin']
Vout = df['Vout']

Vout_filtered = filtfilt(b, a, Vin)

plt.figure(figsize=(12, 10))
plt.xlabel("time(s)")
plt.ylabel("Vin")
plt.subplot(3, 1, 1)
plt.plot(time, Vin, label='Vin')
plt.plot(time, Vout, label='Vout', c = "red")
plt.plot(time, Vout_filtered, label='Vout_filtered', c = "green")
plt.show()