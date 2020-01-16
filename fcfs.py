global n, pid, at, bt, ct, wt, tat
at, bt, ct, wt, tat, pid = [], [], [], [], [], []

def readInput():
	global n
	global pid, at, bt
	n = input("Enter the number of processes: ")
	
	for i in range(n):
		pid.append("P"+str(i))	
	
		a, b = map(int, raw_input("Enter AT and BT of P"+str(i)+": ").split())
		at.append(a)
		bt.append(b)

def getCT():
	global at, bt, ct
	ct.append(at[0] + bt[0])
	
	for i in range(1, n):
		ct.append(ct[i-1] + bt[i])
		
def calc():
	global at, bt, ct, wt, tat
	
	for i in range(n):
		tat.append(ct[i] - at[i])
		
	for i in range(n):
		wt.append(tat[i] - bt[i])

def display():
	print "\nPID\tAT\tBT\tCT\tTAT\tWT\n"
	
	for i in range(n):
		st1 = str(pid[i]) + "\t" + str(at[i]) + "\t" + str(bt[i]) + "\t" + str(ct[i]) + "\t"+ str(tat[i]) + "\t" + str(wt[i]) + "\n"
		print(st1)
		

def main():
	global n, pid, at, bt, ct, wt, tat
	readInput()
	getCT()
	calc()
	
	avgWT = sum(wt)/float(n)
	avgTAT = sum(tat)/float(n)
	
	display()
	print("Average WT = " + str(avgWT))
	print("Average TAT = " + str(avgTAT))

main()
	
