import 'practiceFour.dart';


void main() {
  var person1 = BankAccount('test bank account',"Ar234234", 50000, Gender.Male);
  var person2 = BankAccount('test bank account2',"Ar234235", 50000, Gender.Female);
  person1.Deposit(1000);
  person1.Withdraw(500);
  person1.Transfer(100, person2);
  person1.DisplayAccountInfo();
  person2.DisplayAccountInfo();
}