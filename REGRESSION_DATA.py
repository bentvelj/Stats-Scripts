from scipy.stats import t

x = [int(i) for i in input("Enter x values separated by space: ").split()]
y = [int(i) for i in input("Enter y values separated by space: ").split()]
HYPB1 = int(input("Enter hypothesis test B1 (null hypothesis): "))
HA = input("Enter alternative hypothesis (input <, >, or =/=): ")
alpha = float(input("Enter hypothesis significance value (between 0 and 1): "))

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
sigmaHat = (SSE / (n-2))**(1/2)
SE_B1HAT = sigmaHat / (Sxx)**(1/2)

t_nMinus2 = (B1HAT - HYPB1) / SE_B1HAT

print("\nB0 = {}, B1 = {}".format(B0, B1))
print("Residuals: ", end=" ")
for i in residuals:
    print(i, end=" ")
print("\nSSE: {}".format(SSE))
print("t_n-2 (test statistic) = {}".format(t_nMinus2))

if HA == "<":
    multiplier = -1
else:
    multiplier = 1

if HA == "=/=":
    tails = 2
else:
    tails = 1

critVal = multiplier * abs((t.ppf(alpha/tails, n-2)))

print("Critical value = {}".format(critVal))