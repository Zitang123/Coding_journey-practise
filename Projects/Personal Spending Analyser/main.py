
transactions = []

stopping = False

while not stopping:
    merchant = input("Enter merchant: ")

    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Must enter number")
    
    category = input("Enter category: ")


    transaction = {"merchant" : merchant, "amount" : amount, "category" : category}

    transactions.append(transaction)

    decision = input("Continue or Stop: ").lower()
    
    if decision == "stop":
        stopping = True

total_amount = 0

num = len(transactions)

for transaction in transactions:

    print(f"{transaction["merchant"]} - £{transaction["amount"]:.2f} - {transaction["category"]}")

    total_amount += transaction["amount"]

average_amount = total_amount / num

print(f"Total number of transactions: {num}")
print(f"Total amount spent: £{total_amount:.2f}")
print(f"Average amount spent: £{average_amount:.2f}")
    

