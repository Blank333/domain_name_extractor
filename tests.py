def test(command, tests):
    result = []
    for i in range(len(tests)):
        result.append("Pass" if command(**tests[i]["input"]) == tests[i]["output"] else "Fail")
    return result

def add_test(input, output, tests):
    tests.append({
        "input": {
            "url": input
            },
        "output": output
        })
