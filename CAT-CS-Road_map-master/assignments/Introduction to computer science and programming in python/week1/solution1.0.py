 
 
 
 
 
 
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi annual raise as decimal: "))


portion_down_payment = 0.25
r = 0.04;
monthly_salary = annual_salary / 12


saving = 0
months = 0

while(saving < total_cost * portion_down_payment):
    saving += (saving*r/12) + (monthly_salary*portion_saved)
    months+=1
    if months%6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12


print("Number of Months: ", months)
