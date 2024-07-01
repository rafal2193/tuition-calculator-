#Rafal Krauze
#June 23,2024
#CMP 131
#Chapter 4 Lab Working with loops, to create a tuition caculator
# This program prints a table displaying increases in tuition at 4% per year
# The user enters the starting tuition and how many years to display on the table,
#with the option to create another table until they indicate they are done.
#I hereby attest that this code is original and written by me alone. I understand that I risk a penalty for violating the Academic Integrity policy at CCM


# Use a constant for the increase per year
INCREASE_PER_YEAR = .04

#Prime the loop to always runs at least once
again = 'y'

#Start the loop by testing the value of the again variable to see if it is 'y'
while again == 'y':

    #Print a blank line for space
    print()
    
    #Ask the user for a tuition starting amount. Remember - It must be numeric!
    tuition = float(input('Enter starting tuition: '))

    #Validate that the user input is at least $3,000 and less than $100,000
    while tuition < 3000 or tuition > 100000:

        #The test is true so print an error message
        print("Error!  The tuition starting amount must be between $3,000 and $100,000")

        #Have the user re-enter the starting amount.  You must change what you test inside the loop!
        tuition = float(input("Enter starting tuition:  "))


    #Set the first year in the table to be 2024
    start_year = 2024

    #Ask the user for the number of years to show on the table. Remember! It must be numeric!
    num_years = int(input("Table starts in 2024.  How many years (4-10) do you want displayed on the table? "))

    #Validate that the user input is at least 4 years and no more than 10
    while num_years < 4 or num_years > 10:

        #The test is true so print an error message
        print("Error!  The table can only contain 4-10 years!")

        #Have the user re-enter the starting amount.  You must change what you test inside the loop!
        num_years = int(input("Table starts in 2024.  How many years (4-10) do you want displayed on the table? "))

    #Calculate the end year based on how many the user wants to see
    end_year = start_year + num_years

    # Print the table header
    print ('Year\t Projected Tuition')
    print ('------------------------------------------')

    #Print the chart showing the user requested number of years of the tuition increases each year
    #Remember that the table should start with 2024!
    for year in range( start_year , end_year ):
        tuition += (tuition * INCREASE_PER_YEAR)
        print (f'{year}\t${tuition:,.2f}')

    #Print blank lines for spacing
    print()
    print()
    
    #See if the user wants to create another table
    again = input("Would you like to create a new table? (y/n): ")

#Program ends when again is not 'y'
print("Thank you for using the tuition calculator!")
