import matplotlib.pyplot as plt
import random

def tinkerbellMap(n):
    xValues = [0]*n
    yValues = [0]*n

    xValues[0] = -0.7
    yValues[0] = -0.6
    for i in range(1, n):
        xPrevious = xValues[i-1]
        yPrevious = yValues[i-1]

        print(i)
        xValues[i] = pow(xPrevious, 2) - pow(yPrevious, 2) + (0.9 * xPrevious) - (0.6 * yPrevious)
        yValues[i] = (2 * xPrevious * yPrevious) + (2 * xPrevious) + (0.5 * yPrevious)
 
    plt.plot(xValues, yValues, 'k,')
    plt.suptitle("Tinkerbell map")
    plt.show()
