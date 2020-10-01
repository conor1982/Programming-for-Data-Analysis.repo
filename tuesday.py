import datetime

today = datetime.datetime.today()
dayofweek = today.weekday()

print("Lets check if it is Tuesday.")

if dayofweek == 1:
    print("It's Tuesday")
elif dayofweek == 0:
    print("It's not Tuesday, it is Monday!")
    print("Luckily it will be Tuesday tomorrow!")

else:
    print("Unfortunatley, It is not Tuesday")

print("Thanks for checking if it's Tuesday")

