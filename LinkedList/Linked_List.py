class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'(DATA: {self.data} | NEXT: {self.next})'
    
class linkedList:
    def __init__(self):
        self.start = None

    def __repr__(self):
        nodes = ['START']
        for node in self:
            nodes.append(node.data)
        nodes.append('NIL')
        return '\n' + ' --> '.join(nodes)

    def __iter__(self):
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        length = 0
        for _ in self:
            length += 1
        return length

    def traverse(self):
        for node in self:
            print(node.data)

    def insert_at_beginning(self, element: Node):
        element.next = self.start
        self.start = element