# Inheritance
# Mulyilevel Inheritance

class GrandFather:
    gf_name = "Gopal Sharma"
    gf_age = 88
    
    def drive_a_car(self):
        print("No car.")

class Father(GrandFather):
    f_name = "Sushant Sharma"
    f_age = 50
    
    def drive_a_car2(self):
        print("Drive Suzuki Vitara Brezza.")

class Son(Father):
    name = "Kunal Sharma"
    age = 30
    
    def drive_a_car3(self):
        print("Drive Tata Safari.")
    
son_obj = Son()
son_obj.drive_a_car2()
son_obj.drive_a_car3()
print("Grandfather's name:", son_obj.gf_name)
print("Grandfather's age:", son_obj.gf_age)
print("Father's name:", son_obj.f_name)
print("Father's age:", son_obj.f_age)