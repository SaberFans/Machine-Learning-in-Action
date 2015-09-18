# This Python file uses the following encoding: utf-8

'''
Created on Sep 16, 2010

'''

from kNN import *
import matplotlib
import matplotlib.pyplot as plt
import numpy
#from matplotlib import font_manager
from matplotlib import rcParams


def drawPlot1():
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
    plt.show()
    return


def drawPlot2():
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:,1], datingDataMat[:,2],
                    35*numpy.array(datingLabels), 15*numpy.array(datingLabels))
    
    xlabelText = '玩游戏的时间百分比'.decode('utf8')
    ylabelText = '每周吃的冰淇淋升数'.decode('utf8') 
      
    ax.set_xlabel(xlabelText, family='microsoft yahei')
    ax.set_ylabel(ylabelText, family='microsoft yahei')
    plt.show()
    return

def drawPlot3():
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    fig = plt.figure()
   
    ax = fig.add_subplot(111)

    # concatenate the labels and dating Data
    datingLabels = numpy.asarray(datingLabels)
    t_datingLabels = datingLabels[:, numpy.newaxis]
    datingDataMatJoined = numpy.concatenate((datingDataMat, t_datingLabels), axis = 1)

    color = ['red', 'green', 'blue']
    likeV = [u'非常讨厌', u'有好感', u'非常喜欢']

    checker = [False, False, False]
    # for color, x, y in zip(datingLabels, datingDataMat[:,0], datingLabels[:,1]):  
    for x, y, cvalue in  zip(datingDataMatJoined[:,0], datingDataMatJoined[:,1], datingDataMatJoined[:, 3]):
        
        if not checker[int(cvalue)-1] :
            plt.scatter(x, y, c=color[int(cvalue)-1], s= cvalue*15, label = likeV[int(cvalue)-1] )
            checker[int(cvalue)-1] = True
        else :
            plt.scatter(x, y, c=color[int(cvalue)-1], s= cvalue*15)

    #fontP = font_manager.FontProperties()     
    #fontP.set_family('microsoft yahei')
    rcParams['font.family'] = 'microsoft yahei'
    xlabelText = '每年航班飞行里程'.decode('utf8')
    ylabelText = '玩游戏的时间百分比'.decode('utf8') 

    plt.legend()  
    plt.grid(True)
    

    ax.set_xlabel(xlabelText, family='microsoft yahei')
    ax.set_ylabel(ylabelText, family='microsoft yahei')
    ax.set_title(u'妹子喜欢你吗，三叔？', family='microsoft yahei')
    
    plt.show()
    return   
