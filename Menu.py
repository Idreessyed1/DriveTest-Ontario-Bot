
class Menu:

    def __init__(self):
        # scrapper = Scraper()
        print("Welcome to DriveTest Ontario booking bot.\n"
              "This bot will automatically check for openings to book or reschedule a test. ")
        PATH = input("To begin enter the full path to the chromedriver: ")
        self.booking_selection()

    def booking_selection(self):
        while True:
            print("Would you like to:\n"
                  "[1]: Book a test\n"
                  "[2]: Reschedule a test")
            option = int(input())
            if option == 1:
                self.booking_info()
                break
            elif option == 2:
                self.reschedule_info()
                break
            else:
                print("Invalid entry!")
        print("!!!!!!!!!!!!!!!!!")

    def booking_info(self):
        license_num = input("Enter your licence number: ").replace(" ", "")
        license_exp = input("Enter your licence expiration date (YYYY/MM/DD): ")
        email = input("Enter your email address to be notified when a booking opens: ")
        email_2 = input("Re-enter your email address ")

    def reschedule_info(self):
        license_num = input("Enter your licence number: ").replace(" ", "")
        license_exp = input("Enter your licence expiration date (YYYY/MM/DD): ")
        print(license_num, license_exp)

    def verify_info(self):
        pass

    def num_months(self):
        months = 0
        while months < 1:
            try:
                months = int(input("Enter the number of months you would like to check: "))
            except (TypeError, ValueError) as e:
                print("Enter a number greater than 1!")


menu = Menu()
