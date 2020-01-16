global n, pid, at, bt, ct, wt, tat, rem_bt
at, bt, ct, wt, tat, pid, rem_bt = [], [], [], [], [], [], []

def readInput():
	global n
	global pid, at, bt, rem_bt
	n = input("Enter the number of processes: ")
	
	for i in range(n):
		pid.append(i)	
	
		a, b = map(int, raw_input("Enter AT and BT of P"+str(i)+": ").split())
		at.append(a)
		bt.append(b)
		ct.append(0)
		
	rem_bt = bt[:]

def getCT():
	global n, pid, at, bt, ct, wt, tat
	validList = []
	completed = []
	t = 0
	flag = True
	
	while flag:
		
		# FIND THE PROCESSES THAT ARRIVED:
		for i in range(n):
			if (at[i] <= t) and (pid[i] not in completed) and (pid[i] not in validList):
				validList.append(pid[i])
	
		# FIND THE LEAST REMAINING TIME
		small = rem_bt[validList[0]]
		pos = validList[0]
		
		for i in validList:
			if small > rem_bt[i]:
				small = rem_bt[i]
				pos = i
				
		# REDUCE TIME BY 1 UNIT
		rem_bt[pos] -= 1
		t = t + 1
	
		if rem_bt[pos] == 0:
			completed.append(pos)
			ct[pos] = t
			validList.remove(pos)
		
		if validList == []:
			flag = False
	
def calc():
	global at, bt, ct, wt, tat
	
	for i in range(n):
		tat.append(ct[i] - at[i])
		
	for i in range(n):
		wt.append(tat[i] - bt[i])		
		
def display():
	print "\nPID\tAT\tBT\tCT\tTAT\tWT\n"
	
	for i in range(n):
		st1 = str("P"+pid[i]) + "\t" + str(at[i]) + "\t" + str(bt[i]) + "\t" + str(ct[i]) + "\t"+ str(tat[i]) + "\t" + str(wt[i]) + "\n"
		print(st1)
		
def main():
	readInput()
	getCT()
	calc()
	
	avgWT = sum(wt)/float(n)
	avgTAT = sum(tat)/float(n)
	
	display()
	
	print("Average WT = " + str(avgWT))
	print("Average TAT = " + str(avgTAT))
main()
	
