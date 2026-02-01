import "practiceSix.dart";

void main() {
  var employee = Employee(
    "John Doe",
    DateTime(2015, 6, 15),
    DateTime(1990, 4, 20),
  );

  try {
    var voterCard = VoterCard("12345678901234567");
    employee.voterCard = voterCard;
    print("Voter Card assigned successfully.");
  } catch (e) {
    print("Error: $e");
    return;
  }

  print("Employee Name: ${employee.Name}");
  print("Year of Experience: ${employee.yearOfExperience()} years");

  try {
    employee.applyLeave(5);
    print("Leave applied successfully.");
  } catch (e) {
    print("Error: $e");
  }
}
