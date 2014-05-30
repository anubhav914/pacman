# graphAlgorithms.py
# -------
# This file contains graph algorithms which are used in the code


# this function implements the kruskal algorithm for
# finding the lenght of minimum spanning tree.

import itertools

def lengthMST(points):
	return sum( [ weight for weight,p1,p2 in MST(points) ] )


def manhattanDistance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def euclideanDistance(point1, point2):
	return ( (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 ) ** 0.5

def getEdges(points):
	makeEdge = lambda x,y : ( (euclideanDistance(x, y), x, y) )
	edges = [  makeEdge(p1,p2) for p1 in  points for p2 in points if p1 < p2 ]
	return edges

def MST(points):
	# this function implements the kruskal algorithm for
	# finding the lenght of minimum spanning tree.
	S = []
	parents, ranks  = makeSet(points)
	edges  = getEdges(points)
	edges.sort()
	for edge in edges:
		weight, p1, p2 = edge
		if findSet(parents, p1) != findSet(parents, p2):
			S.append(edge)
			unioun(parents, ranks, p1, p2)
	return S

def makeSet(points):
	parents,ranks = dict(), dict()
	for point in points:
		parents[point] = point
		ranks[point] = 0
	return ( (parents, ranks) )

def unioun(parents, ranks, p1, p2):
	p1Root,p2Root = findSet(parents, p1), findSet(parents, p2)
	if ranks[p1Root] < ranks[p2Root]:
		return unioun(parents, ranks, p2Root, p1Root)
	parents[p2Root] = p1Root
	if p1Root != p2Root and ranks[p1Root] == ranks[p2Root]:
		ranks[p1Root] = ranks[p1Root] + 1

def findSet(parents, point):
	if parents[point] == point:
		return point
	return findSet(parents, parents[point])
	