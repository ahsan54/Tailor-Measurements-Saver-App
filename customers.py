class CustomerManager:
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

    def InsertValues(self, name, arm_size, leg_size, waist_size, neck_size):
        Emptymaps = self.ReturnEmpty_Maps()
        if not Emptymaps:
            return "No Empty Maps Available!"
        MapNo = Emptymaps[0]
        self.Customers[MapNo] = {
            'name': name,
            'arm_size': arm_size,
            'leg_size': leg_size,
            'waist_size': waist_size,
            'neck_size': neck_size
        }
        return f"{MapNo} has been updated with the provided details."

    def UpdateValues(self, customer_name, values_to_update):
        if customer_name in self.Customers:
            for key, value in values_to_update.items():
                if key in self.Customers[customer_name]:
                    self.Customers[customer_name][key] = value
            return f"{customer_name} has been updated."
        else:
            return f"{customer_name} Does Not Exist"

    def DeleteValues(self, customer_name, value_to_delete):
        if customer_name in self.Customers:
            if value_to_delete in self.Customers[customer_name]:
                self.Customers[customer_name][value_to_delete] = ''
                return f"{value_to_delete} in {customer_name} has been cleared."
            else:
                return f"{value_to_delete} not found in {customer_name}."
        else:
            return f"{customer_name} Invalid"

    def Print_All_CustomerInfo(self):
        info = []
        for customer_name, customer_info in self.Customers.items():
            customer_details = {'Customer': customer_name}
            for key, value in customer_info.items():
                customer_details[key] = value
            info.append(customer_details)
        return info

    def search_customer(self, search_term):
        found_customers = []
        for customer_id, customer_info in self.Customers.items():
            if search_term.lower() in customer_info['name'].lower():
                found_customers.append((customer_id, customer_info))
        return found_customers
