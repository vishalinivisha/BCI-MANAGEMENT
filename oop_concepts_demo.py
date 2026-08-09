"""Demonstration of the required OOP concepts in the BCI Management System."""

from course import Course
from student import Student
from employee import AcademicEmployee, NonAcademicEmployee


print("BCI MANAGEMENT SYSTEM - OOP CONCEPTS")
print("=" * 50)

# 1. STATIC METHOD
print("\n1. STATIC METHOD")
print(Course.is_valid_credit(3))
print(Course.is_valid_credit(-1))

# 2. NON-STATIC METHOD
print("\n2. NON-STATIC METHOD")
course = Course("SE101", "Enterprise App Development", 3)
course.display_course()

# 3. METHOD OVERLOADING (simulated using a default argument)
print("\n3. METHOD OVERLOADING")
student = Student("ST1005", "Visha", "BSc in Information Technology")
student.addCourse(course)
student.addCourse(Course("SE102", "Database Management Systems", 4), "Semester 2")
print("Registered courses:")
for item in student.showRegisteredCourses():
    item.display_course()

# 4. ABSTRACT CLASS + ABSTRACT METHOD
# Employee is abstract, so it cannot be instantiated directly.
print("\n4. ABSTRACT CLASS AND ABSTRACT METHOD")
print("Employee is an abstract class and calculate_salary() is an abstract method.")

# 5. METHOD OVERRIDING
print("\n5. METHOD OVERRIDING")
employees = [
    AcademicEmployee("AC01", "Dr. Kumar", 100000, 5000, 3000),
    NonAcademicEmployee("NA01", "Nimal", 40000, 10, 500, 2000)
]

for employee in employees:
    employee.show_sal()
    print()
