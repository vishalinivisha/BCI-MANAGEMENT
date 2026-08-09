class Course:
    def __init__(self, course_code, course_name, credit_value):
        if not Course.is_valid_credit(credit_value):
            raise ValueError("Credit value must be greater than 0")

        self.course_code = course_code
        self.course_name = course_name
        self.credit_value = credit_value

    # Static method - can be called without creating a Course object
    @staticmethod
    def is_valid_credit(credit_value):
        return isinstance(credit_value, (int, float)) and credit_value > 0

    # Non-static method - works with a Course object
    def display_course(self):
        print(f"{self.course_code} - {self.course_name} ({self.credit_value} credits)")
