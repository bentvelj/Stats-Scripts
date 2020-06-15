from scipy.stats import t
D = [float(x) for x in input("Enter data: ").split(',')]
pm = float(input("Enter null hypothesis population mean: "))
Ha = input("Alternative Hypothesis (Enter <, >, or =/=): ")
tails = 2 if Ha == "=/=" else 1
alpha = float(input("Alpha (Sig. lvl): "))
xbar = sum(D)/len(D)
s = (sum([(x-xbar)**2 for x in D])/(len(D)-1))**0.5
test_stat = (xbar - pm)/(s/len(D)**0.5)
crit_val = -abs(t.ppf(alpha/tails,len(D)-1)) if Ha == "<" else abs(t.ppf(alpha/tails,len(D)-1)) 
print("\nTest Stat = {}".format(test_stat))
print("Crit. Value = {}".format(crit_val))
print("{} the Ho!".format("Accept" if abs(test_stat) < abs(crit_val) else "Reject"))