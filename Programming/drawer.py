import matplotlib as mpl
import matplotlib.pyplot as plt

# ПЕРВЫЙ ГРАФИК

fig, ax = plt.subplots()
xes = []
yes = []
with open("data/launch.txt", "r", encoding="UTF-8") as f:
    for line in f.readlines():
        (x, y) = tuple(map(float, line.split()))
        xes.append(x)
        yes.append(y)
ax.plot(xes, yes, label="ksp")

xes = []
yes = []
with open("data/launch_mod.txt", 'r', encoding="UTF-8") as f:
    for line in f.readlines():
        (x, y) = tuple(map(float, line.split()))
        xes.append(x)
        yes.append(y)
ax.plot(xes, yes, label="model")
ax.set_xlabel("Время, с")
ax.set_ylabel("Скорость, м/с")
ax.set_title("Запуск, выход на орбиту Кербина")
ax.legend()
ax.grid(True)
plt.show()

# ВТОРОЙ ГРАФИК

fig2, ax2 = plt.subplots()
xes = []
yes = []
with open("data/obt_tr.txt", "r", encoding="UTF-8") as f:
    for line in f.readlines():
        (x, y) = tuple(map(float, line.split()))
        xes.append(x)
        yes.append(y)
ax2.plot(xes, yes, label="ksp")
xes = []
yes = []

with open("data/obt_tr_mod.txt", 'r', encoding="UTF-8") as f:
    for line in f.readlines():
        (x, y) = tuple(map(float, line.split()))
        xes.append(x)
        yes.append(y)
ax2.plot(xes, yes, label="model")
ax2.set_xlabel("Время, ч")
ax2.set_ylabel("Скорость, м/с")
ax2.set_title("Гелиоцентрический участок полёта")
ax2.legend()
ax2.grid(True)
plt.show()

# ТРЕТИЙ ГРАФИК

fig3, ax3 = plt.subplots()
xes = []
yes = []
with open("data/eve_obt.txt", "r", encoding="UTF-8") as f:
    for line in f.readlines():
        (x, y) = tuple(map(float, line.split()))
        xes.append(x)
        yes.append(y)
ax3.plot(xes, yes, label="ksp")
xes = []
yes = []
with open("data/eve_mod.txt", 'r', encoding="UTF-8") as f:
    for line in f.readlines():
        (x, y) = tuple(map(float, line.split()))
        xes.append(x)
        yes.append(y)
ax3.plot(xes, yes, label="model")
ax3.set_xlabel("Время, с")
ax3.set_ylabel("Скорость, м/с")
ax3.set_title("Торможение в SOI Евы, посадка")
ax3.legend()
ax3.grid(True)
plt.show()
