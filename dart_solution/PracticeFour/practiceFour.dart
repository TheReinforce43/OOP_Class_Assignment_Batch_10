enum Gender{
    Male,
    Female,
    Others
}

class BankAccount{
    final String _bankName="Dutch Bangla Bank Limited";
    String ? AccountName;
    String ? AccountNumber;
    double ?balance;
    Gender ? gender; 

    BankAccount(this.AccountName, this.AccountNumber, this.balance, this.gender);


    void Deposit(double amount){

        if(isNegativeBalance(amount)){
            throw("Amount can not be negative");
        }
        balance = balance! + amount;

    }

    void Withdraw(double amount){
        
        if(isNegativeBalance(amount)){
            throw("Amount can not be negative");
        }

        if(!IsAvailableBalance(amount)){
            throw("Insufficient Balance");
        }
        balance = balance! - amount;


    }

    void Transfer(double amount , BankAccount toAccount){

        if(isNegativeBalance(amount)){
            throw("Amount can not be negative");
        }
        if(!IsAvailableBalance(amount)){
            throw("Insufficient Balance");
        }
         Withdraw(amount);
        toAccount.Deposit(amount);

    }
    void DisplayAccountInfo(){

        print("Bank Name: $_bankName");
        print("Account Name: $AccountName");
        print("Account Number: $AccountNumber");
        print("Balance: $balance");

    }

    bool isNegativeBalance(double amount){
        return amount<0;
    }

    bool IsAvailableBalance(double amount){

        return amount<= balance!;
    }

}

