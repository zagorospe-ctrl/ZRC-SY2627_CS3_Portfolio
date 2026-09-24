class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = 0.0
        self.__submitted_files = []        
    
    def __validate_grade(self, score):
        validation = False
        if score >= 0 and score <= 100:
            validation = True
        return validation

    def __check_submission_status(self):
        if len(self.__submitted_files) > 0:
            self.__is_submitted = True
        else:
            self.__is_submitted = False
        return self.__is_submitted
       
    def __is_duplicate (self, filename):
        duplicate = False
        if filename in self.__submitted_files:
            duplicate = True
        return duplicate
    
    def add_file(self, filename):
        if not self.__is_duplicate(filename):
            self.__submitted_files.append(filename)
            self.__check_submission_status()

    def remove_file(self, filename):
        if self.__grade > 0:
            return filename
        elif filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
            self.__check_submission_status()
            
    def assign_grade(self, score):
        if len(self.__submitted_files) > 0:
            if self.__validate_grade(score):
                self.__grade = score
        
    def get_grade(self):
        return self.__grade
    def view_files(self):
        return self.__submitted_files
    def get_status_report(self):
        status_report = {
            "Student Name": self.student_name,
            "Student ID": self.student_id,
            "Assignment Title": self._assignment_title,
            "Due Date": self._due_date,
            "Submission Status": "Submitted" if self.__is_submitted is True else "Missing",
            "Grade": self.__grade,
            "Submitted Files": f"{self.__submitted_files} ({len(self.__submitted_files)})"
        }
        return status_report
    
print("---INTIALIZING DROPBOX FOR STUDENTS--")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="John Pork", student_id="pshs-6700-x", assignment_title="CS-106", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Wanderer", student_id="pshs-0103-x", assignment_title="CS-102", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Sebastian", student_id="pshs-1110-x", assignment_title="CS-105", due_date="2026-10-01")

print()

print("---TEST SCENARIO 1: Multiple Files via List---")
student1.add_file("main.py")
print(f"---> [Success] Alexa Gonzaga attached 'main.py'. Total files: 1")
print(f"---> [Success] Alexa Gonzaga attached 'report.pdf'. Total files: 2")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"---> [Success] Grade 95 officially assigned to Alex Gonzaga.")
print(f"Alex's Files: {student1.view_files()}\n")

print("---TEST SCENARIO 2: Removing Files from List---")
student2.add_file("wrong_homework.docx")
print(f"---> [Success] Adelle attached 'wrong_homework.docx'. Total files: 1")
student2.remove_file("wrong_homework.docx")
print(f"---> [Success] Adelle removed 'wrong_homework.docx'.")
student2.add_file("correct_project.py")
print(f"---> [Success] Adelle attached 'correct_project.py'. Total files: 1")
student2.assign_grade(88)
print(f"---> [Success] Grade 88 officially assigned to Adelle")
print(f"Adelle's Files: {student2.view_files()}\n")
print()

print("---TEST SCENARIO 3: Preventing Duplicate Files---")
student3.add_file("script.py")
print(f"---> [Success] John Pork attached 'script.py'. Total files: 1")
student3.add_file("script.py")
print(f"---> [Warning] 'script.py' is already attached!")
print(f"John's Files: {student3.view_files()}\n")
print()

print("---TEST SCENARIO 4: Removing File After Being Graded---")
student4.add_file("exam_answers.pdf")
print(f"---> [Success] Wanderer attached 'exams_answers.pdf'. Total files: 1")
student4.assign_grade(75)
print(f"---> [Success] Grade 75 officially assigned to Wanderer.")
student4.remove_file("exam_answers.pdf")
print(f"---> [Warning] Wanderer cannot remove files. Assignment already graded.")
print()

print("---TEST SCENARIO 5: Empty List Handling---")
student5.add_file("draft.txt")
print(f"---> [Success] Sebastian attached 'draft.txt'. Total files: 1")
student5.remove_file("draft.txt")
print(f"---> [Success] Sebastian removed 'draft.txt'.")
student5.assign_grade(100)
print(f"---> [Error] Cannot grade. No files submitted for Sebastian.")
print()

print("---FINAL SYSTEM REPORT---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
