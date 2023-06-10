def power(baseNum, powNum):
    result = 1
    for x in range(powNum):
        result = result * baseNum
    return result


print(power(2, 3))
