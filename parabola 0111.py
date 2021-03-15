import numpy as num
import math
import matplotlib.pyplot as plt

x = 0
y = 0
v0 = 20
angle = 60
radian = (angle/360)*(2*3.14)
g = -9.8
t = 0
dt = 0.01

arr_x = []
arr_y = []
arr_t = []

vx = v0*math.cos(radian)
vy = v0*math.sin(radian)

#update dan append array
while (y >= 0):
    vy += (g*dt)
    y += (vy * dt)
    x += (vx * dt)
    t += dt
    if (y < 0):
        break
    arr_x.append(x)
    arr_y.append(y)
    arr_t.append(t)

#solusi numerik
t_total = arr_t[-1]
range = arr_x[-1]
h_max_num = num.max(arr_y)

#solusi analitik
ex_arr_x = [0]
ex_arr_y = [0]
for t in arr_t:
    ex_x = v0 * math.cos(radian) * t
    ex_y = (0.5 * g * t**2) + (v0 * math.sin(radian) * t)
    ex_arr_x.append(ex_x)
    ex_arr_y.append(ex_y)

# total waktu tepat
tot_ex_t = (2 * v0 * math.sin(radian))/-g
# range tepat
ex_range = v0 * math.cos(radian) * tot_ex_t
# h maksimum
max_ex_h = (v0**2 * math.sin(radian)**2) / (-2 * g)

# print hasil
print('numerik dan analitik')
print('total time (s): {:.2f} vs {:.2f}'.format(t_total, tot_ex_t))
print('range (m) {:.2f} vs {:.2f}'.format(range, ex_range))
print('max height (m) {:.2f} vs {:.2f}'.format(h_max_num, max_ex_h))

#grafik
plt.figure()
plt.plot(arr_x, arr_y, c='blue', label='numerik')
plt.plot(ex_arr_x, ex_arr_y, c='pink', label='analitik')
plt.axhline(c='black')
plt.axvline(c='black')
plt.legend()
plt.show()
