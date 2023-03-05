
def simpsons_rule(f, a:float, b:float, n=1000)->float:
    dx = (b-a) / n

    area = 0.0
    for j in range(n):
        x1 = a + dx*j
        x0 = a + dx*(j-1)

        left = f(x0)
        right = f(x1)
        mid = f((x0 + x1) / 2)

        area += ((1/6) * (left + 4*mid + right) * dx)
    return area
