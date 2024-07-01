import math
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

x = [10, 100, 300, 362, 500, 800, 1000, 1200, 1500, 1800, 2000]
y = [1, 0.980, 0.800, 0.740, 0.630, 0.470, 0.380, 0.330, 0.280, 0.230, 0.220]
y2 = [1, 0.964, 0.770, 0.707, 0.586, 0.412, 0.340, 0.289, 0.234, 0.197, 0.178]
Y = []
Y2 = []
for i in y:
    Y.append(20*abs(math.log10(i)))
for i in y2:
    Y2.append(20*abs(math.log10(i)))
fig = plt.figure(figsize=(8, 6))
plt.scatter(x, Y)
plt.plot(x, Y)
plt.plot(x, Y2, linestyle="dashed", c = "orange")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Frequency", fontsize=20)
plt.ylabel("HdB", fontsize=20)
plt.title("LPF의 주파수응답특성 - 크기", fontsize=25)
plt.show()
