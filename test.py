x = [1,3,5,7,23,11,12]
y = [2,4,123,8,10,12,13]
n = len(x)
B1 = (n * sum([x[i] * y[i] for i in range(len(x))]) - sum(x)*sum(y)) \
/ ((n*sum([x[i] ** 2 for i in range(len(x))])) - (sum(x) ** 2))

B0 = (sum(y) * sum([x[i] ** 2 for i in range(len(x))]) - (sum(x)*sum([x[i] * y[i] for i in range(len(x))]))) \
/ ((n*sum([x[i] ** 2 for i in range(len(x))])) - (sum(x) ** 2))

residuals = [(y[i] - (x[i]*B1 + B0)) for i in range(n)]
SSE = sum([i ** 2 for i in residuals])

Sxy = sum([x[i] * y[i] for i in range(len(x))]) - (sum(x)*sum(y))/n
Sxx = sum([x[i] ** 2 for i in range(len(x))]) - (sum(x) ** 2)/n
B1HAT = Sxy / Sxx

print(B1HAT,B1)