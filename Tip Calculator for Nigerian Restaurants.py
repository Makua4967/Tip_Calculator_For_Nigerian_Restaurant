print("Welcome to the tip calculator!")
total_bill= input("What was the total bill? N")
tip_to_give= input("How much tip would you like to give? 10, 12, or 15? ")
people_to_split_bill= input("How many people to split the  bill? ")
tip_perc= (int(tip_to_give)/100)*float(total_bill)
complete_total=tip_perc+float(total_bill)
payment= complete_total/float(people_to_split_bill)
result= round(payment, 2)
result= "{:.2f}".format(payment)
print(f"Each person should pay: N{result}")

