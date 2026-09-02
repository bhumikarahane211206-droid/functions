def calculate_bill(amount,discount=0):
    final = amount-(amount*discount/100)
    print("final amount: rs.",final)


calculate_bill(500)
calculate_bill(500,20)