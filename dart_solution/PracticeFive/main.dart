import "practicefive.dart";


void main(){
  var bankAccount=BankManagementSystem("DBBL0012345");
  
  try{
    bankAccount.CreditedMoney(25000000);
    print("Amount credited successfully.");
  }catch(e){
    print("Error: $e");
    return;
  }
  bankAccount.displayBankInfo();
}