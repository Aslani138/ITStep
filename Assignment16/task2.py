class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)
        return f"{self.name} has been enrolled in {course}"

    def display_info(self):
        return f"Student Name: {self.name}, Student ID: {self.student_id}"

    def display_courses(self):
        return f"{self.name}'s Courses: {', '.join(self.courses)}"

# Creating student objects
student1 = Student("Daviti", "S001")
student2 = Student("Mariami", "S002")

# Enrolling students in courses
print(student1.enroll_course("Mathematics"))
print(student1.enroll_course("Physics"))
print(student2.enroll_course("Biology"))
print(student2.enroll_course("Chemistry"))

# Displaying student information and courses
print(student1.display_info())
print(student1.display_courses())
print(student2.display_info())
print(student2.display_courses())
