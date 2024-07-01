import math
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

x = [10, 100, 300, 362, 500, 800, 1000, 1200, 1500, 1800, 2000]
y = [0,15.8,41.0,48.2,57.6,73.7,82.1,81.2,95.0,98.5,104]
y2 = [1.58, 15.5, 39.7, 45, 54.1, 65.7, 70.1, 73.2, 76.4, 78.6, 79.7]
fig = plt.figure(figsize=(8, 6))
plt.scatter(x, y)
plt.plot(x, y)
plt.plot(x, y2, linestyle="dashed", c = "orange")
plt.xscale('log')
plt.xlabel("Frequency", fontsize=20)
plt.ylabel("HdB", fontsize=20)
plt.title("LPF의 주파수응답특성 - 위상", fontsize=25)
plt.show()
