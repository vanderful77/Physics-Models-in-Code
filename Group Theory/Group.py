class Group:
    def __init__(self, elements, operation):
        self.elements = elements
        self.operation = operation
    def validity(self):
        # check if closed
        close = True
        for a in self.elements:
            for b in self.elements:
                if not (self.operation(a,b) in self.elements):
                    closed = False
        
        # check identity
        identity = False
        for a in self.elements:
            for b in self.elements:
                if (self.operation(a,b) == a):
                    identity = True
    def __repr__(self):
        return f'Group(elements={self.elements}, operation={self.operation})'
    
# elements = {0, 1, 2, 3, 4}

# def addition(a, b):
#     return (a+b)%5

# group1 = Group(elements, addition)
# print(group1.validity())