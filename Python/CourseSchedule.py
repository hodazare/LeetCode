"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses? 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible. 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5

SOLUTION: topological sort

"""
from collections import defaultdict
class nodes(object):
    def __init__(self):
        self.degree = 0
        self.inNeighbors = []
        
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        graph = defaultdict(nodes)
        q = []
        
        for p in prerequisites:
            graph[p[1]].inNeighbors.append(p[0])
            graph[p[0]].degree += 1
        
        for node, neighbor in graph.items():
            if neighbor.degree == 0:
                q.append(node)
        
        visitedEdge = 0
        while q:
            node = q.pop()
            for neighbor in graph[node].inNeighbors:
                graph[neighbor].degree -= 1
                visitedEdge += 1
                
                if graph[neighbor].degree == 0:
                    q.append(neighbor)
        if visitedEdge == len(prerequisites):
            return True
        else:
            return False
