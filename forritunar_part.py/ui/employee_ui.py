from logic.employee_logic import Employee_Logic


class Employee_UI:
    def __init__(self):
        self.employee_logic = Employee_Logic()


    def menu_output(self):
        print(" _  _      _  _        _     ")
        print("| \| |__ _| \| |  __ _(_)_ _ ")
        print("| .` / _` | .` | / _` | | '_|")
        print("|_|\_\__,_|_|\_| \__,_|_|_| ")                                                    
        print("╔════════════════════════════════════════════════════════════╗")
        print("║                    Welcome to the Menu!                    ║")
        print("║                  Please select an option:                  ║")
        print("║   ╔════════════════════════════════════════════════════╗   ║")
        print("║   ║   1. Register Cabin Crew                           ║   ║")
        print("║   ╚════════════════════════════════════════════════════╝   ║")
        print("║   ╔════════════════════════════════════════════════════╗   ║")
        print("║   ║   2. Look up Employee                              ║   ║")
        print("║   ╚════════════════════════════════════════════════════╝   ║")
        print("║   ╔════════════════════════════════════════════════════╗   ║")
        print("║   ║   3. Register Destination                          ║   ║")
        print("║   ╚════════════════════════════════════════════════════╝   ║")
        print("║   ╔════════════════════════════════════════════════════╗   ║")
        print("║   ║   4. Register Voyages                              ║   ║")
        print("║   ╚════════════════════════════════════════════════════╝   ║")
        print("║   ╔════════════════════════════════════════════════════╗   ║")
        print("║   ║   5. View as Cabin Crew                            ║   ║")
        print("║   ╚════════════════════════════════════════════════════╝   ║")
        print("╚════════════════════════════════════════════════════════════╝")

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