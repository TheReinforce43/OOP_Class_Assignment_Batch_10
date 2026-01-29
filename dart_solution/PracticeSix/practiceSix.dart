class VoterCard{


    final String VoterId;
    final String Country='Bangladesh';

    VoterCard._internal(this.VoterId);

    factory VoterCard(String id){

        if (id.length != 17) {
            throw ArgumentError("Invalid Voter ID");
        }
        return VoterCard._internal(id);
    }  

}


class Employee{
    final String Name;
    final DateTime JoiningDate;
    final DateTime DateOfBirth;
    final total_leave_days=20;
    int used_leave_days=0;
    VoterCard ? voterCard;


    Employee(this.Name, this.JoiningDate,this.DateOfBirth); 

    void applyLeave(int days){
    
      if(IsExceedLeaveDays(days)){
        throw Exception("Leave days exceeded");
         
      }
      else{
        used_leave_days += days;
      }

    }

    int yearOfExperience(){
        return DateTime.now().year - JoiningDate.year;
    }

    bool IsExceedLeaveDays (int days){
        if(used_leave_days + days >total_leave_days) return true;
        return false;
    }


}