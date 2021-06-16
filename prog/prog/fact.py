def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


_fact_test_cases = [
    ((2,), 2),
    ((3,), 6),
    ((3,), 7)
]


def runTests(fun, test_cases):
    return [params
            for (params, expected) in test_cases
            if not assertEquals(expected, fun.__call__(*params),
                                "%s%s" % (fun.__name__, params))]


def assertEquals(expected, actual, message=None):
    result = expected == actual
    if not result:
        print("In %s, expecting %s, found %s" % (message, expected, actual))
    return result


if __name__ == '__main__':
    runTests(fact, _fact_test_cases)
