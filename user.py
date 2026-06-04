
class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_unit_info(self):
        return f"Unit: {self.first_name},{self.last_name}"


my_user = Users("Svetlana", "Bazhenova") 

print(my_user.get_first_name())
print(my_user.get_last_name())  
print(my_user.get_unit_info())
