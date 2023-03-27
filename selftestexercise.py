name = input("Please enter your name: ")
year_of_service = int(input("Enter your year of service: "))
salary = int(input("Enter your salary: "))
net_bonus = 0

if(year_of_service > 5):
    net_bonus = salary * (5 / 100)
    print("Employee name is: ", name)
    print("Employee salary is: ", salary)
    print("Employee year of service is : ", year_of_service)
    print("Congratulations your Net Bonus is: ", net_bonus)
else:
    print("Employee name is: ", name)
    print("Employee salary is: ", salary)
    print("Employee year of service is : ", year_of_service)
    print("Sorry, You don't qualify for the 5% Net Bonus this time")
