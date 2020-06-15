from scipy.stats import t

a = int(input("Enter the number of groups: "))
D = []
for i in range(a):
    D.append([float(x) for x in input("Enter the elements of group " + str(i + 1) + ": ").split(',')])
alpha = float(input("Enter a two-tailed significance value (if applicable): "))
N = sum([len(x) for x in D])
GT = sum([sum(x) for x in D])
GM = GT/sum([len(x) for x in D])
SST = 0
for i in range(a):
    for j in range(len(D[i])):
        SST+=(D[i][j] - GM)**2
SSE = 0
for i in range(a):
    for j in range(len(D[i])):
        SSE+=(D[i][j]-sum(D[i])/len(D[i]))**2
SSTr = SST - SSE
MSTr = SSTr / (a-1)
MSE = SSE / (N - a)
F = MSTr / MSE
print("\nSST = {}".format(SST))
print("SSE = {}".format(SSE))
print("SSTr = {}".format(SST-SSE))
print("MSTr = {}, MSE = {}".format(MSTr, MSE))
print("F = {}".format(F))

n = [len(x) for x in D]
means = [sum(x)/len(x) for x in D]

done = []
for i in range(len(means)):
    for j in range(len(means)):
        if i != j and (j, i) not in done:
            done.append((i,j))
            diff = abs(means[i] - means[j])
            LSD = abs(t.ppf(alpha/2, N-a)) * (MSE*(1/n[i] + 1/n[j])) ** (1/2)
            conclusion = "Accept Null"
            if diff > LSD:
                conclusion = "Reject Null"
            print("u{} = u{}, LSD = {}, Difference = {}, Conclusion = {}".format(i+1,j+1,LSD,diff,conclusion))