
class BankManagementSystem{
  final String bankName="Dutch Bangla Bank Limited";
  final double  max_withdraw_limit=500000;
  final double max_days_transfer_limit=1000000;
  final double per_transaction_limit=200000;
  double total_daily_withdraw=0;
  double total_withdraw_amount=0;

  String  accountId;


  BankManagementSystem(this.accountId);


  void CreditedMoney(double amount){
    if(isNegativeBalance(amount)){
        throw("Amount can not be negative");
    }
    if(IsExceedLimit(amount))
        throw("Amount exceeds per transaction limit");

    if(!IsAvailableDailyTransferLimit(amount))
        throw("Amount exceeds daily transfer limit");
        
    total_withdraw_amount += amount;
  }


  


  bool isNegativeBalance(double amount){
    return amount<0;
  }


  bool IsExceedLimit(double amount){
    return per_transaction_limit< amount;
  }


  bool IsAvailableDailyTransferLimit(double amount){
    return (total_daily_withdraw + amount) <= max_days_transfer_limit;
  }


  void displayBankInfo(){
    print("Bank Name: $bankName");
    print("Max Withdraw Limit: $max_withdraw_limit");
    print("Max Daily Transfer Limit: $max_days_transfer_limit");
    print("Per Transaction Limit: $per_transaction_limit");
    print("Account ID: $accountId");
  }


}