acctNum = input("Please enter your account number: ")
acctBal = float(0)
if acctNum == "0720076154":
	acctBal = 50000.00
	print("Welcome to VSONET Bank, userOne\nYour account balance is NGN50,000.00")
elif acctNum == "1040089238":
	acctBal = 8500.00
	print("Welcome to VSONET Bank, userTwo\nYour account balance is NGN8,500.00")
elif acctNum == "2050643519":
	acctBal = 980.00
	print("Welcome to VSONET Bank, userThree\nYour account balance is NGN980.00")
else:
	print("Invalid account number!!!")

if (acctNum == "0720076154" or acctNum == "1040089238" or acctNum == "2050643519"):
	withdrawAmt = float(input("Please enter the amount you wish to withdraw: NGN"))
	if withdrawAmt <= acctBal:
		newAcctBal = acctBal - withdrawAmt
		print("Transaction successful\nYour new account balance is",newAcctBal)
	elif withdrawAmt > acctBal:
		print("Oops, insufficient funds")
	query = input("Do you wish to perform another transaction?")
	


