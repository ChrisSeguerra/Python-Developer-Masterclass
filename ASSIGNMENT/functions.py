
# Dollarizer
def dollarizer(word):
    return word.replace("s", "$")

input_word = "testcase"
output_word = dollarizer(input_word)
print(f"Dollarizer: {output_word}")
print()


# Eurizer
def eurizer(word2):
    return word2.replace("e", "€")

input_word = "testcase"
output_word = eurizer(input_word)
print(f"Eurizer: {output_word}")
print()


# Replacer
def replacement(word3):
    return word3.replace("s", "$").replace("e", "€").replace("l", "£")

input_word = "testcase"
output_word = replacement(input_word)
print(f"Replacer: {output_word}")
print()

# Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

print(f"Celsius to Fahrenheit: {convert_to_fahrenheit(25)}")


# Age_In_Days
def age_in_days(age):
    return age * 365

print(f"Age in Days: {age_in_days(25)}")


# Simple Interest
def simple_interest(principal, interest_rate, time):
    return principal * interest_rate * time
print(f"Simple Interest: {simple_interest(1000, 0.05, 5)}")


# Plan Finances
def plan_finances(principal, rate, time, final_amount):
    simple_interest = principal * (1 + rate * time)

    if simple_interest >= final_amount:
        return True
    else:
        return False
print(f"Plan Finances: {plan_finances(1000, 0.05, 5, 8000)}")
print()



