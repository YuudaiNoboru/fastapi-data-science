def euclidian_division(dividend, divisor):
    quotient = dividend//divisor
    remainder = dividend % divisor
    return (quotient, remainder)

t = euclidian_division(3, 2)
print(t[1])

q, r = euclidian_division(42, 4)
print(q)
print(r)