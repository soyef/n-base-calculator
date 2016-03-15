from django.shortcuts import render
from .calculate import DoCalculations

# Create your views here.
def home(request):
	message1= ""
	message2= ""
	base1= ""
	base2= ""
	base3 = ""
	number1= ""
	number2 = ""
	result = ""
	flag = 0
	if request.method == "POST":
		 base1 = request.POST["txtBase1"]
		 base2 = request.POST["txtBase2"]
		 number1 = request.POST["txtNumber1"]
		 number2 = request.POST["txtNumber2"]
		 operation = request.POST["dropdown"]
		 base3 = request.POST["txtBase3"]

		 doCalculations = DoCalculations()
		 if doCalculations.checkValidNumber(base1,number1) == 0:
		 	message1 = "Enter correct number"
		 	flag = 1

		 if doCalculations.checkValidNumber(base2,number2) == 0:
		 	message2 = "Enter correct number"
		 	flag = 1

		 if flag == 0:
		 	num1 = doCalculations.convertToBase10(number1,base1)
		 	num2 = doCalculations.convertToBase10(number2,base2)
		 	if operation == "Add":
		 		result = num1 + num2
		 	 	result = doCalculations.ConvertBase10ToN(result,base3)
		 	elif operation == "Subtract":
		 		if num1 >= num2:
			 		result = num1 - num2
			 	 	result = doCalculations.ConvertBase10ToN(result,base3)
			 	else:
			 	 	result = "Number1 < Number2"
		 	elif operation == "Multiply":
		 		result = num1 * num2
		 	 	result = doCalculations.ConvertBase10ToN(result,base3)
		 	result = ''.join(map(str, result))

	context = {
		"message1":message1,
		"message2":message2,	
		"base1": base1,
		"base2" : base2,
		"number1":number1,
		"number2":number2,
		"result" :result,
	}
	return render(request,"home.html",context)
