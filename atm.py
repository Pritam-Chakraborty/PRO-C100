class Atm(object):
    def __init__(self,atmCardNumber,pinNumber):
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber
    
    def withdrawl(self):
        print("Your Cash is being withdrawled")

    def deposit(self):
        print("Depositing Cash")
