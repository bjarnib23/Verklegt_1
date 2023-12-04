from logic.employee_logic import Employee_Logic


class Employee_UI:
    def __init__(self):
        self.employee_logic = Employee_Logic()


    def menu_output(self):
        print("1. register cabin crew")
        print("2. look up employee")
        print("3. register destination")
        print("4. register voyages")
        print("5. view as cabin crew")
        print("q. to exit")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                break

            elif command == "1":

                self.employee_logic.register_cabin_crew()
            elif command == "2":
                result = self.employee_logic.look_up_employee()
            elif command == "3":
                self.employee_logic.register_destination()
            elif command == "4":
                self.employee_logic.register_voyages()
            elif command == "5":
                self.employee_logic.view_as_cabin_crew()
            else:
                print("invalid input, try again")