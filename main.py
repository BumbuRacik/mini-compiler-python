from compiler import MiniCompiler, Num, Var, BinOp, ParserError


def evaluate(node, env):
    if isinstance(node, Num):
        return node.value
    if isinstance(node, Var):
        return env[node.name]
    if isinstance(node, BinOp):
        left = evaluate(node.left, env)
        right = evaluate(node.right, env)

        if node.op == '+': return left + right
        if node.op == '-': return left - right
        if node.op == '*': return left * right
        if node.op == '/': return left / right
        if node.op == '^': return left ** right

    raise Exception("Unknown node")


tests = [
    "a ^ 2 + b * c",
    "a ^ 2 ^ 3",
    "(a + b) * c",
    "a * b + c ^ 2",
    "a ^ (b + c)",
]


symbol_table = {
    'a': 2,
    'b': 3,
    'c': 4
}


print("=== MINI COMPILER TEST ===")

for source_code in tests:
    print("\n=========================")
    print(f"Input: {source_code}")

    try:
        # Compile
        compiler = MiniCompiler(source_code, symbol_table)
        ast = compiler.expr()

        print("\n--- Three Address Code (TAC) ---")
        compiler.generate_tac(ast)

        result = evaluate(ast, symbol_table)
        print("\nHasil Evaluasi:", result)

    except ParserError as pe:
        print("Parser Error:", pe)

    except Exception as e:
        print("Error:", e)

print("\n=== SELESAI ===")