# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log:
#   MyNames, 02/09/2024, Created Script
#
# ------------------------------------------------------------------------------------------ #


import sys #for sys.exit() at end of loop

# Define the Data Constants
MENU: str = '''
------Course Registration Program------
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
---------------------------------------
'''
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str = "" # Hold the choice made by the user.
student_data: dict = [] # Dict of student data
students: list = []  # a table of student data

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    with open(FILE_NAME, "r") as file:
        for row in file.readlines():
            # Transform the data from the file
            student_data = row.strip().split(",")
            student_data = [student_data[0], student_data[1], student_data[2]]
            # Load it into our collection (list of lists)
            students.append(student_data)
except FileNotFoundError as error_message:
    print("")
    print("ERROR: Database file not found!")
    print("")
    print(f"Error details: {error_message}")
    print("")
    print("Exiting the program!")
    sys.exit()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("Select a menu option (1-4): ")

    # Input user data
    match menu_choice:

        case "1":
            while student_first_name =="":
                try:
                    print("")
                    student_first_name = input("Enter the student's first name: ")
                    if student_first_name != "":
                        try:
                            if not student_first_name.isalpha():
                                raise Exception("The first name should only contain letters!")
                        except Exception as error_message:
                            print("")
                            print(f"Error details: {error_message}")
                            student_first_name = ""
                            continue
                    if not student_first_name:
                        raise Exception("You need to enter a first name!")
                except Exception as error_message:
                    print("")
                    print(f"Error details: {error_message}")
                
            while student_last_name =="":    
                try:
                    print("")
                    student_last_name = input("Enter the student's last name: ")
                    if student_last_name != "":
                        try:
                            if not student_last_name.isalpha():
                                raise Exception("The last name should only contain letters!")
                        except Exception as error_message:
                            print("")
                            print(f"Error details: {error_message}")
                            student_last_name = ""
                            continue
                    if not student_last_name:
                        raise Exception("You need to enter a last name!")
                except Exception as error_message:
                    print("")
                    print(f"Error details: {error_message}")
            print("")
            course_name = input("Please enter the name of the course: ")
            student_data = [student_first_name,student_last_name,course_name]
            students.append(student_data)
            print("")
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")


    # Present the current data
        case "2":

            # Process the data to create and display a custom message
            print("-"*50) #Adds dashs above student data
            for student in students:
                print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
            print("-"*50) #Adds dashs below student data


    # Save the data to a file
        case "3":
            try:
                with open(FILE_NAME, "w") as file:
                    for student in students:
                        csv_data = f"{student[0]},{student[1]},{student[2]}\n"
                        file.write(csv_data)
                    print("")
                    print("The following data was saved to file!")
                    for student in students:
                        print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
            except TypeError as error_message:
                print("")
                print("Please check that the data is a valid CSV format!")
                print("ERROR INFO: ")
                print(error_message, error_message.__doc__, type(error_message), sep=",")
            except Exception as error_message:
                print("")
                print("ERROR INFO: ")
                print(error_message, error_message.__doc__, type(error_message), sep=",")


    # Stop the loop
        case "4":
            print("Exiting the program!")# out of the loop
            sys.exit()
    #In the event of something entered other than (1-4)
        case _:
            print("Invalid selection!")