print("Wlcome to the tip calculator.")
totalBill = float(input("What was the total bill? $"))
percentageTip = int(input("What percentage tip would you like to give? 10, 12, o4 15? "))
numberOfPeople = int(input("How many people to split the bill? "))

pricePerPerson = (totalBill*(1 + percentageTip/100))/ numberOfPeople

print(f"Each person should pay: ${round(pricePerPerson, 2)}")