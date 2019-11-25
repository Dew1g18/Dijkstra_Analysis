import numpy
from src import math1058_cwk
from src import graph_methods


def dijkstra1(successors, s):
    S = []
    S.append(s)
    n = len(successors)
    L = dict()
    L[s] = 0    
    P = dict()
    P[s] = '-'

    #WRITE ME
    predesessor = s
    while len(S)<n:
        shortestDistance = numpy.Infinity
        nextNode = s
        # because of the way I have written this if I am given a non traversable graph it may return
        # some infinite distances....
        for i in S:
            for j, length_ij in successors[i].items():
                if L[i]+length_ij<shortestDistance and j not in S:
                    shortestDistance=L[i]+length_ij
                    nextNode=j
                    predesessor = i
        L[nextNode] = shortestDistance
        P[nextNode] = predesessor
       # print (nextNode)
        if nextNode not in S:
            S.append(nextNode)

    return L,P



def dijkstra2(successors, s):

    S = []
    S.append(s)
    n = len(successors)
    L = dict()
    L[s] = 0
    P = dict()
    P[s] = '-'
    unexploredList = []
    #WRITE ME
    for i in range (0, n):
        if (i!=s):
            if (i in successors[s].keys()):
                L[i]=successors[s][i]
            else:
                L[i]=numpy.Infinity
            unexploredList.append(i)
            P[i]=s
    while len(S)<n:
        key,value = minimize(unexploredList, L)
        S.append(key)
        if key in unexploredList:
            unexploredList.remove(key)
        for j in unexploredList:
            if j in successors[key].keys():
                length = L[key]+successors[key].get(j)
                if (length<L[j]):
                    L[j] = L[key]+successors[key].get(j)
                    P[j]= key
    return L,P




def minimize2(explored, all):
    shortest = numpy.Infinity
    node = 0
    for key in all:
        if key not in explored:
            value = all.get(key)
            if value<shortest:
                shortest=value
                node = key
    return node,shortest


def minimize(unexplored, all):
    shortest = numpy.Infinity
    node = 0
    for key in unexplored:
        value = all.get(key)
        if value<shortest:
            shortest=value
            node = key
    return node,shortest


if __name__ == "__main__":
    adj1 = [{1 : 2, 2 : 5},
            {2 : 3},
            {3 : 4},
            {0 : 21, 1 : 8}]

    for o in range(0, 4):
        print(o) 
        print(dijkstra1(adj1, o))
        print(dijkstra2(adj1, o))


    graph_ns, graph_ms, times = math1058_cwk.run_experiments(dijkstra1, 30091055)
    graph_ns, graph_ms, times = math1058_cwk.run_experiments(dijkstra2, 30091055)
