age = int(input("what is your age: "))
year = 90 - age
month = (90*12) - (age*12)
days = (90*365) - (age*365)
weeks = (90*52) - (age*52)
print(f"you have {days} days,{month} month,{year} years left and {weeks} weeks left.")