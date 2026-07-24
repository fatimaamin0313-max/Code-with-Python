print("Welcome to number Analyzer")
Number = float(input("Enter Number"))
print("==========Analyze Number=========")
if Number > 0:
	Status = "+ive"
elif Number < 0:
	Status = "-ive"
else:
	Status = "0"
print("Number Type:", Status)

Square = Number **2
Cube = Number **3
print("Square:", Square)
print("Cube:", Cube)

Absolte_Value = abs(Number)
print("Absolte Value:", Absolte_Value)

if Number > 0:
	print("Half:", Number/2)
	print("Double:", Number/2)

print("========")