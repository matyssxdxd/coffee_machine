class CoffeeMachine:

    def __init__(self, ingredients):
        self.water = ingredients[0]
        self.milk = ingredients[1]
        self.beans = ingredients[2]
        self.cups = ingredients[3]
        self.money = ingredients[4]

    def supplies(self):
        print("The coffee machine has:\n"
              f"{self.water} ml of water\n"
              f"{self.milk} ml of milk\n"
              f"{self.beans} g of coffee beans\n"
              f"{self.cups} disposable cups\n"
              f"${self.money} of money")

    def buy_coffee(self, choice):
        if choice == "1":
            if self.check_supplies():
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
        elif choice == "2":
            if self.check_supplies():
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
        elif choice == "3":
            if self.check_supplies():
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6

    def fill_machine(self, fillers):
        self.water += fillers[0]
        self.milk += fillers[1]
        self.beans += fillers[2]
        self.cups += fillers[3]

    def give_money(self):
        self.money = 0

    def check_supplies(self):
        can_make = [self.water // 200, self.milk // 50, self.beans // 15]
        if min(can_make) >= 1:
            print("I have enough resources, making you a coffee!")
            return True
        else:
            if self.water // 200 == 0:
                print("Sorry, not enough water")
            if self.milk // 50 == 0:
                print("Sorry, not enough milk")
            if self.beans // 15 == 0:
                print("Sorry, not enough beans")
            return False


coffee_machine = CoffeeMachine([400, 540, 120, 9, 550])

while True:
    user_input = input("Write action (buy, fill, take, remaining, exit): ")
    if user_input == "buy":
        user_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3- cappuccino: ")
        coffee_machine.buy_coffee(user_input)
    elif user_input == "fill":
        user_input = [int(input("Write how many ml of water you want to add: ")),
                      int(input("Write how many ml of milk you want to add: ")),
                      int(input("Write how many grams of coffee beans you want to add: ")),
                      int(input("Write how many disposable cups you want to add: "))]
        coffee_machine.fill_machine(user_input)
    elif user_input == "take":
        print(f"I gave you ${coffee_machine.money}")
        coffee_machine.give_money()
    elif user_input == "remaining":
        coffee_machine.supplies()
    elif user_input == "exit":
        break
