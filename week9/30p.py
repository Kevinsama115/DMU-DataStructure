def make_morse_tree():
    root = TNode(None, None, None)

    for tp in table:
        code = tp[1]  # 알파벳 말고 모스 코드
        node = root

        for c in code:  # 모스코드 있는 동안 아래 반복
            if c == '.':  # 왼쪽으로 이동
                if node.left == None:  # 비었으면 빈 노드 만들기
                    node.left = TNode(None, None, None)
                node = node.left  # 그쪽으로 이동

            elif c == '-':  # 오른쪽으로 이동
                if node.right == None:  # 비었으면 빈 노드 만들기
                    node.right = TNode(None, None, None)
                node = node.right  # 그쪽으로 이동

        node.data = tp[0]  # 코드의 알파벳

    return root


def decode(root, code):
    node = root

    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right

    return node.data