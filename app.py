from flask import Flask, request, jsonify, render_template
import ast
import operator as op

app = Flask(__name__)


_BIN_OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
}

_UNARY_OPS = {
    ast.UAdd: op.pos,
    ast.USub: op.neg,
}


def eval_expression(expr: str):
    # transforma a input string em uma tree
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError:
        raise ValueError("Expressao invalida.")
    return _eval_node(tree.body)


def _eval_node(node):
    # se e um numero -> devolve o numero
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    # se for uma op binaria, resolve recursivamente
    if isinstance(node, ast.BinOp) and type(node.op) in _BIN_OPS:
        lhs = _eval_node(node.left)
        rhs = _eval_node(node.right)
        return _BIN_OPS[type(node.op)](lhs, rhs)

    # se for unario, aplica o operador no valor dentro
    if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPS:
        operand = _eval_node(node.operand)
        return _UNARY_OPS[type(node.op)](operand)

    raise ValueError("Expressao nao permitida.")


@app.post("/api/calc")
def api_calc():
    # garante q se json vier quebrado ou None, o codigo n quebra
    data = request.get_json(silent=True) or {}
    # limpa espacos inicio/fim
    expr = (data.get("expr") or "").strip()

    # se nao veio expr, retorna erro 400
    if not expr:
        return jsonify(error="Campo 'expr' e obrigatorio"), 400

    # tenta calcular, 200 ok 400 client error
    try:
        result = eval_expression(expr)
        return jsonify(result=result)
    except ZeroDivisionError:
        return jsonify(error="Divisao por zero."), 400
    except ValueError as e:
        return jsonify(error=str(e)), 400


@app.get("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
