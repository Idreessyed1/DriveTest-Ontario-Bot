
class Menu:

    def __init__(self):
        pass

    def enter_info(self):
        license_num = input("Enter your licence number: ").replace(" ", "")
        license_exp = input("Enter your licence expiration date (YYYY/MM/DD): ")
        email = input("Enter your email address to be notified when a booking opens: ")
        print(license_num, license_exp, email)

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
menu.enter_info()
menu.num_months()
