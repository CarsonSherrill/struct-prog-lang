import parser, tokenizer

def evaluate(ast, environment):
    if ast["tag"] == "number":
        return ast["value"]
    elif ast["tag"] == "identifier":
        if ast["tag"] in environment:
            return environment[ast["value"]]
        else:
            raise ValueError(f"Unknown identifier: {ast['value'}")
    elif ast["tag"] == "+":
        return evaluate(ast["left"], environment) + evaluate(ast["right"], environment)
    elif ast["tag"] == "-":
        return evaluate(ast["left"], environment) - evaluate(ast["right"], environment)
    elif ast["tag"] == "*":
        return evaluate(ast["left"], environment) * evaluate(ast["right"], environment)
    elif ast["tag"] == "/":
        return evaluate(ast["left"], environment) / evaluate(ast["right"], environment)
    else:
        raise ValueError(f"Unknown AST node: {ast}")

def test_evaluate():
    print("test evaluate()")
    ast = {"tag": "number", "value": 3}
    assert evaluate(ast,{}) == 3
    ast = {
        "tag": "+",
        "left": {"tag": "number", "value": 3},
        "right": {"tag": "number", "value": 4},
    }
    assert evaluate(ast,{}) == 7
    ast = {
        "tag": "*",
        "left": {
            "tag": "+",
            "left": {"tag": "number", "value": 3},
            "right": {"tag": "number", "value": 4},
        },
        "right": {"tag": "number", "value": 5},
    }
    assert evaluate(ast,{}) == 35
    tokens = tokenizer.tokenize("3*(4+5)")
    ast, tokens = parser.parse_expression(tokens)
    assert evaluate(ast,{}) == 27

def test_evaluate_environments(){
    print("test evaluate() wtih environments")
    ast = {"tag": "number", "value": "x"}
    assert evaluate(ast,{"x":3}) == 3
}

if __name__ == "__main__":
    test_evaluate()
    test_evaluate_environments()
    print("done.")
