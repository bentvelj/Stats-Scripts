from scipy.stats import norm

a, b = map(float, input("Enter numerator, denominator of sample proportion (p hat) separated by space: ").split())
P_0 = float(input("Enter population proportion (p nought) as float: "))
HA = input("Enter alternative hypothesis (input <, >, or =/=): ")
alpha = float(input("Enter hypothesis significance value (between 0 and 1): "))

P_HAT = a/b
Z_0 = (P_HAT - P_0) / (P_0 * (1 - P_0) / b) ** (1/2)

tails = 2 if HA == "=/=" else 1

critVal = norm.ppf(alpha/tails) if HA == "<" else norm.ppf((1-alpha)/tails)
pVal = norm.cdf(-abs(round(Z_0, 2)))

conclusion = "Reject Null" if abs(Z_0) > abs(critVal) else "Accept Null"

print("\nTest statistic (Z_0) = {}".format(Z_0))
print("Critical value = {}".format(critVal))
print("P Value = {}".format(pVal))
print("Conclusion: {}".format(conclusion))