def fibonacci(start, length):
    res = []
    for i in range(length):
        if len(res) < 2:
            res.append(start)
        else:
            res.append(res[i-2] + res[i-1])
    return res


def run():
    t = fibonacci(1, 10)
    print(t)
