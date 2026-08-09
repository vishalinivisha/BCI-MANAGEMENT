from employee import AcademicEmployee, NonAcademicEmployee, display_salary_details


teacher = AcademicEmployee(
    employee_id="bs01",
    employee_name="Dr. Krish Kapoor",
    basic_salary=100000,
    academic_allowance=5000,
    research_allowance=3000
)

assistant = NonAcademicEmployee(
    employee_id="bs02",
    employee_name="Vaani",
    basic_salary=40000,
    overtime_hours=10,
    overtime_rate=500,
    service_allowance=2000
)

print("=" * 50)
print("BCI MANAGEMENT SYSTEM - EMPLOYEE SALARY")
print("=" * 50)
display_salary_details([teacher, assistant])
