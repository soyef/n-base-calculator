
class DoCalculations:
	def checkValidNumber(self,txtBase1,txtNumber1):
		#txtNumber1 = list(txtNumber1)
		flag = 0
		max = -1

		for i in range(0,len(txtNumber1)):
			if ord(txtNumber1[i]) >=65 and ord(txtNumber1[i]) <=90:
				if i != len(txtNumber1)-1 and (ord(txtNumber1[i+1]) >=97 and ord(txtNumber1[i+1]) <=122):
					if (((ord(txtNumber1[i])-64) - 1)*26 + ord(txtNumber1[i+1]) - 96 + 35) > max:
						max = ((ord(txtNumber1[i])-64) - 1)*26 + ord(txtNumber1[i+1]) - 96 + 35
				else:
					return flag

		for i in range(0,len(txtNumber1)):
			if ord(txtNumber1[i]) >=97 and ord(txtNumber1[i]) <=122:
				if ord(txtNumber1[i]) - 96 + 9 > max:
					max = ord(txtNumber1[i]) - 96 + 9

		for i in range(0,len(txtNumber1)):
			if ord(txtNumber1[i]) >=48 and ord(txtNumber1[i]) <=57:
				if ord(txtNumber1[i]) - 48 > max:
					max = ord(txtNumber1[i]) - 48

		if int(txtBase1) > max:
			flag = 1
		else:
			flag = 0

		return flag


	def convertToBase10(self,number,base):
		length = 0
		for i in range(0,len(number)):
			if ord(number[i]) >=65 and ord(number[i]) <=90:
				length-=1
			length+=1
		i=0	
		power = length-1
		num = 0
		while i<len(number):
			if ord(number[i]) >=48 and ord(number[i]) <=57:
				num += (ord(number[i]) - 48) * (int(base) ** power)
				power-=1

			if ord(number[i]) >=97 and ord(number[i]) <=122:
				num += (ord(number[i]) - 96 + 9) * (int(base) ** power)
				power-=1


			if ord(number[i]) >=65 and ord(number[i]) <=90:
				next = (ord(number[i])-64-1)*26 + ord(number[i+1]) - 96 + 35
				num += (next * (int(base) ** power))
				power-=1
				i+=1
			i+=1
		return num

	def ConvertBase10ToN(self,number,base):
		convert=[]
		i=0
		if int(number) == 0:
			convert.append(0)
		while(int(number)>0):
			rem = int(number) % int(base)
			if rem >=0 and rem <= 9:
				convert.append(rem)
			elif rem>=10 and rem <= 35:
				convert.append(chr(rem + 87)) 
			elif rem>35 and rem<712:
				rem = rem - 35
				quo = rem/26
				if quo == 26:
					temp = chr(quo + 64)
				else:
					temp = chr(quo + 65)
				temp2 = rem % 26
				if temp2 == 0:
					temp2 = 'z'
				else:
					temp2 = chr(temp2 + 96)
				convert.append(temp2)
				convert.append(temp)

			number=int(number)/int(base)
		convert.reverse()
		return convert[:]


