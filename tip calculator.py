
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇


print("Welcome to the tip calculator!")

bill = float (input ("What was the total bill? $"))
amount_of_tip = float(input("How much tip wolud you like to give? 10 , 12 or 15? "))
split = float(input("How many people to split the bill? "))


total_tip = ( bill * amount_of_tip )/100
final_bill = (bill + total_tip)
split_bill = "{:.2f}".format(final_bill/split) 

print(f"Each person should pay {split_bill}")





