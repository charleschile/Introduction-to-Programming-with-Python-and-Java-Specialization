import traceback

def calculator():
    
    # Get dog age
    age = input("Input dog years: ")

    try:
        # Cast to float
        d_age = float(age)

        # If user enters negative number, print message
        # Otherwise, calculate dog's age in human years
        # your code here
        if d_age < 0:
            print("Age cannot be a negative number.")
            return
        elif d_age <= 1:
            human_age = 15 * d_age
        elif d_age <=2:
            human_age = 12 * d_age
        elif d_age <=3:
            human_age = 9.3 * d_age
        elif d_age <=4:
            human_age = 8 * d_age
        elif d_age <=5:
            human_age = 7.2 * d_age
        else:
            human_age = 36 + (d_age - 5) * 7 
        h_age = round(human_age, 2)
        print("The given dog age " + str(d_age) + " is " + str(h_age) + " in human years.")

    except ValueError as e:
        print(age, "is an invalid age.")
        print(traceback.format_exc())
    
calculator() # This line calls the calculator function
