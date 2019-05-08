import numpy as np
import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
from numpy import genfromtxt

def draw_result():

    r1 = np.load("1.npy")
    r2 = np.load("sharpe.npy")
    r3 = np.load("sortino.npy")
    r4 = np.load("sterling.npy")
    r5 = np.load("all.npy")

    plt.clf()
    plt.plot(np.arange(1, len(r1)+1), r1, label='all buy')
    plt.plot(np.arange(1, len(r2)+1), r2, label='sharpe')
    plt.plot(np.arange(1, len(r3)+1), r3, label='sortino')
    plt.plot(np.arange(1, len(r4)+1), r4, label='sterling')
    plt.plot(np.arange(1, len(r5)+1), r5, label='ensemble')

    plt.xlabel('Days')
    plt.ylabel('Total Asset')
    plt.legend(bbox_to_anchor=(0.36, 1), loc=1)
    plt.savefig('result.png')

def draw_ana():
    
    X = genfromtxt('SPY.csv', delimiter=',')[1:, 1:]
    r1 = X[:, 0]
    r2 = X[:, 1]
    r3 = X[:, 2]
    r4 = X[:, 3]
    r5 = X[:, 4]-X[:, 3]+X[:, 0]
    r6 = X[:, 4]

    plt.clf()
    plt.plot(np.arange(1, len(r1)+1), r1, label='Open')
    plt.plot(np.arange(1, len(r2)+1), r2, label='High')
    plt.plot(np.arange(1, len(r3)+1), r3, label='Low')
    plt.plot(np.arange(1, len(r4)+1), r4, label='Close')
    plt.plot(np.arange(1, len(r5)+1), r5, label='AdjOpen')
    plt.plot(np.arange(1, len(r6)+1), r6, label='AdjClose')

    plt.xlabel('Days')
    plt.ylabel('Value')
    plt.legend(bbox_to_anchor=(0.36, 1), loc=1)
    plt.savefig('ana.png')

if __name__ == '__main__':
    draw_result()
    draw_ana()

