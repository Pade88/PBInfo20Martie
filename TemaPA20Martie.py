import math

#1625
def eqSolver():
	pv_inputs=input().split(" ")
	pv_inputA = float(pv_inputs[0])
	pv_inputB = float(pv_inputs[1])
	pv_inputC = float(pv_inputs[2])
	if pv_inputA == 0:
		return
	lv_delta = (pv_inputB**2) - 4*pv_inputA*pv_inputC

	if lv_delta < 0:
		print("Nu are solutii reale")
		return
	elif lv_delta == 0:
		print("Radacina dubla {}".format((-1*pv_inputB)/(2*pv_inputA)))
	else:	
		print("{:.2f} {:.2f}".format(((-1*pv_inputB) + math.sqrt(lv_delta))/(2*pv_inputA), ((-1*pv_inputB) - math.sqrt(lv_delta))/(2*pv_inputA)))


#3391
#3391
#3391
#3391
#3391

#327
def nonZeroNumbers():
	pv_input = int(input())
	if pv_input > 0 and pv_input <101:
		for index in range(0, pv_input):
			print(index+1, end = " ")


#328
def NonZeroNumbersDecreasing():
	pv_input = int(input())
	if pv_input > 0 and pv_input <101:
		for index in reversed(range(0, pv_input)):
			print(index+1, end = " ")



#3231
def NonZeroIncreasingAndDecreasing():
	pv_input = int(input())
	if pv_input > 0 and pv_input <101:
		for index in range(0, pv_input):
			print(index+1, end = " ")
		print()
		for index in reversed(range(0, pv_input)):
			print(index+1, end = " ")

#3232
def NonZeroIncreasingOdd():
	pv_input = int(input())
	if pv_input > 0 and pv_input <101:
		for index in range(0, pv_input):
			if index & 1:
				print(index+1, end = " ")

#3233
def NonZeroDeacreasingEven():
	pv_input = int(input())
	if pv_input > 0 and pv_input <101:
		for index in reversed(range(0, pv_input)):
			if not index & 1:
				print(index+1, end = " ")

#1362
def PowerOfTen():
	pv_input = int(input())
	if pv_input >= 0 and  pv_input <= 1000:
		print (10**pv_input)
 
#1681 MERGE DOAR IN C++

#2747
def someKindOfLog():
	pv_input = input().split(" ")
	lv_base = int(pv_input[0])
	lv_exp = int(pv_input[1])
	if 1 <= lv_base <= lv_exp <= 1000000:
		for power in range(1, 1000000):
			if lv_base ** power == lv_exp:
				print(power)
				return


#1565 MERGE DOAR IN C++
def nTimesTenAtA():
	pv_input = input().split(" ")
	lv_N = int(pv_input[0])
	lv_A = int(pv_input[1])
	if 1 <= lv_N <= 1000 and 0 <= lv_A <= 5:
		print(lv_N * (10**lv_A))

#348
def PowersLessThan():
	pv_input = input().split(" ")
	lv_inputN = int(pv_input[0])
	lv_inputP = int(pv_input[1])
	if 2<= lv_inputN <= 10 and 1<= lv_inputP <= 1000000000:
		for power in range (0, lv_inputP):
			if lv_inputN**power < lv_inputP:
				print(lv_inputN**power, end = " ")
			else:
				return


#2572
#Aplicatia ruleaza prin lista, si daca radical din numar este intreg, il returneaza ca patrat perfect.
def CheckIfItsPerfect():
	pv_input = input().split(" ")
	lv_inputCheck = int(pv_input[0])
	lv_list = []
	for lv_index in range(1, lv_inputCheck+1):
		lv_list.append(pv_input[lv_index])
	
	for lv_idx in lv_list:
		lv_idx = float(lv_idx)
		if math.sqrt(lv_idx) -  int(math.sqrt(lv_idx)) == 0:
			print("DA")
		else:
			print("NU")

#2695 XXXXX
#2695 XXXXX
#2695 XXXXX
#2695 XXXXX


#351
def Pyramid():
	pv_input = int(input())
	lv_check = 1
	if 1 <= pv_input <= 20:
		while lv_check <= pv_input:
			for lv_index in range(1, lv_check+1):
				print(lv_index, end = " ")
			print()
			lv_check = lv_check + 1

#456 --- Nu functioneaza ? ? ?
def PyramidChars():
	pv_input = input().split(" ")
	lv_lines = int(pv_input[0])
	lv_rows =  pv_input[1]
	lv_check = 1
	if 1 <= lv_lines <= 20 and  33 <= ord(lv_rows) <= 126:
		while lv_check <= lv_lines:
			for lv_index in range(1, lv_check+1):
				print(str(lv_rows), end = " ")
			print()
			lv_check = lv_check + 1

#457 ---- Nu functioneaza ? ? ?
def SquaredMatrix():
	pv_input = input().split(" ")
	pv_inputSize = int(pv_input[0])
	pv_inputOutter = pv_input[1]
	pv_inputInner = pv_input[2]
	lv_builded_rows = 0
	lv_builded_lines = 0
	while lv_builded_lines <= pv_inputSize:
		for lv_index in range(0, pv_inputSize):
			if lv_builded_lines == 0 or lv_builded_lines == pv_inputSize or lv_index == 0 or lv_index == pv_inputSize-1:
				print(pv_inputOutter, end = " ")
			else:
				print(pv_inputInner, end = " ")
		print()
		lv_builded_lines = lv_builded_lines + 1

#2699
def PowersLessThanInput():
	pv_input = input().split(" ")
	pv_base = int(pv_input[0])
	pv_limit = int(pv_input[1])
	if 2<= pv_base <= 10 and 1<= pv_limit <= 1000000000:
		for lv_index in range(0, pv_limit):
			if pv_base ** lv_index <= pv_limit:
				print(pv_base**lv_index, end = " ")
			else:
				return

#350
def CartProd():
	pv_input = input().split(" ")
	pv_inputN = int(pv_input[0])
	pv_inputM = int(pv_input[1])
	A = []
	B = []
	if (1<= pv_inputN <= 10) and (1<= pv_inputM <= 10):
		for lv_index in range(pv_inputN):
			A.append(lv_index+1)
		for lv_index in range(pv_inputM):
			B.append(lv_index+1)

	print("{",end="")
	for lv_loop in A:
		for lv_inner_loop in B:
			if lv_inner_loop is not pv_inputM:
				print("({},{})".format(lv_loop, lv_inner_loop), end = ",")
			else:
				print("({},{})".format(lv_loop, lv_inner_loop), end = "}")
CartProd()