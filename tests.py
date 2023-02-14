def test(command, tests):
    result = []
    for i in range(len(tests)):
        result.append(True if command(**tests[i]["input"]) == tests[i]["output"] else False)
    return result

def add_test(input, output, tests):
    tests.append({
        "input": {
            "url": input
            },
        "output": output
        })
