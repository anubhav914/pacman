# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
import pdb

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]


def buildPath(parents, state, path):
    """ Returns a list of directions to reach the 
    parents is a dictionary of state and direction
    goal state 
    We build the path going up the tree starting from leaf
    """
    while parents[state] is not None:
      state, direction = parents[state]
      path.append(direction)
    path.reverse()

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    path = []
    """testing git basics"""
    startState, stack  = problem.getStartState(), util.Stack()
    visited = []
    stack.push(startState)
    parents = { startState : None }
    while not stack.isEmpty():
        state = stack.pop()
        visited.append(state)
        if problem.isGoalState(state):
            buildPath(parents,state, path)
            break
        for successorState, direction, cost in problem.getSuccessors(state):
            if successorState not in visited:
                parents[successorState] = (state, direction)
                stack.push(successorState)
    if path:
        return path
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    path, queue, startState = [], util.Queue(), problem.getStartState()
    queue.push(startState)
    parents = { startState : None }
    visited = [startState]
    while not queue.isEmpty():
        state = queue.pop()
        if problem.isGoalState(state):
            path = getPath(parents, state)
            break
        for successorState, direction, cost in problem.getSuccessors(state):
            if successorState not in visited:
                visited.append(successorState)
                parents[successorState] = (state, direction)
                queue.push(successorState)
    if path:
        return path
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    frontier.push( problem.getStartState(), 0)
    parents = { problem.getStartState() : None }
    distance = { problem.getStartState() : 0 }
    visited = []
    path = []
    while not frontier.isEmpty():
        # pdb.set_trace()
        state = frontier.pop()
        pathcost = distance[state]
        visited.append(state)
        if problem.isGoalState(state):
            while parents[state] is not None:
              parentState, direction = parents[state]
              path.append(direction)
              state = parentState
            path.reverse()
            break
        for successorState, direction, cost in problem.getSuccessors(state):
            if successorState not in visited:
                if successorState in distance and distance[successorState] < cost + pathcost:
                    continue
                if successorState in distance:
                    frontier.changePriority(successorState, cost + pathcost)
                else:
                    frontier.push(successorState, cost + pathcost)
                distance[successorState] = cost + pathcost
                parents[successorState] = (state, direction)
    if path:
        return path
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    frontier.push( problem.getStartState(), 0)
    parents = { problem.getStartState() : None }
    distance = { problem.getStartState() : 0 }
    visited = []
    path = []
    while not frontier.isEmpty():
        # pdb.set_trace()
        state = frontier.pop()
        pathcost = distance[state]
        visited.append(state)
        if problem.isGoalState(state):
            while parents[state] is not None:
              parentState, direction = parents[state]
              path.append(direction)
              state = parentState
            path.reverse()
            break
        for successorState, direction, cost in problem.getSuccessors(state):
            if successorState not in visited:
                if successorState in distance and distance[successorState] < cost + pathcost:
                    continue
                if successorState in distance:
                    frontier.changePriority(successorState, cost + pathcost + heuristic(successorState, problem))
                else:
                    frontier.push(successorState, cost + pathcost + heuristic(successorState, problem))
                distance[successorState] = cost + pathcost
                parents[successorState] = (state, direction)
    if path:
        return path
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
