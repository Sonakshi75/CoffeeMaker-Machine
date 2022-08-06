MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def espresso():
    print("You chose espresso")
    water = 50
    coffee = 18
    cost = 1.5
    if(resources["water"]>=water and resources["coffee"]>=coffee):
        print(f"Your total cost is ${cost}")
        print("Insert coins")
        quarters = int(input("Enter number of quarters "))
        dimes = int(input("Enter number of dimes "))
        nickles = int(input("Enter number of nickles "))
        pennies = int(input("Enter number of pennies "))
        total_money_entered = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        if (total_money_entered > cost):
            print("Enjoy Your espresso!")
            print(f"Here's your change {total_money_entered - cost}")
            resources["water"] = resources["water"] - water
            resources["coffee"] = resources["coffee"] - coffee
        elif (total_money_entered == cost):
            print("Enjoy your espresso!")
            resources["water"] = resources["water"] - water
            resources["coffee"] = resources["coffee"] - coffee
        else:
            print("You did not enter sufficient money ")
    else:
        print("Not sufficient resources!")
    main()


def latte():
    print("You chose latte")
    water = 200
    milk = 150
    coffee = 24
    cost = 2.5
    if(resources["water"]>=water and resources["milk"]>=milk and resources["coffee"]>=coffee):
      print(f"Your total cost is ${cost}")
      print("Insert coins")
      quarters = int(input("Enter number of quarters "))
      dimes = int(input("Enter number of dimes "))
      nickles = int(input("Enter number of nickles "))
      pennies = int(input("Enter number of pennies "))
      total_money_entered = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
      if (total_money_entered > cost):
          print("Enjoy Your latte!")
          print(f"Here's your change {total_money_entered - cost}")
          resources["water"] = resources["water"] - water
          resources["milk"] = resources["milk"] - milk
          resources["coffee"] = resources["coffee"] - coffee
      elif (total_money_entered == cost):
          print("Enjoy your latte!")
          resources["water"] = resources["water"] - water
          resources["milk"] = resources["milk"] - milk
          resources["coffee"] = resources["coffee"] - coffee
      else:
          print("You did not enter sufficient money ")
    else:
        print("Not sufficient resources!")
    main()


def cappuccino():
    print("You chose cappuccino")
    water = 250
    milk = 100
    coffee = 24
    cost = 3.0
    if(resources["water"]>=water and resources["coffee"]>=coffee and resources["milk"]>=milk):
        print(f"Your total cost is ${cost}")
        print("Insert coins")
        quarters = int(input("Enter number of quarters "))
        dimes = int(input("Enter number of dimes "))
        nickles = int(input("Enter number of nickles "))
        pennies = int(input("Enter number of pennies "))
        total_money_entered = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
        if(total_money_entered >cost):
            print("Enjoy Your cappuccino!")
            print(f"Here's your change {total_money_entered - cost}")
            resources["water"] = resources["water"] - water
            resources["milk"] = resources["milk"] - milk
            resources["coffee"] = resources["coffee"] - coffee
        elif(total_money_entered == cost):
            print("Enjoy your cappucino!")
            resources["water"] = resources["water"] - water
            resources["milk"] = resources["milk"] - milk
            resources["coffee"] = resources["coffee"] - coffee
        else:
            print("You did not enter sufficient money ")
    else:
        print("Not sufficient resources!")
    main()


def report():
    print("You chose to see report")
    print(resources)
    main()


def main():
    choice = input("What would you like? (espresso/latte/cappuccino): Enter report to see the report ")
    if(choice=="espresso"):
        espresso()
    elif(choice == "latte"):
        latte()
    elif(choice == "cappuccino"):
        cappuccino()
    elif(choice == "report"):
        report()
    else:
        exit()


main()
