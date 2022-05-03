import random
import time
import sys

distanceList = []

def calcDistance(nodes):
    arraySize = len(nodes)
    sum=0
    for x in range(arraySize-1):
         sum += distanceList[nodes[x]['id']][nodes[x+1]['id']]
    sum += distanceList[nodes[arraySize-1]['id']][nodes[0]['id']]
    return sum

def two_opt(nodes):
    #fucntion
    newList=[]
    reversedList=[]
    arraySize = len(nodes)
    broken = False
    for i in range(arraySize):
        for j in range(arraySize):
            if (i<j):
                newList = nodes.copy()
                for k in range(i,j):
                    newList[k]=nodes[j+i-k-1]
                if (calcDistance(newList)<calcDistance(nodes)):
                    broken = True
                    break
        if (broken):
            break
    if(broken):
        #recursion
        return two_opt(newList)
    else:
        return nodes

def opt(nodes, distances,cutoff,seed):
    sys.setrecursionlimit(10000)
    global distanceList
    distanceList = distances.copy()
    path = []
    trace = {}
    quality = 0
    start_time = time.time()  
    random.seed(seed)
    random.shuffle(nodes)
    nodes = two_opt(nodes)
    quality = calcDistance(nodes)
    trace.update({round(time.time() - start_time, 2): quality})
    while (time.time() - start_time) < cutoff:
        random.seed(seed)
        random.shuffle(nodes)
        nodes = two_opt(nodes)
        if calcDistance(nodes)<quality:
            quality = calcDistance(nodes)
            trace.update({round(time.time() - start_time, 2): quality})
    for x in nodes:
        path.append(x["id"])
    print(trace)
    return quality, path, trace