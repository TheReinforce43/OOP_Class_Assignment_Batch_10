from datetime import date 
class UssCreditCard:

    def __init__(self, card_number, expiry_date,credit_limit=500_000):

        if not card_number.isdigit():
            raise ValueError("Card number must be numeric")
    

        self.card_number = card_number
        
        self.expiry_date = expiry_date
        
        self.credit_limit = credit_limit
        self.spend_balance = 0 

    def is_max_limit_reached(self, amount):

        if self.spend_balance + amount > self.credit_limit:
            return True
        return False


    def make_payment(self, amount):
       today = date.today()
       expiry = date.fromisoformat(self.expiry_date) 

       if today > expiry:
              raise Exception("Card has expired")
       
       if self.is_max_limit_reached(amount):
              raise Exception("Credit limit exceeded")
       
       self.spend_balance += amount

    def get_available_credit(self):
        return self.credit_limit - self.spend_balance
    
    def get_spend_balance(self):
        return self.spend_balance   
       



class BankUserProfile:

    credit_limit = 500_000


    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
        self.credit_card = None

    def add_credit_card(self,card):

        if self.credit_card:
            raise Exception("User already has a credit card") 
        self.credit_card = card




if __name__ == "__main__":
    card = UssCreditCard("1234567890123456", "2025-12-31")
    card2 = UssCreditCard("1234567423234345", "2026-12-31")
    user = BankUserProfile("Md.Rahim Uddin", 30, 1000000)    

    user.add_credit_card(card)
    print(f"Available credit: {user.credit_card.get_available_credit()}")
    user.credit_card.make_payment(200000)
    print(f"Available credit after payment: {user.credit_card.get_available_credit()}")

  
    user.add_credit_card(card2)  # This should raise an exception






