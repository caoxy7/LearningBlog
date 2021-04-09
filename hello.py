import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import random

def readFile(filename):
    np.set_printoptions(suppress=True)
    rfile = open(filename)
    array4Lines = rfile.readlines()
    linesNum = len(array4Lines)
    matrix = np.zeros((linesNum, 3))
    index = 0
    for line in array4Lines:
        line = line.strip()             # delete \n
        listFromLine = line.split(' ')  # split space
        matrix[index, :] = listFromLine[0:3]
        index += 1
    return matrix

def s_gradient_decent():
    alpha = 0.00015 # learn rate
    # init
    theta0 = 0.0
    theta1 = 0.0
    theta2 = 0.0
    trainMat = readFile('./doc/dataForTrainingLinear.txt')
    testMat = readFile('./doc/dataForTestingLinear.txt')

    resTable = PrettyTable(["number of iterations", "theta0", "theta1", "theta2", "training_error", "testing_error"])

    training_errors = []
    iter_times = []
    testing_errors = []
    m = len(trainMat)
    n = len(testMat)
    count = 1

    for j in range(1500000):
        index = random.randint(0, m-1)
        hx = theta0 + theta1 * trainMat[index][0] + theta2 * trainMat[index][1]
        # one sample to refresh theta
        theta0 = theta0 - alpha * (hx - trainMat[index][2]) * 1
        theta1 = theta1 - alpha * (hx - trainMat[index][2]) * trainMat[index][0]
        theta2 = theta2 - alpha * (hx - trainMat[index][2]) * trainMat[index][1]

        if j % 99999 == 0 and j >= 99999:
            iter_times.append(j + count)
            tmp = 0
            test_tmp = 0

            for i in range(m):
                Hx = theta0 + theta1 * trainMat[i][0] + theta2 * trainMat[i][1]
                # tmp += np.abs(Hx-trainMat[i][2])
                tmp += np.square(Hx-trainMat[i][2])
                # Hx = theta0 + theta1 * trainMat[i][0] + theta2 * trainMat[i][1] - trainMat[i][2]
                # tmp += np.abs(Hx)/np.sqrt(np.square(theta2)+np.square(theta1)+1)
            trainError = (1.0/m) * tmp
            training_errors.append(trainError)

            for k in range(n):
                Hx = theta0 + theta1 * testMat[k][0] + theta2 * testMat[k][1]
                # test_tmp += np.abs(Hx-testMat[k][2])
                test_tmp += np.square(Hx - testMat[k][2])
                # Hx = theta0 + theta1 * testMat[k][0] + theta2 * testMat[k][1] - testMat[k][2]
                # test_tmp += np.abs(Hx)/np.sqrt(np.square(theta2)+np.square(theta1)+1)
            testError = (1.0/n) * test_tmp
            testing_errors.append(testError)

            resTable.add_row([j + count, theta0, theta1, theta2, trainError, testError])
            count += 1

    print(resTable)
    plt.figure()
    plt.plot(iter_times, training_errors, '*-', c = "r", linewidth=1, label="training error")
    plt.plot(iter_times, testing_errors, '+-', c = "b", linewidth=1, label="testing error")

    plt.xlabel("iteration times")
    plt.ylabel("error")
    plt.legend()
    plt.title("Stochastic Gradient Descent")  
    plt.show() 

def gradient_decent():
    alpha = 0.00015 # learn rate
    # init
    theta0 = 0.0
    theta1 = 0.0
    theta2 = 0.0
    trainMat = readFile('./doc/dataForTrainingLinear.txt')
    testMat = readFile('./doc/dataForTestingLinear.txt')

    resTable = PrettyTable(["number of iterations", "theta0", "theta1", "theta2", "training_error", "testing_error"])

    training_errors = []
    iter_times = []
    testing_errors = []
    m = len(trainMat)
    n = len(testMat)
    count = 1

    for j in range(1500000):
        sum0 = 0
        sum1 = 0
        sum2 = 0
        for index in range(m):
            hx = theta0 + theta1 * trainMat[index][0] + theta2 * trainMat[index][1]
            sum0 += (hx - trainMat[index][2])
            sum1 += (hx - trainMat[index][2]) * trainMat[index][0]
            sum2 += (hx - trainMat[index][2]) * trainMat[index][1] 

        theta0 = theta0 - alpha * sum0 / m
        theta1 = theta1 - alpha * sum1 / m
        theta2 = theta2 - alpha * sum2 / m

        if j % 99999 == 0 and j >= 99999:
            print(count)
            iter_times.append(j + count)
            tmp = 0
            test_tmp = 0

            for i in range(m):
                Hx = theta0 + theta1 * trainMat[i][0] + theta2 * trainMat[i][1]
                # tmp += np.abs(Hx-trainMat[i][2])
                tmp += np.square(Hx-trainMat[i][2])
                # Hx = theta0 + theta1 * trainMat[i][0] + theta2 * trainMat[i][1] - trainMat[i][2]
                # tmp += np.abs(Hx)/np.sqrt(np.square(theta2)+np.square(theta1)+1)
            trainError = (1.0/m) * tmp
            training_errors.append(trainError)

            for k in range(n):
                Hx = theta0 + theta1 * testMat[k][0] + theta2 * testMat[k][1]
                # test_tmp += np.abs(Hx-testMat[k][2])
                test_tmp += np.square(Hx - testMat[k][2])
                # Hx = theta0 + theta1 * testMat[k][0] + theta2 * testMat[k][1] - testMat[k][2]
                # test_tmp += np.abs(Hx)/np.sqrt(np.square(theta2)+np.square(theta1)+1)
            testError = (1.0/n) * test_tmp
            testing_errors.append(testError)

            resTable.add_row([j + count, theta0, theta1, theta2, trainError, testError])
            count += 1

    print(resTable)
    plt.figure()
    plt.plot(iter_times, training_errors, '*-', c = "r", linewidth=1, label="training error")
    plt.plot(iter_times, testing_errors, '+-', c = "b", linewidth=1, label="testing error")

    plt.xlabel("iteration times")
    plt.ylabel("error")
    plt.legend()
    plt.title("Stochastic Gradient Descent")  
    plt.show() 

gradient_decent()
# s_gradient_decent()