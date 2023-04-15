import matplotlib.pyplot as plt
import random

def barnsleyFern(n):
    xValues = [0]*n
    yValues = [0]*n

    xValues[0] = 0
    yValues[0] = 0
    for i in range(1, n):
        xPrevious = xValues[i-1]
        yPrevious = yValues[i-1]

        print(i)
        probability = random.randint(0, 100)
        if probability in range(0, 86):
            xValues[i] = (0.85 * xPrevious) + (0.04 * yPrevious)
            yValues[i] = (-0.04 * xPrevious) + (0.85 * yPrevious) + 1.6
        elif probability in range(86, 93):
            xValues[i] = (0.2 * xPrevious) - (0.26 * yPrevious)
            yValues[i] = (0.23 * xPrevious) + (0.22 * yPrevious) + 1.6
        elif probability in range(93, 100):
            xValues[i] = (-0.15 * xPrevious) + (0.28 * yPrevious) - 0.28
            yValues[i] =(0.26 * xPrevious) + (0.24 * yPrevious) + 1.05
        else:
            xValues[i] = 0
            yValues[i] = 0.16 * yPrevious

    plt.plot(xValues, yValues, 'k,')
    plt.suptitle("Barnsley fern")
    plt.show()

