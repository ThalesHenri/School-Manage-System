# Director GUI
from professor import Professor
from student import Student
from course import Course


# vars
teacher_list = []
student_list = []
course_list = []


# functions
def show_menu():
    run = True
    while run:
        print('-' * 20)
        print("Welcome to the School management app\n")
        print('+' * 20)
        print("Choose what you want to do: ")
        print("1 -------- Register a new teacher\n2 -------- Register a new student")
        print("3 -------- Register a new Course\n4 -------- Manage existent courses")
        print("5 -------- Exit")
        print('+' * 20)
        a = int(input("->"))
        if a == 1:
            register_teacher()
        elif a == 2:
            register_student()
        elif a == 3:
            register_course()
        elif a == 4:
            pass  # manage
        elif a == 5:
            print("Exiting the program")
            break  # quiting


def register_teacher():  # Done
    print("-" * 20)
    print("Please type the teacher information bellow. ")
    # name, cpf, address, salary
    name = str(input("1 -------- Name: "))
    cpf = str(input("2 -------- CPF: "))
    address = str(input("3 -------- Address: "))
    salary = float(input("4 -------- Salary: R$ "))
    teacher = Professor(name, cpf, address, salary)
    teacher_list.append(teacher)
    print("The professor {} was been added to the list {}".format(teacher.name, teacher_list))


def register_student():  # Done
    print("-" * 20)
    print("Please type the student information bellow. ")
    # name, cpf, address, registration, international
    name = str(input("1 -------- Name: "))
    cpf = str(input("2 -------- CPF: "))
    address = str(input("3 -------- Address: "))
    a = input("4 -------- international (1 for yes, 2 for no): ")
    if a == "1":
        international = True
    elif a == "2":
        international = False
    else:
        print("ERROR enter a valid information please!")
        print("Your registration process will be restarted!")
        register_student()
    student = Student(name, cpf, address, international)
    student_list.append(student)
    print("The student {} with the following registration code {} was been added to the list {}".format(student.name, student.registration, student_list))    


def register_course():  # Done 
    print("-" * 20)
    print("Please type the student information bellow. ")
    #  name, professor, min of students, max of students, duration, students enrolled
    name = str(input("1 -------- Name: "))
    print("checking if there is any teacher registred in the system.")
    if len(teacher_list) > 0:
        print("This is the list of the teacher registred in the sistem")
        b = 1
        for a in teacher_list:
            print("{}-{}. ".format(b,a.name))
            b += 1
        print("Choose one of the list to ministrate the course.")
        professor = str(input(""))
        for a in teacher_list:
            if a.name == professor:
                print("valid teacher!.")
            else:
                print("choose one from the list, otherwise will be an ERROR")  # Error message
        min_ = input("The mininmum of students to the course exist: ")
        max_ = input("The maximum of students to the course handle: ")
        duration = input(int("The duration of to the course in months: "))
        course = Course(name, professor, min_, max_, duration)
        course_list.append(course)
        print("the {} course has been Created in the list {}".format(course.name, course_list))


def manage_course():  # ToDO
    pass


# script
show_menu()
