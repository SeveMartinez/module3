#Calculates a French loan
capital = float(input("Inout Capital:"))
interes = float(input("Interest:"))
years = int(input("How many years:"))
n = 1
paidout=0
while n <= years:
    quota = capital * ( (interes/100 * pow(1 + interes/100, years) ) / ( pow(1+interes/100,years) - 1) )
    paidout += quota
    print("Year", n,"Quota",quota,"Paid out",paidout)
    n += 1



