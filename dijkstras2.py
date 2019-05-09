#graph={'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}
graph={'a':{'b':10,'c':3},'b':{'a':10,'c':2},'c':{'a':3,'b':2}}


def dijkstra(graph,start):
    shortest_distance={}
    predecessor={}
    unseenNodes=graph
    infinity=999999
    path=[]
    for node in unseenNodes:
        shortest_distance[node]=infinity
    shortest_distance[start]=0
    #print(shortest_distance)

    while unseenNodes:
        minNode=None
        for node in unseenNodes:
            if minNode is None:
                minNode=node
            elif shortest_distance[node]<shortest_distance[minNode]:
                minNode=node

        for childNode,weight in graph[minNode].items():
            if weight+shortest_distance[minNode]<shortest_distance[childNode]:
                shortest_distance[childNode]=weight+shortest_distance[minNode]
                predecessor[childNode]=minNode

        unseenNodes.pop(minNode)
    #print(shortest_distance)
    return shortest_distance

