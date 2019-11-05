class Node:
    def __init__(self, token, value=None, ntype=None, children=None):
            self.token = token
            self.value = value
            self.ntype = ntype

            if children:
                self.children = children
            else:
                self.children = []

    def get_values(self):
        return str(self.token)

    def traverse_ast(self, result):
        if self.children:
            for child in self.children:

                if(isinstance(child, Node)):
                    result.append(f'({self.get_values()} -> {child.get_values()})')
                    child.traverse_ast(result)
                else:
                    result.append(f'{self.get_values()} -> Value: {str(child)}')

    def __str__(self):
        ast = []
        self.traverse_ast(ast)
        return '\n'.join(ast)
