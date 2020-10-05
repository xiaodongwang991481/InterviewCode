import collections

def presentGraph(nodes, edges):
    nodeMap = {}
    for node in nodes:
        nodeMap[node] = set()
    for edge in edges:
        startNode, endNode = edge
        nodeMap[startNode].add(endNode)
    return nodeMap

def reachableNodes(startNode, graph):
    nodeSet = set()
    nodeQueue = collections.deque([startNode])
    while nodeQueue:
        node = nodeQueue.pop()
        nodeSet.add(node)
        nextNodes = graph[node]
        for nextNode in nextNodes:
            if nextNode not in nodeSet:
                nodeQueue.append(nextNode)
    return nodeSet


if __name__ == "__main__":
    graph = presentGraph([0,1,2,3,4,5], [(0, 1), (1,2), (2, 0), (3, 4), (4,5), (5, 3)])
    print("graoh: %s" % graph)
    nodes = reachableNodes(4, graph)
    print('reachable nodes from 0 is %s' % nodes)