class Node(object):
    def __init__(self, value):
        self.value = value
        self.parant = self

    def link(self, node):
        parant = node.root()
        selfRoot = self.root()
        selfRoot.parant = parant

    def root(self):
        parant = self
        while parant.parant != parant:
            parant.parent = parant.parant.parant
            parant = parant.parant
        return parant

    def __eq__(self, node):
        return self.value == node.value

def islands(matrix, n):
    nodeMatrix = []
    for i in range(n):
        nodeMatrix.append([])
        for j in range(n):
            if matrix[i][j]:
                nodeMatrix[i].append(Node((i, j)))
                if i > 0 and nodeMatrix[i-1][j]:
                    nodeMatrix[i][j].link(nodeMatrix[i-1][j])
                if j > 0 and nodeMatrix[i][j - 1]:
                    nodeMatrix[i][j].link(nodeMatrix[i][j-1])
            else:
                nodeMatrix[i].append(None)
    rootNodeMap = {}
    for i in range(n):
        for j in range(n):
            if nodeMatrix[i][j]:
                rootNode = nodeMatrix[i][j].root()
                rootNodeMap.setdefault(rootNode.value, set()).add((i, j))
    return rootNodeMap

if __name__ == "__main__":
    islands = islands([[1,1,0,0,0], [0,1,0,0,1], [1,0,0,1,1], [0,0,0,0,0,0], [1,0,1,0,1]], 5)
    print(islands)
