# graphAlgorithms.py
# -------
# This file contains graph algorithms which are used in the code


# this function implements the kruskal algorithm for
# finding the lenght of minimum spanning tree.

import heapq

def lenghtMST(points):
	edges = edgesBetweenPoints(points)
	heapq.heapify(edges)
	visited = []
	length = 0
	while len(visited) != len(points) and len(edges):
		distance,  point1, point2 =  heapq.heappop(edges)
		if point1 in visited and point2 in visited:
			continue
		else:
			length = length + distance
			if point1 not in visited:
				visited.append(point1)
			if point2 not in visited:
				visited.append(point2)
	return length


def manhattanDistance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def edgesBetweenPoints(points):
	edges = []
	for x,y in points:
		for a,b in points:
			if x is not a or y is not b:
				edges.append( ( manhattanDistance((x,y), (a,b)), (x,y), (a,b) ) )
	return edges

