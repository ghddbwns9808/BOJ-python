def preorder(cur):
    print(cur, end='')
    for i in range(2):
        child = graph[cur][i]
        if child != '.':
            preorder(child)



def inorder(cur):
    root = cur
    left = graph[cur][0]
    right = graph[cur][1]

    if left != '.':
        inorder(left)
    print(root, end='')
    if right != '.':
        inorder(right)


def postorder(cur):
    for i in range(2):
        child = graph[cur][i]
        if child != '.':
            postorder(child)

    print(cur, end='')


N = int(input())

graph = {}
for _ in range(N):
    Node, L, R = map(str, input().split())
    graph[Node] = [L,R]

preorder('A')
print()
inorder('A')
print()
postorder('A')