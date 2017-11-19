#NAME : Narwade Swapnil
#UTA ID : 1001396025
import pickle
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILENAME = 'employee.dat'


class Employee:
    def __init__(self, name, emp_id, department, job_title):
        self.__name = name
        self.__emp_id = emp_id
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_id(self, emp_id):
        self.__emp_id = emp_id

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__emp_id

    def get_department(self):
        return self.get_department

    def get_job_title(self):
        return self.__job_title

    def __str__(self):
        return "Name:\t\t" + self.__name + "\nID:\t\t\t" + self.__emp_id + "\nDepartment:\t\t\t" \
               + self.__department + "\nJob_Title:\t\t  " + self.__job_title


def main():
    employee = load_employee()
    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(employee)
        elif choice == ADD:
            add(employee)
        elif choice == CHANGE:
            change(employee)
        elif choice == DELETE:
            delete(employee)
    save_employee(employee)


def load_employee():
    try:
        input_file = open(FILENAME, 'rb')
        employee_info = pickle.load(input_file)
        input_file.close()
    except IOError:
        employee_info = {}
    return employee_info


def get_menu_choice():
    print("--------------------------------")
    print("WELCOME TO THE EMPLOYEE DATABASE")
    print("1)Look For The Employee Using ID")
    print("2)Add Employee Into The Database")
    print("3)Change Existing Employees Data")
    print("4)Delete Existing Employee")
    print("5)Quit")
    choice = int(input("Enter The Choice"))
    while LOOK_UP < choice > QUIT:
        choice = int(input("Enter A Valid Choice"))
    return choice


def save_employee(employee):
    output_file = open(FILENAME, 'wb')
    pickle.dump(employee, output_file)
    output_file.close()


def look_up(employee):
    emp_id = input("Enter an ID of Employee")
    print(employee.get(emp_id, 'Employee Is Not Found'))


def add(employee):
    name = input("Name:")
    emp_id = input("ID")
    department = input("Department")
    job_title = input("Job Title")
    entry = Employee(name, emp_id, department, job_title)
    if id not in employee:
        employee[emp_id] = entry
        print("The Entry Has Been Added")
    else:
        print("The Employee already exists")


def change(employee):
    emp_id = input("Enter The Employee ID ")
    if emp_id in employee:
        name = input("Enter The Name:")
        department = input("Enter The Department")
        job_title = input("Enter The Job Title")
        entry = Employee(name, emp_id, department, job_title)
        employee[emp_id] = entry
        print("Information Updated")
    else:
        print("Employee ID is not Found")


def delete(employee):
    emp_id = input("Enter The Employee ID")
    if emp_id in employee:
        del employee[emp_id]
        print("Entry Deleted")
    else:
        print("Employee ID is not found")


main()
