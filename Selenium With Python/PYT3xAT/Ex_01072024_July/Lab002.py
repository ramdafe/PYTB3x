class Mom:
    def give_money(self):
        print("$150")

class Dad:
    def give_money(self):
        print("$100")

class Me(Mom, Dad):
    def my_money(self):
        print("$50")

obj = Me()
obj.give_money()
# obj.d_give_money()