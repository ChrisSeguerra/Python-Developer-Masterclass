
income = float(input("What is your gross income per year? "))


if income < 10000:
  print("You are exempted from tax.")

else:
  if income <= 30000:
    total_taxed_income = (income * 20) / 100
    print(f"Your total taxed income will be {total_taxed_income}")
  
  if income <= 50000:
    total_taxed_income = (income * 35) / 100
    print(f"Your total taxed income will be {total_taxed_income}")


  if income > 50000:
    total_taxed_income = (income * 45) / 100
    print(f"Your total taxed income will be {total_taxed_income}")


