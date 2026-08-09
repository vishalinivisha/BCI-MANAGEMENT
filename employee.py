from abc import ABC, abstractmethod


# Abstract class
class Employee(ABC):
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    # Abstract method - subclasses MUST implement this method
    @abstractmethod
    def calculate_salary(self):
        pass

    # Non-static method
    def show_sal(self):
        print(f"ID: {self.eid}")
        print(f"Name: {self.ename}")
        print(f"Salary: {self.calculate_salary()}")


class AcademicEmployee(Employee):
    def __init__(self, employee_id, employee_name, basic_salary,
                 academic_allowance, research_allowance):
        super().__init__(employee_id, employee_name, basic_salary)
        self.academic_allowance = academic_allowance
        self.research_allowance = research_allowance

    # Method overriding
    def calculate_salary(self):
        return self.sal + self.academic_allowance + self.research_allowance

    # Method overriding
    def show_sal(self):
        print("Academic Employee")
        print(f"Employee ID: {self.eid}")
        print(f"Employee Name: {self.ename}")
        print(f"Basic Salary: Rs. {self.sal}")
        print(f"Academic Allowance: Rs. {self.academic_allowance}")
        print(f"Research Allowance: Rs. {self.research_allowance}")
        print(f"Total Monthly Salary: Rs. {self.calculate_salary()}")


class NonAcademicEmployee(Employee):
    def __init__(self, employee_id, employee_name, basic_salary,
                 overtime_hours, overtime_rate, service_allowance):
        super().__init__(employee_id, employee_name, basic_salary)
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate
        self.service_allowance = service_allowance

    # Method overriding
    def calculate_salary(self):
        return (self.sal +
                (self.overtime_hours * self.overtime_rate) +
                self.service_allowance)

    # Method overriding
    def show_sal(self):
        print("Non-Academic Employee")
        print(f"Employee ID: {self.eid}")
        print(f"Employee Name: {self.ename}")
        print(f"Basic Salary: Rs. {self.sal}")
        print(f"Overtime Hours: {self.overtime_hours}")
        print(f"Overtime Rate: Rs. {self.overtime_rate}")
        print(f"Service Allowance: Rs. {self.service_allowance}")
        print(f"Total Monthly Salary: Rs. {self.calculate_salary()}")


def display_salary_details(employees):
    for employee in employees:
        print("=" * 40)
        employee.show_sal()
        print()


if __name__ == "__main__":
    academic_employee = AcademicEmployee("bs01", "Maharish", 50000, 7000, 3000)
    non_academic_employee = NonAcademicEmployee("bs02", "Yathu", 40000, 8, 1500, 2000)
    display_salary_details([academic_employee, non_academic_employee])
