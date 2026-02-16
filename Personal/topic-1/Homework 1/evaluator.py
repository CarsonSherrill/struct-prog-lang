import parser, tokenizer

def evaluate(ast):
    if ast["tag"] == "number":
        return ast["value"]
    elif ast["tag"] == "+":
        return evaluate(ast["left"]) + evaluate(ast["right"])
    elif ast["tag"] == "-":
        return evaluate(ast["left"]) - evaluate(ast["right"])
    elif ast["tag"] == "*":
        return evaluate(ast["left"]) * evaluate(ast["right"])
    elif ast["tag"] == "/":
        return evaluate(ast["left"]) / evaluate(ast["right"])
    elif ast["tag"] == "%":
        left = evaluate(ast["left"])
        right = evaluate(ast["right"])
        if left < 0 or right < 0:
            raise ValueError("Negative number used in modulo operation")
        return left % right
    else:
        raise ValueError(f"Unknown AST node: {ast}")

def test_evaluate():
    print("test evaluate()")
    ast = {"tag": "number", "value": 3}
    assert evaluate(ast) == 3
    ast = {
        "tag": "+",
        "left": {"tag": "number", "value": 3},
        "right": {"tag": "number", "value": 4},
    }
    assert evaluate(ast) == 7
    ast = {
        "tag": "*",
        "left": {
            "tag": "+",
            "left": {"tag": "number", "value": 3},
            "right": {"tag": "number", "value": 4},
        },
        "right": {"tag": "number", "value": 5},
    }
    assert evaluate(ast) == 35
    tokens = tokenizer.tokenize("3*(4+5)")
    ast, tokens = parser.parse_expression(tokens)
    assert evaluate(ast) == 27

    tokens = tokenizer.tokenize("7 % 3")
    ast, tokens = parser.parse_expression(tokens)
    assert evaluate(ast) == 1
    tokens = tokenizer.tokenize("2 + 11 % 3")
    ast, tokens = parser.parse_expression(tokens)
    assert evaluate(ast) == 4
    tokens = tokenizer.tokenize("9 % 4 * 3")
    ast, tokens = parser.parse_expression(tokens)
    assert evaluate(ast) == 3

if __name__ == "__main__":
    test_evaluate()
    print("done.")
