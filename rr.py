global n, pid, at, bt, ct, wt, tat, rem_bt, q
at, bt, ct, wt, tat, pid, rem_bt = [], [], [], [], [], [], []

def readInput():
	global n, q
	global pid, at, bt, rem_bt
	n = input("Enter the number of processes: ")
	q = input("Enter the time quanta: ")
	
	for i in range(n):
		pid.append(i)	
	
		b = input("Enter the BT of P"+str(i)+": ")
		at.append(0)
		bt.append(b)
		ct.append(0)
		
	rem_bt = bt[:]
	
def getCT():
	global n, pid, at, bt, ct, wt, tat
	
	t = 0
	flag = True
	completed = []
	ongoing = []
	
	while flag:
		# FIND THE PROCESSES THAT ARE NOT DONE
		check = False
		for i in range(n):
			if (rem_bt[i] > 0):
				check = True
				
				if rem_bt[i] > q:
					t = t + q
					rem_bt[i] = rem_bt[i] - q
				
				else:
					t = t + rem_bt[i]
					#wt[i] = t - bt[i]
					rem_bt[i] = 0
					ct[i] = t
			else:
				continue
				
		if check == False:
			flag = False
			break
			
	
def calc():
	global at, bt, ct, wt, tat
	
	for i in range(n):
		tat.append(ct[i] - at[i])
		
	for i in range(n):
		wt.append(tat[i] - bt[i])		

def display():
	print "\nPID\tAT\tBT\tCT\tTAT\tWT\n"
	
	for i in range(n):
		st1 = str("P"+str(pid[i])) + "\t" + str(at[i]) + "\t" + str(bt[i]) + "\t" + str(ct[i]) + "\t"+ str(tat[i]) + "\t" + str(wt[i]) + "\n"
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
	
