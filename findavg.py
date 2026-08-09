from student import Student
from course import Course


def calculate_gpa_and_avg():
    # Course list
    course_ead = Course("SE101", "Enterprise App Development", 3)
    course_dbms = Course("SE102", "Database Management Systems", 4)
    course_dsa = Course("SE103", "Data Structures & Algorithms", 3)
    course_oop = Course("SE104", "Object Oriented Programming", 3)
    course_web = Course("SE105", "Web Development", 3)

    # Student list
    rama = Student("ST1001", "rama", "BSc in Software Engineering",
                   [course_ead, course_dbms, course_dsa, course_oop])
    shobana = Student("ST1002", "shobana", "BSc in Information Technology",
                     [course_dbms, course_dsa, course_oop, course_web])
    vishuu = Student("ST1003", "vishuu", "BSc in Software Engineering",
                    [course_ead, course_dbms, course_dsa, course_oop])
    aadhithy = Student("ST1004", "aadhithy", "BSc in Information Technology",
                      [course_dbms, course_dsa, course_oop, course_web])

    rama.assign_marks(course_ead, 85)
    rama.assign_marks(course_dbms, 90)
    rama.assign_marks(course_dsa, 78)
    rama.assign_marks(course_oop, 88)

    shobana.assign_marks(course_dbms, 92)
    shobana.assign_marks(course_dsa, 85)
    shobana.assign_marks(course_oop, 80)
    shobana.assign_marks(course_web, 95)

    vishuu.assign_marks(course_ead, 75)
    vishuu.assign_marks(course_dbms, 80)
    vishuu.assign_marks(course_dsa, 70)
    vishuu.assign_marks(course_oop, 85)

    aadhithy.assign_marks(course_dbms, 88)
    aadhithy.assign_marks(course_dsa, 92)
    aadhithy.assign_marks(course_oop, 90)
    aadhithy.assign_marks(course_web, 85)

    students = [rama, vishuu, shobana, aadhithy]

    print("Student GPA and Average:")
    print()
    for student in students:
        gpa = student.calculate_gpa()
        average = student.calculate_average()
        print(f"{student.showStudentName()}'s GPA is: {gpa:.2f} and average is: {average:.2f}")


if __name__ == "__main__":
    calculate_gpa_and_avg()
