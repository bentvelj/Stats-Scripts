from scipy.stats import t,norm

n = int(input("Enter n: "))
xbar = float(input("Enter xbar: "))
s = float(input("Enter std dev : "))
pm = float(input("Enter null hypothesis population mean: "))
Ha = input("Alternative Hypothesis (Enter <, >, or =/=): ")
tails = 2 if Ha == "=/=" else 1
alpha = float(input("Alpha (Sig. lvl): "))
test_stat = (xbar - pm)/(s/n**0.5)
crit_val = norm.ppf(alpha/tails) if Ha == "<" else norm.ppf(1-alpha/tails)
p_val = tails * norm.cdf(-abs(round(test_stat, 2)))
print("\nTest Stat = {}".format(test_stat))
print("Crit. Value = {}".format(crit_val))
print("P-Value = {}".format(p_val))
print("{} the Ho!".format("Accept" if abs(test_stat) < abs(crit_val) else "Reject"))