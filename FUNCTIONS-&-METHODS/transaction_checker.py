
BALANCE = 10000

transaction_amount = int(input("What is the sum of the transaction? "))

if transaction_amount < 0:
    print("Error: Transaction amount must be greater than zero.")
else:
    if transaction_amount <= BALANCE:
        print("Proceed to transaction")
    else:
        print("Transaction has been cancelled due to lack of BALANCE.")    