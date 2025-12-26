

class BankManagementSystem :



    def __init__(self,bank_name):

        self.bank_name = bank_name 
        self.user_accounts = {}
        self.total_balance = 0 


    # Here We implement supporting class methods 


    def is_account_exist(self,account_number):
        return account_number in self.user_accounts





    # Here We implement main class methods 

    def add_user_account(self,account_number,account_holder_name,initial_deposit):

        if account_number in self.user_accounts:
            raise Exception("this account number is already exist in this bank")
        
        self.user_accounts[account_number] = {
            'account_holder_name': account_holder_name,
            'balance': initial_deposit
        }

        self.total_balance += initial_deposit

    def deposit_amount(self,account_number,amount):

        if not self.is_account_exist(account_number):
            raise Exception('please ensure that this account number is exist in this bank')
        
        account_info = self.user_accounts[account_number]

        account_info['balance'] += amount
        self.total_balance += amount

    def withdraw_amount(self,account_number,amount):

        if not self.is_account_exist(account_number):
            raise Exception('please ensure that this account number is exist in this bank')
        
        account_info = self.user_accounts[account_number]

        if account_info['balance'] < amount:
            raise Exception('insufficient balance in the account')
        
        account_info['balance'] -= amount
        self.total_balance -= amount

    def transfer_amount(self,sender_user_account,receiver_user_account,amount):

        if not self.is_account_exist(sender_user_account):
            raise Exception('please ensure that the sender account number is exist in this bank')
        
        if not self.is_account_exist(receiver_user_account):
            raise Exception('please ensure that the receiver account number is exist in this bank')
       

        self.withdraw_amount(sender_user_account,amount)
        self.deposit_amount(receiver_user_account,amount)

    def get_account_balance(self):

        return self.total_balance 
    

if __name__ == "__main__":
    bank = BankManagementSystem("Global Bank")

    bank.add_user_account("123456", "Md.Rahim Uddin", 1000)
    bank.add_user_account("654321", "Farhan Kabir", 500)

    bank.deposit_amount("123456", 500)
    print(bank.user_accounts["123456"]['balance'])  # Output: 1500
    bank.withdraw_amount("654321", 200)
    print(bank.user_accounts["654321"]['balance'])  # Output: 300
    bank.transfer_amount("123456", "654321", 300)
    print(bank.user_accounts["123456"]['balance'])  # Output: 1200  
    print(bank.user_accounts["654321"]['balance'])  # Output: 600   

    print(f"Total balance in the bank: {bank.get_account_balance()}")  # Output: 1800 

    
