from Scraper import Scraper


class Menu:

    def __init__(self):
        print("Welcome to DriveTest Ontario booking bot.\n"
              "This bot will automatically check for open test dates. ")
        PATH = input("To begin enter the full path to the chrome driver: ")
        self.scrapper = Scraper(PATH)
        self.booking_selection()

    def booking_selection(self):
        while True:
            print("Would you like to:\n"
                  "[1]: Book a test\n"
                  "[2]: Reschedule a test")
            option = int(input())
            if option == 1:
                self.book()
                break
            elif option == 2:
                self.reschedule()
                break
            else:
                print("Invalid entry!")

    def book(self):
        URL = "https://drivetest.ca/book-a-road-test/booking.html#/validate-driver-email"
        license_num = input("Enter your licence number: ").replace(" ", "")
        license_exp = input("Enter your licence expiration date (YYYY/MM/DD): ")
        email = input("Enter your email address to be notified when a booking opens: ")
        email_2 = input("Re-enter your email address ")

    def reschedule(self):
        URL = "https://drivetest.ca/book-a-road-test/booking.html#/verify-driver"
        license_num = input("Enter your licence number: ").replace(" ", "")
        license_exp = input("Enter your licence expiration date (YYYY/MM/DD): ")
        months = self.num_months()
        self.scrapper.reschedule_login(URL, license_num, license_exp)
        self.scrapper.reschedule()
        self.scrapper.select_location()
        self.scrapper.open_dates(months)

    def verify_info(self):
        pass

    def num_months(self):
        months = 0
        while months < 1:
            try:
                months = int(input("Enter the number of months you would like to check: "))
            except (TypeError, ValueError) as e:
                print("Enter a number greater than 1!")
        return months


menu = Menu()
