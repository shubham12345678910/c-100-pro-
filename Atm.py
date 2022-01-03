class atm(object):
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        
    def balanceinquiry(self):
        print("your balance in 50,000,000,00/")
    def cashwidrawal(self,amount):
        new_amount = 10,000-amount
        print ("You withdrawed: " + str(amount)) + "Your remaining balance is: " + str(new_amount)

def main():
    name  = input("hello what is your namer ")
    print("Hello," + name)
    cardnumber = input("Insert your card number :")
    pin = input(" Enter your pin")
    new_user = atm(cardnumber,pin)

    print("Choose your activity")
    print("1. Balance Inquiry")
    print("2. Cash Widthdrawal")
    activity = int(input(" Enter activity choice:"))
         
    if (activity == 1):
        new_user.balanceinquiry()
    elif (activity == 2):
          amount = int(input("Enter the amount:"))
          new_user.cashwidthdrawal(amount)
    else:
            print("Enter a valid number")
if __name__ == "_main_":
   main()