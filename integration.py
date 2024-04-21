import numpy as np
import scipy
import matplotlib.pyplot as plt


#Функия которую будем итегрировать
def funct(x):
    a = x ** 2
    return a


def integr(x):
    s = 0
    step = 0.1 #Шаг значений х
    j = -10 #Минимальное значение х
    res = []
    for i in x:
            while (j <= i):
                s += funct(j) * step
                j += step
            res.append(s)
    return res


x = np.arange(-10, 10, 0.1) #Промежуток значений х
y = integr(x)#Первообразня функции

plt.plot(x, y)
plt.show()