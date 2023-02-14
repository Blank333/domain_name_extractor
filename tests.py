def test(command, tests):
    for i in range(len(tests)):
        return True if command == tests[i]["output"] else False

def add_test(input, output, tests):
    tests.append({
        "input": {
            "url": input
            },
        "output": output
        })
