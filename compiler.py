import re

class AST:
    pass

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(AST):
    def __init__(self, value):
        self.value = value

class Var(AST):
    def __init__(self, name):
        self.name = name

class ParserError(Exception):
    pass

class MiniCompiler:
    def __init__(self, source, env):
        self._tokens = iter(
            re.findall(r'[a-zA-Z_]\w*|\d+(?:\.\d+)?|[+*/()\-^]', source) + ['?']
        )
        self._current = None
        self._env = env
        self._temp_count = 0
        self.advance()

    def advance(self):
        try:
            self._current = next(self._tokens)
        except StopIteration:
            self._current = None

    def factor(self):
        token = self._current
        if token and token.replace('.', '', 1).isdigit():
            self.advance()
            return Num(float(token) if '.' in token else int(token))
        elif token and token.isalpha():
            if token not in self._env:
                raise ParserError(f"Undefined variable '{token}'")
            self.advance()
            return Var(token)
        elif token == '(':
            self.advance()
            node = self.expr()
            if self._current != ')':
                raise ParserError("Expected ')'")
            self.advance()
            return node
        raise ParserError(f"Unexpected token: {token}")

    def power(self):
        node = self.factor()
        while self._current == '^':
            op = self._current
            self.advance()
            node = BinOp(node, op, self.factor())
        return node

    def term(self):
        node = self.power()
        while self._current in ('*', '/'):
            op = self._current
            self.advance()
            node = BinOp(node, op, self.power())
        return node

    def expr(self):
        node = self.term()
        while self._current in ('+', '-'):
            op = self._current
            self.advance()
            node = BinOp(node, op, self.term())
        return node

    def generate_tac(self, node):
        if isinstance(node, Num): return str(node.value)
        if isinstance(node, Var): return node.name

        left = self.generate_tac(node.left)
        right = self.generate_tac(node.right)

        self._temp_count += 1
        temp = f"t{self._temp_count}"
        print(f"{temp} = {left} {node.op} {right}")
        return temp