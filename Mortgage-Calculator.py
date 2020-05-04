principle = int(input("Please enter the loan amount: \n"))

years = int(input("Please enter how many years the loan will last: \n"))

rate = 1+(.01*float(input("Please enter the yearly interest rate: \n")))

perMonth = 12
homeOwnerIns = 1741
propertyTax = 1448
def mortgageAmount(principle,years,rate,perMonth,homeOwnerIns,propertyTax):
    return ((principle/years)*(rate)+homeOwnerIns+propertyTax)/12
mortgageAmount(principle,years,rate,perMonth,homeOwnerIns,propertyTax)