import pyttsx3
import keyboard

voice = pyttsx3.init()

class A():
    def __init__(self):
        self.Customers = {
            "Customer_1": {
                'name': '',
                'arm_size': '',
                'leg_size': '',
                'waist_size': '',
                'neck_size': ''
            },
            "Customer_2": {
                'name': '',
                'arm_size': '',
                'leg_size': '',
                'waist_size': '',
                'neck_size': ''
            },
            "Customer_3": {
                'name': '',
                'arm_size': '',
                'leg_size': '',
                'waist_size': '',
                'neck_size': ''
            }
        }

    def ReturnEmpty_Maps(self):
        EmptyMaps = []
        for CustomerName, CustomerValue in self.Customers.items():
            if all(value == '' for value in CustomerValue.values()):
                EmptyMaps.append(CustomerName)
        return EmptyMaps

    def InsertValues(self):
        Emptymaps = self.ReturnEmpty_Maps()
        if not Emptymaps:
            print("No Empty Maps Available!")
            return
        MapNo = Emptymaps[0]
        Name = input("Enter Name: ")
        arm_size = input("Enter ArmSize: ")
        leg_size = input("Enter legSize: ")
        waist_size = input("Enter Waste: ")
        neck_size = input("Enter NeckSize: ")

        self.Customers[MapNo] = {
            'name': Name,
            'arm_size': arm_size,
            'leg_size': leg_size,
            'waist_size': waist_size,
            'neck_size': neck_size
        }
        print(f"{MapNo} has been updated with the provided details.")

    def UpdateValues(self):
        Map_Want = input("Enter CustomerName: ")
        if Map_Want in self.Customers:
            print("1 : For Single Value Change")
            print("2 : For All Value Change")
            No_Of_Val_To_Change = input(": ")

            if No_Of_Val_To_Change == "1":
                ValToChng = input("Enter Key_Name: ")
                if ValToChng in self.Customers[Map_Want]:
                    NewVal = input("Enter Updated Value: ")
                    self.Customers[Map_Want][ValToChng] = NewVal
                else:
                    print(f"{ValToChng} Not Found")

            elif No_Of_Val_To_Change == "2":
                i = 1
                while i <= 5:
                    ValToChng = input("Enter Key_Name: ")
                    if ValToChng in self.Customers[Map_Want]:
                        NewVal = input("Enter Updated Value: ")
                        self.Customers[Map_Want][ValToChng] = NewVal
                    else:
                        print(f"{ValToChng} Not Found")
                    i += 1

        else:
            print(f"{Map_Want} Does Not Exist")

    def DeleteValues(self):
        Map_Want = input("Enter CustomerName: ")
        if Map_Want in self.Customers:
            Value_To_Delete = input("Enter Value TO Delete: ")
            if Value_To_Delete in self.Customers[Map_Want]:
                self.Customers[Map_Want][Value_To_Delete] = ''
                print(f"{Value_To_Delete} in {Map_Want} has been cleared.")
            else:
                print(f"{Value_To_Delete} not found in {Map_Want}.")
        else:
            print(f"{Map_Want} Invalid")

    def Print_All_CustomerInfo(self):
        for customer_name, customer_info in self.Customers.items():
            print(f"Customer: {customer_name}")
            for key, value in customer_info.items():
                print(f"  {key}: {value}")
            print()

    def main_menu(self):
        while True:
            print("\nSelect an option:")
            print("1: Insert Values")
            print("2: Update Values")
            print("3: Delete Values")
            print("4: Print All Customer Info")
            print("Press Esc to exit")

            option = input("Enter option: ")

            if option == '1':
                self.InsertValues()
            elif option == '2':
                self.UpdateValues()
            elif option == '3':
                self.DeleteValues()
            elif option == '4':
                self.Print_All_CustomerInfo()
            elif keyboard.is_pressed('esc'):
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")

# Create an instance of the class
Obj = A()
Obj.main_menu()
