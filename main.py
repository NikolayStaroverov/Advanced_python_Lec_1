from application.Data import Names, Salaries
from application.db.People import get_employees
from application.Salary import calculate_salary

def main():
    get_employees(Names)
    calculate_salary(Salaries)

if __name__ == '__main__':
    main()