from logic.employee_logic import Employee_Logic


class Employee_UI:
    def __init__(self):
        self.employee_logic = Employee_Logic()


    def menu_output(self):
        print(" " * 32 + " _  _      _  _        _     ")
        print(" " * 32 + "| \| |__ _| \| |  __ _(_)_ _ ")
        print(" " * 32 + "| .` / _` | .` | / _` | | '_|")
        print(" " * 32 + "|_|\_\__,_|_|\_| \__,_|_|_| ")                                                    
        print(" " * 32 + "╔════════════════════════════════════════════════════════════╗")
        print(" " * 32 + "║                    Welcome to the Menu!                    ║")
        print(" " * 32 + "║                  Please select an option:                  ║")
        print(" " * 32 + "║   ╔════════════════════════════════════════════════════╗   ║")
        print(" " * 32 + "║   ║   1. Register Cabin Crew                           ║   ║")
        print(" " * 32 + "║   ╚════════════════════════════════════════════════════╝   ║")
        print(" " * 32 + "║   ╔════════════════════════════════════════════════════╗   ║")
        print(" " * 32 + "║   ║   2. Look up Employee                              ║   ║")
        print(" " * 32 + "║   ╚════════════════════════════════════════════════════╝   ║")
        print(" " * 32 + "║   ╔════════════════════════════════════════════════════╗   ║")
        print(" " * 32 + "║   ║   3. Register Destination                          ║   ║")
        print(" " * 32 + "║   ╚════════════════════════════════════════════════════╝   ║")
        print(" " * 32 + "║   ╔════════════════════════════════════════════════════╗   ║")
        print(" " * 32 + "║   ║   4. Register Voyages                              ║   ║")
        print(" " * 32 + "║   ╚════════════════════════════════════════════════════╝   ║")
        print(" " * 32 + "║   ╔════════════════════════════════════════════════════╗   ║")
        print(" " * 32 + "║   ║   5. View as Cabin Crew                            ║   ║")
        print(" " * 32 + "║   ╚════════════════════════════════════════════════════╝   ║")
        print(" " * 32 + "╚════════════════════════════════════════════════════════════╝")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input(" " * 32 +"Enter your command: ")
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