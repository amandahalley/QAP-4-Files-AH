# Description: A program to enter and calculate new insurance policy information for the One Stop Insurance Company customers.
# Author: Amanda Halley
# Date(s): March 18, 2024 - 

# Import libraries
import datetime
import FormatValues as FV
import time 
import sys
import Functions as FN

# Define progarm constants.
f = open("defaults.dat", "r")
POLICY_NUM = int(f.readline())
BASIC_PREM_RATE = float(f.readline())
ADD_CAR_DISCOUNT = float(f.readline())
EXTRA_LIABILITY_RATE = float(f.readline())
GLASS_COVERAGE_RATE = float(f.readline())
LOANER_CAR_RATE = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())
f.close()

CurDate = datetime.datetime.now()


allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
allowed_num = set("1234567890")
allowed_address_char = set("1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
allowed_postal_char = set("1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ProvLst = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]
Paylst = ["Full", "Monthly"]



# Main program.
while True:

     # Gather user input.
    while True:
        CustfirstName = input("Enter the customers first name: ").title()
        if CustfirstName == "":
            print("Data entry error - customers first name can not be blank.")
        elif set(CustfirstName).issubset(allowed_char) == False:
            print("Data entry error - Customers first name contains invalid characters.")
        else:
            break

    while True:
        CustLastName = input("Enter the customers last name: ").title()
        if CustLastName == "":
            print("Data entry error - customers last name can not be blank.")
        elif set(CustLastName).issubset(allowed_char) == False:
            print("Data entry error - Customers last name contains invalid characters.")
        else:
            break

    while True:
        Address = input("Enter the customers address: ").title()
        if Address == "":
            print("Data entry error - Address can not be blank.")
        elif set(Address).issubset(allowed_address_char) == False:
            print("Data entry error - Address contains invalid characters.")
        else:
            break

    while True:
        City = input("Enter the city: ").title()
        if City == "":
            print("Data entry error  - City can not be blank")
        elif set(City).issubset(allowed_char) == False:
            print("Data entry error - City can not be blank.")
        else:
            break

    
    while True:
        Prov = input("Enter the province (XX): ").upper()
        if Prov == "":
            print("Data entry error - province can not be blank.")
        elif len(Prov) != 2:
            print("Data entry error - province must be 2 characters only")
        elif Prov not in ProvLst:
            print("Data entry error - Invalid province.")
        else: 
            break

    while True:
        PostalCode = input("Enter the postal code (X9X9X9): ").upper()
        if PostalCode == "":
            print("Data entry error - Postal code can not be blank.")
        elif set(PostalCode).issubset(allowed_postal_char) == False:
            print("Data entry error - Postal code contains invalid characters.")
        elif len(PostalCode) != 6:
            print("Data Entry Error - Invalid postal code, must be 6 characters.")
        else:
            break
    
    while True:
        PhoneNum =  input("Enter the customers phone number (9999999999): ")
        if PhoneNum == "":
            print("Data entry error - Phone Number cannot be blank.")
        elif len(PhoneNum) != 10: 
            print("Data entry error - Phone number must be 10 digits only.")
        elif PhoneNum.isdigit() == False: 
            print("Data Entry Error - Phone number must be digits only.")
        else:
            break

    while True:
        NumCarsIns = int(input("Enter the number of cars being insured: "))
        if NumCarsIns == "":
            print("Data entry error - Number of cars being insured can not be blank.")
        else: 
            break

    while True:
        ExtLiability = input("Enter if the customer wants extra liability (Y/N): ").upper()
        if ExtLiability == "":
            print("Data entry error - Extra liability option can not be blank.")
        elif ExtLiability != "Y" and ExtLiability != "N":
            print("Data entry error = Extra liability must be entered as Y or N only.")
        else: 
            break
    
    while True:
        GlassCvrg = input("Enter if the customer wants glass coveage (Y/N): ").upper()
        if GlassCvrg == "":
            print("Data entry error - Glass coverage option can not be blank.")
        elif GlassCvrg != "Y" and GlassCvrg != "N":
            print("Data entry error = Glass coverage must be entered as Y or N only.")
        else: 
            break

    while True:
        LoanerCar = input("Enter if the customer opts for a loaner car (Y/N): ").upper()
        if LoanerCar == "":
            print("Data entry error - Loaner car option can not be blank.")
        elif LoanerCar != "Y" and LoanerCar != "N":
            print("Data entry error = Loaner car option must be entered as Y or N only.")
        else: 
            break

   
    DownPayAmt = 0
    while True:
        while True:
            PayMethod = input("How do you want to pay? (Full, Monthly): ").title()
            if PayMethod == "":
                print("Data entry error - Payment method can not be blank.")
            elif PayMethod not in Paylst:
                print("Data entry error - Invalid payment method.")
            else:
                break
    
        DownPay = input("Do you want to make a down payment? (Y/N): ").upper()
        if DownPay == "Y":
            while True:
                DownPayAmt = input("Enter the down payment amount: ")
                if DownPayAmt == "":
                    print("Data entry error - Down payment amount can not be blank.")    
                else:
                    DownPayAmt = float(DownPayAmt)
                    break
        break

        


    #Program functions/calculations.
    InsPremium = FN.CalculatePremium(NumCarsIns, BASIC_PREM_RATE, ADD_CAR_DISCOUNT)

    ExtraCosts = FN.CalculateExtraCosts(NumCarsIns, ExtLiability, GlassCvrg, LoanerCar, EXTRA_LIABILITY_RATE, GLASS_COVERAGE_RATE, LOANER_CAR_RATE)

    TotalInsPremium = ExtraCosts + InsPremium
    
    HST = FN.CalculateHST(TotalInsPremium, HST_RATE)    

    TotalCost = HST + TotalInsPremium

    MonthlyPay = FN.CalcMonthPay(PayMethod, TotalCost, PROCESSING_FEE, DownPayAmt)   

    InvDate = FN.GetInvDate()

    FirstPayDate = FN.CalcFirstPayDate(CurDate)

    if ExtLiability== "Y":
        ExtLiability= "Yes"
    else:
        ExtLiability = "No"

    if GlassCvrg == "Y":
        GlassCvrg= "Yes"
    else:
        GlassCvrg = "No"

    if LoanerCar == "Y":
        LoanerCar = "Yes"
    else:
        LoanerCar = "No"

    if DownPay == "Y":
        DownPay = "Yes"
    else:
        DownPay = "No"

    Claims = FN.GetClaims()
    FN.SaveClaims(Claims, "Claims.txt",POLICY_NUM, CustfirstName, CustLastName, PhoneNum, Address, City, Prov, PostalCode, NumCarsIns, ExtLiability, GlassCvrg, LoanerCar, PayMethod, DownPay, TotalInsPremium)

    

    # Display results
    print()
    print("-----------------------------------------------------------")
    print("                One Stop Insurance Policy")
    print("-----------------------------------------------------------")
    print()
    CurDateDsp = FV.FDateS(CurDate)
    print(f"Policy Number: {POLICY_NUM}                        Date: {CurDateDsp:>10s}")
    print(f"Customer Name: {CustfirstName} {CustLastName}          First Pay: {FV.FDateS(FirstPayDate):>10s}")
    print()
    print(f"Address: ")
    print("---------")
    print(f"{Address}")
    print(f"{City}, {Prov} {PostalCode}")
    print(f"Phone Number: {PhoneNum}")
    print()
    print("-----------------------------------------------------------")
    print()
    print(f"                          ADD-ONS")
    print("                         ---------")
    print(f"          Number of Cars:                     {NumCarsIns:>2d}")
    print(f"          Extra Liability Coverage:          {ExtLiability:>3s}")
    print(f"          Glass Coverage:                    {GlassCvrg:>3s}")
    print(f"          Loaner vehicle:                    {LoanerCar:>3s}")
    print()
    print("-----------------------------------------------------------")
    print()
    print("                    PAYMENT INFORMATION")
    print("                   ---------------------")
    print()
    print(f"          Payment Method:                {PayMethod}")
    if DownPay != "N":
        print(f"          Down Payment Amount:         {FV.FDollar2(DownPayAmt):>9s}")
    print(f"          Add-on Costs:                {FV.FDollar2(ExtraCosts):>9s}")
    print(f"          Insurance Premium rate:      {FV.FDollar2(TotalInsPremium):>9s}")
    print(f"          HST:                         {FV.FDollar2(HST):>9s}")
    print(f"          -----------------------      ---------")
    print(f"          Total Cost:                  {FV.FDollar2(TotalCost):>9s}")
    print()
    print(f"          Monthly Payment:             {FV.FDollar2(MonthlyPay):>9s}")
    print()
    print("-----------------------------------------------------------")
    print()
    print("                     PREVIOUS CLAIMS")
    print("                    -----------------")
    print()
    print("   Claim #    |        Claim Date       |    Claim Amount")
    print("-----------------------------------------------------------")
    print()
    for Claim in Claims:
        print(f"    {Claim[0]}              {FV.FDateS(Claim[1]):>10s}             {FV.FDollar2(Claim[2]):>9s}")
    print()
    print("-----------------------------------------------------------")
    print("                       Thank you!")
    print("-----------------------------------------------------------")




    

    for _ in range(4):  
        print('Saving claim data ...', end='\r')
        time.sleep(.3)  
        sys.stdout.write('\033[2K\r')  
        time.sleep(.3)
    print()
    print("Claim data successfully saved ...", end='\r')
    print()
    time.sleep(1.5)  
    sys.stdout.write('\033[2K\r') 
    POLICY_NUM += 1

    # clear the file
    AddCustomer = input("Would you like to add another customer? (Y/N): ").upper()
    if AddCustomer != "Y" and AddCustomer != "N":
        print("Data entry error = Loaner car option must be entered as Y or N only.")
    elif AddCustomer == "":
        print("Data entry error - Must enter Y or N.")
        break
    if AddCustomer == "N":
        print()
        print("Thank you for using the One Stop Insurance Progam!")
        print()
        break

    


# Housekeeping.
