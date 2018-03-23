
class Pilha():
    items = None
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if(len(self.items) == 0):
            return True
        return False

    def clean(self):
        self.items.clear()
     
