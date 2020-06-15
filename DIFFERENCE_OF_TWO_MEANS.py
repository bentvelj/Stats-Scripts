from scipy.stats import t,norm
print("CASE 1: Both std. devs are known.")
print("CASE 2: Both std. devs are unknown, but assume equal variances.")
print("CASE 3: Both std. devs are unknown.")
CASE=int(input("Enter the case:"))
if(CASE == 1): ## NO TEST EXAMPLES
    n1 = int(input("Enter n for first group: "))
    xb1 = float(input("Enter xbar for first group: "))
    s1 = float(input("Enter POPULATION std dev for first group: "))
    n2 = int(input("Enter n for second group: "))
    xb2 = float(input("Enter xbar for second group: "))
    s2 = float(input("Enter POPULATION std dev for second group: "))
    alpha = float(input("Alpha (Sig lvl): "))
    Ha = input("Alternative Hypothesis (Enter <, >, or =/=): ")
    tails = 2 if Ha == "=/=" else 1
    test_stat = (xb1 - xb2)/((s1**2/n1 + s2**2/n2))**0.5
    crit_val = norm.ppf(alpha/tails) if Ha == "<" else norm.ppf(1-alpha/tails)
    p_val = tails*norm.cdf(-test_stat)
    print("Test Stat = {}".format(test_stat))
    print("Crit. Value = {}".format(crit_val))
    print("P-Value = {}".format(p_val))
    print("{} the Ho!".format("Accept" if test_stat < crit_val else "Reject"))
    
elif(CASE==2):
    n1 = int(input("Enter n for first group: "))
    xb1 = float(input("Enter xbar for first group: "))
    s1 = float(input("Enter SAMPLE std dev for first group: "))
    n2 = int(input("Enter n for second group: "))
    xb2 = float(input("Enter xbar for second group: "))
    s2 = float(input("Enter SAMPLE dev for second group: "))
    alpha = float(input("Alpha (Sig lvl): "))
    Ha = input("Alternative Hypothesis (Enter <, >, or =/=): ")
    tails = 2 if Ha == "=/=" else 1
    sp = ((n1-1)*s1**2 + (n2-1)*s2**2)/(n1 + n2-2)
    test_stat = (xb1 - xb2)/((sp*(1/n1+1/n2))**0.5)
    crit_val = -abs(t.ppf(alpha/tails,n1+n2-2)) if Ha == "<" else abs(t.ppf(alpha/tails,n1+n2-2))
    print("Test Stat = {}".format(test_stat))
    print("Crit. Value = {}".format(crit_val))
    print("{} the Ho!".format("Accept" if test_stat < crit_val else "Reject")) 
        
elif(CASE==3):
    n1 = int(input("Enter n for first group: "))
    xb1 = float(input("Enter xbar for first group: "))
    s1 = float(input("Enter SAMPLE std dev for first group: "))
    n2 = int(input("Enter n for second group: "))
    xb2 = float(input("Enter xbar for second group: "))
    s2 = float(input("Enter SAMPLE dev for second group: "))
    alpha = float(input("Alpha (Sig lvl): "))
    Ha = input("Alternative Hypothesis (Enter <, >, or =/=): ")
    tails = 2 if Ha == "=/=" else 1
    sp = ((n1-1)*s1**2 + (n2-1)*s2**2)/(n1 + n2-2)
    test_stat = (xb1 - xb2)/(s1**2/n1+s2**2/n2)**0.5
    df = int((s1**2/n1+s2**2/n2)**2/((s1**2/n1)**2/(n1-1)+(s2**2/n2)**2/(n2-1)))
    crit_val = -abs(t.ppf(alpha/tails,df)) if Ha == "<" else abs(t.ppf(alpha/tails,df))
    print("Test Stat = {}".format(test_stat))
    print("Crit. Value = {}".format(crit_val))
    print("{} the Ho!".format("Accept" if abs(test_stat) < abs(crit_val) else "Reject")) 