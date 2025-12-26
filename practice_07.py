
"""
Docstring for OOP_Assignment_Tiemoon_Sir.practice_07
We have assume that , school wants to manage homeworks assigned by teachers to students. Each homework has following attributes:
- teacher_id
- homework_id
- due_date
- task_list
- resources
Each student has following attributes:
- student_id
- submitted_homeworks
Each homework assignment has following attributes:
- tracker_id
- homework_id
- student_id
- status (assigned, submitted, evaluated)

Finally, each homework evaluation has following attributes:
- tracker_id    
- grades 

"""

class SchoolHomeWorkManagement:

    def __init__(self,school_name):

        self.school_name = school_name 
        self.teachers = []
        self.homeworks= {}
        self.students = {}
        self.homeWorkTracks= {}
        self.homeworkEvaluations= {}    


    def is_teacher_exist(self,teacher_id):
        return teacher_id in self.teachers
    
    def is_homework_exist(self,homework_id):
        return homework_id in self.homeworks
    
    def is_student_exist(self,student_id):
        return student_id in self.students


    def add_teacher(self,teacher_id):

        if self.is_teacher_exist(teacher_id):
            print(f" this id : {teacher_id} teacher already exist!!")
            return 

        self.teachers.append(teacher_id)

    def add_homework(self,homework_id,teacher_id,due_date,task_list,resources):

        if not self.is_teacher_exist(teacher_id):
            print(f" please ensure that this teacher id : {teacher_id} exist!!")
            return 

        if self.is_homework_exist(homework_id):
            print(f" this id : {homework_id} homework already exist!!")
            return 

        self.homeworks[homework_id] = {
            'teacher_id': teacher_id,
            'due_date': due_date,
            'task_list': task_list,
            'resources': resources
        }

    def add_student(self,student_id):

        if self.is_student_exist(student_id):
            print(f" this id : {student_id} student already exist!!")
            return 

        self.students[student_id] = {
            'submitted_homeworks': []
        }

    def assign_homework_to_student(self,tracker_id,homework_id,student_id):

        if not self.is_homework_exist(homework_id):
            print(f" please ensure that this homework id : {homework_id} exist!!")
            return

        if not self.is_student_exist(student_id):
            print(f" please ensure that this student id : {student_id} exist!!")
            return
        
        self.homeWorkTracks[tracker_id] = {
            'homework_id': homework_id,
            'student_id': student_id,
            'status': 'assigned'
        }

    def update_homework_status(self,tracker_id,status):
        if tracker_id not in self.homeWorkTracks:
            print(f" please ensure that this tracker id : {tracker_id} exist!!")
            return

        self.homeWorkTracks[tracker_id]['status'] = status

    def evaluate_homework(self,tracker_id,evaluation_notes,grade):

        if tracker_id not in self.homeWorkTracks:
            print(f" please ensure that this tracker id : {tracker_id} exist!!")
            return
        
        homeWorkTracks_info = self.homeWorkTracks[tracker_id] 

        if homeWorkTracks_info['status'] != 'submitted':
            print(f" homework with tracker id : {tracker_id} is not submitted yet!!")
            return

        self.homeworkEvaluations[tracker_id] = {
            'evaluation_notes': evaluation_notes,
            'grade': grade
        }

    

if __name__ == "__main__":

    ataturk_model_high_school = SchoolHomeWorkManagement('ataturk_model_high_school')
    ataturk_model_high_school.add_teacher('T001')

    # Here check this teacher exist or not
    print(f" is this teacher exist: {ataturk_model_high_school.is_teacher_exist('T001')}")
    print(f" is this teacher exist: {ataturk_model_high_school.is_teacher_exist('T002')}")

    ataturk_model_high_school.add_homework('H001','T001','2025-12-31',['Math Exercises','Science Project'],['link1','link2'])
    # Here check this homework exist or not
    print(f" is this homework exist: {ataturk_model_high_school.is_homework_exist('H001')}")
    print(f" is this homework exist: {ataturk_model_high_school.is_homework_exist('H002')}")

    # Add a student

    ataturk_model_high_school.add_student('S001')

    # Here check this student exist or not
    print(f" is this student exist: {ataturk_model_high_school.is_student_exist('S001')}")
    print(f" is this student exist: {ataturk_model_high_school.is_student_exist('S002')}")


    # Assign homework to student
    ataturk_model_high_school.assign_homework_to_student('TR001','H001','S001')
    # check homework track exist or not
    print(f" is this homework track exist: {'TR001' in ataturk_model_high_school.homeWorkTracks}")
    print(f" is this homework track exist: {'TR002' in ataturk_model_high_school.homeWorkTracks}")

    

    # Update homework status
    ataturk_model_high_school.update_homework_status('TR001','submitted')

    # Evaluate homework
    ataturk_model_high_school.evaluate_homework('TR001','Good work on the assignments','A+') 
    # Check homework evaluation exist or not
    print(f" is this homework evaluation exist: {'TR001' in ataturk_model_high_school.homeworkEvaluations}")
    print(f" is this homework evaluation exist: {'TR002' in ataturk_model_high_school.homeworkEvaluations}")
    
