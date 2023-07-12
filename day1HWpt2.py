int1 = float(input("Give me a random whole number.  "))
minutesOrHours = input("Would you like a conversion to minutes or hours from your original number? ('min' or 'hour')")
if minutesOrHours == "min":
    ans = int1*60
    print("Your conversion from hours to minutes is ", ans)
elif minutesOrHours == "hour":
    ans = int1/60
    print("Your conversion from minutes to hours is ", ans)
else:
    print("Invalid answer")