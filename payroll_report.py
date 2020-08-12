"""
    * Class: CS 3A
    * Description: Payroll Report is a program which gathers input from the
    *              user and does a set of comparisons and calculations to give
    *              a total statement regarding gross pay, federal taxes, state
    *              taxes, and fica taxes.
    * Due Date: July 13, 2020
    * Name: Sachi Bhatkar
    * File Name: payroll_report.py
"""

# declare 5 variables which will account for the total gross pay,federal,state and fica
total_gross = 0
total_federal = 0
total_state = 0
total_fica = 0

print("Enter the following information: \n")

# allow program to run while user enters a number which is NOT zero
while True:

    # prompt user to enter number, if it is zero, then terminate program
    employee_num = int(input("Employee Number (0 to quit): "))
    if employee_num == 0:
        break

    # if user enters negative number, send error message and
    # prompt till user enters a positive number
    if employee_num < 0:
        print("Employee Num can not be negative")
        employee_num = int(input("Re Enter Employee Number (0 to quit): "))
        while employee_num < 0:
            employee_num = int(input("Re Employee Number (0 to quit): "))

    # prompt user to enter a gross pay which isn't negative
    # convert it to float.
    gross_pay = float(input("Gross Pay: "))
    if gross_pay < 0.0:
        print("Gross Pay may not be less than 0");
        gross_pay = float(input("Re-Enter Gross Pay "))
        while gross_pay < 0:
            gross_pay = float(input("Re-Enter Gross Pay "))

    # prompt user to enter a federal pay which isn't negative
    # convert it to float.
    # make sure federal tax is less than gross pay, if not prompt proper response
    federal_with = float(input("Federal withholding: "))
    if federal_with < 0.0:
        print("Federal Withholding may not be less than zero")
        federal_with = float(input("Re-Enter federal withholding: "))
        while federal_with < 0:
            federal_with = float(input("Re-Enter federal withholding: "))
    if federal_with > gross_pay:
        print("Federal Withholding can not be greater than Gross Pay")
        federal_with = float(input("Re-Enter federal withholding: "))
        while federal_with > gross_pay:
            federal_with = float(input("Re-Enter federal withholding: "))

    # prompt user to enter a state pay which isn't negative
    # convert it to float.
    # make sure state tax is less than gross pay, if not prompt proper response
    state_with = float(input("State withholding: "))
    if state_with < 0.0:
        print("State withholding may not be less than zero")
        state_with = float(input("Re-Enter state withholding: "))
        while state_with < 0.0 :
            state_with = float(input("Re-Enter state withholding: "))
    if state_with > gross_pay:
        print("State withholding may not be greater than gross pay")
        state_with = float(input("Re-Enter state withholding: "))
        while state_with > gross_pay:
            state_with = float(input("Re-Enter state withholding: "))

    # prompt user to enter a fica pay which isn't negative
    # convert it to float.
    # make sure fica tax is less than gross pay, if not prompt proper response
    fica_with = float(input("FICA withholding: "))
    if fica_with < 0.0:
        print("FICA withholding may not be less than zero")
        fica_with = float(input("Re-Enter FICA withholding: "))
        while fica_with < 0:
            fica_with = float(input("Re-Enter FICA withholding: "))
    if fica_with > gross_pay:
        print("FICA Withholding may not be greater than Gross Pay")
        fica_with = float(input("Re-Enter FICA withholding: "))
        while fica_with > gross_pay:
            fica_with = float(input("Re-Enter FICA withholding: "))

    # Calculate sum of taxes, if its bigger than gross pay reenter
    # else, calculate total gross, total federal , total fica
    # and total state
    sum = federal_with + fica_with + state_with
    if sum > gross_pay:
        print("ERROR: Withholdings cannot exceed gross pay")
        print("Please re- enter the data for this employee: ")
    else:
        total_gross += gross_pay
        total_federal += federal_with
        total_fica += fica_with
        total_state += state_with
        print("\nProcessing next employee: ")

# at the end of program, print totals from ALL inputs
if employee_num == 0:
    print("\nTotal Gross: ${:.2f}".format(total_gross))
    print("Total Federal withholding: ${:.2f}".format(total_federal))
    print("Total State withholding: ${:.2f}".format(total_state))
    print("Total Fica withholding: ${:.2f}".format(total_fica))

