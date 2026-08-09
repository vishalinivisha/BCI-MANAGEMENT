class Student:
    def __init__(self, id, name, program, courses=None):
        # Student ID is private (encapsulation)
        self.__id = id
        self.name = name
        self.program = program
        self.courses = courses if courses is not None else []
        self.marks = {}

    def getDetails(self):
        return self.__id, self.name, self.program, self.courses

    def showStudentName(self):
        return self.name

    def showStudentId(self):
        return self.__id

    def showDegreeProgram(self):
        return self.program

    def showRegisteredCourses(self):
        return self.courses

    # Method overloading in Python is simulated using a default argument.
    # addCourse(course) and addCourse(course, semester) are both supported.
    def addCourse(self, course, semester=None):
        self.courses.append(course)
        if semester is not None:
            print(f"{course.course_code} registered for {semester} semester.")

    def assign_marks(self, course, score):
        self.marks[course] = score

    def calculate_average(self):
        if not self.marks:
            return 0.0
        return sum(self.marks.values()) / len(self.marks)

    def calculate_gpa(self):
        total_points = 0
        total_units = 0

        for course, score in self.marks.items():
            if score >= 75:
                points = 4.0
            elif score >= 65:
                points = 3.0
            elif score >= 55:
                points = 2.0
            elif score >= 35:
                points = 1.0
            else:
                points = 0.0

            total_points += points * course.credit_value
            total_units += course.credit_value

        return total_points / total_units if total_units > 0 else 0.0
