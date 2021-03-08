#Clement 1301180111
import math
import matplotlib.pyplot as plt

gravity = -9.8
velocity = 0
dT = 0.1 #delta T
t = 0
tn = 0
y0 = float(input("height :"))
arr_pos = []
arr_time = []
arr_velo = []
yn = y0
yt = y0

def ffnum(v,y, g, dT, t):
    while y >= 0:
        v = v + (g * dT)
        y = y + (v * dT)
        t += dT
        arr_pos.append(round(y,2))
        arr_time.append(round(t,2))
        arr_velo.append(round(-v,2))
        print("posisi : ",(round(y,2)),"meters;" ,"t: ",(round(t,2)), "s;", "kecepatan: ",(round(-v,2)),"m/s")

ffnum(velocity, y0, gravity, dT, t)

#grafik 
plt.plot(arr_time,arr_pos)
plt.xlabel("Waktu")
plt.ylabel("Posisi dan Kecepatan")
plt.title("Grafik Posisi dan Waktu")

plt.plot(arr_time,arr_velo)
plt.xlabel("Waktu")
plt.ylabel("Kecepatan dan Posisi")
plt.title("Grafik Kecepatan")
plt.legend(["pos","kec"])
plt.show()
