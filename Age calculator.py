def age_calc():
    print("Hello! Welcome to my age calculator :) ")
    intro = int(input("Enter the year you were born in: "))
    curr_year = int(2022)
    if intro < curr_year:
        curr_year = curr_year - intro
        print("Your current age is", curr_year)
    else:
        print("You are too old!")
age_calc()
