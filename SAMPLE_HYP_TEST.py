from scipy.stats import t
D = [float(x) for x in input("Enter data:").split(',')]
pm = float(input("Enter null hypothesis population mean:"))
tails = int(input("One tail or two tail? (Enter 1 or 2)"))
alpha = float(input("Alpha (Sig. lvl)?"))
xbar = sum(D)/len(D)
s = (sum([(x-xbar)**2 for x in D])/(len(D)-1))**0.5
test_stat = (xbar - pm)/(s/len(D)**0.5)
crit_val = abs(t.ppf(alpha if tails == 1 else alpha >> 1,len(D)-1))
print("Test Stat = {}".format(test_stat))
print("Crit. Value = {}".format(crit_val))
print("{} the Ho!".format("Accept" if test_stat < crit_val else "Reject"))