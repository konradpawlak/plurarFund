temp = 90
forecast_temp = int(input("What is the temp outside?\n"))
forecast_sun = input("Is it sunny today?\n")
forecast_rain = input("Does it rain?\n")

if forecast_temp > 28:
    print("Too hot bro, stay home")
elif forecast_temp < 20:
    print("Cold as heck yoo, stay home brah")
else:
    print("Get ya stuff ready, we going hikin rn!")