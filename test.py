'''

left = 0
right = len(nums)-1

while left <= right:
    medium = (left+right)//2

    if nums[medium]<target:
        left=medium+1
    elif nums[medium]>target:
        right=medium-1
    elif nums[medium]==target:
        return True

return False
#*-----------------BFS---------------------#
def bfs(adjList, startNode):
    q=deque
    
    # add start node

    # iterate over the q so long as it is non-empty
    while q:
        # dequeuing over front of queue
        currNode=q.popLeft()

        # loop over the neighbours of the starting node
        for neighbour in adjList[currNode]:

            if not visited[neighbour]:
                visited[neighbour]=True
                q.addRight(neighbour)
#-----------------DFS------------------------#
def dfs(adjList, startNode):
    stack=[]
    visited=[False for _ in range(len(adjList))]
    
    stack.append(startNode)
    visited[startNode]=True

    while stack:
        currNode=stack.pop()
        if not visited[currNode]:
            visited[currNode]=True
        for neighbour in adjList[currNode]:
            if not visited[neighbour]:
                stack.append(neighbour)

#-----------------RECURSIVE DFS------------------------#
def dfs(adjList, startNode, visited=None):
    if visited==None:
        visited=[False for _ in range(len(adjList))]

    currNode=startNode
    if not visited[currNode]:
        visited[currNode]=True
        
    for neighbour in adjList[currNode]:
        if not visited[neighbour]:
            dfs(adjList, neighbour, visited)
'''
print("hello")

import math
print(math.pi)