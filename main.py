portfolio = [
    {"name" : "apple", "shares" : 10, "purchase_price" : 35, "current_price" : 40},
    {"name" : "nasa", "shares" : 5, "purchase_price" : 75, "current_price" : 78},
]

def view_portfolio(lst):
    print("-----------   ||    ------------")
    for dic in lst:
        print(f"company: {dic['name']}")
        print(f"shares: {int(dic['shares'])}")
        print(f"purchase price: {float(dic['purchase_price'])}$")
        print(f"current price: {float(dic['current_price'])}$")
        print("")

    return None

def add_stock(lst,name,shares,purchase_price,current_price):
    lst.append({"name" : name, "shares" : shares , "purchase_price" : purchase_price, "current_price" : current_price})
    print("Success fully added!")

def delete_stock(lst,name):
    lst.pop(is_there(lst,name) - 1)
    print("Deleted Succesfully!")

def total_investment(lst):
    result = 0
    for dic in lst:
        result += dic["shares"] * dic["purchase_price"]

    print(f"total investment: {float(result)}$")

def is_there(lst, name):
    for i in range(len(lst)):
        if lst[i]["name"] == name:
            return i + 1
    return 0

def update_current_price(lst, name, current_price):
    lst[is_there(lst,name) - 1]["current_price"] = current_price
    print("Current price updated successfully!")

def update_share(lst, name, shares):
    lst[is_there(lst,name) - 1]["shares"] = shares
    print("Shares updated successfully!")

def calculate_profit(lst):
    result = 0
    for dic in lst:
        result += dic["shares"] * (dic["current_price"] - dic["purchase_price"]) 

    print(f"Profit: {float(result)}$")           

def is_digit(num):
    if not num.isalpha():
        return True
    return False

while True:
    user_data = input("> ").lower()

    if user_data == "quit":
        break

    elif user_data == "help":
        print("-----------   ||    ------------")
        print("View -> to view portfolio")
        print("Profit -> to view your profit")
        print("Add -> to add new share")
        print("Update -> to update your shares")
        print("Delete -> to delete your shares")
        print("Total -> to get total investment in shares")
        print("Quit -> to Exit")
        print("")

    elif user_data == "view":
        view_portfolio(portfolio)

    elif user_data == "add":
        print("-----------   ||    ------------")
        name = input("Enter company name: ")
        if bool(is_there(portfolio, name)):
                print("sorry, you already saved that share!")
                continue
        shares = input("Enter number of shares: ")
        purchase_price = input("Enter purchase price: ")
        current_price = input("Enter current price: ")
        if is_digit(shares) and is_digit(purchase_price) and is_digit(current_price):
            add_stock(portfolio,name,int(shares),float(purchase_price),float(current_price))
        else:
            print("Enter valid inputs!")
        print("")

    elif user_data == "delete":
        print("-----------   ||    ------------")
        name = input("Enter company name: ")

        if not bool(is_there(portfolio, name)):
                print("NO SHARES FOUND!")
                continue
        delete_stock(portfolio, name)
        print("")

    elif user_data == "total":
        print("-----------   ||    ------------")
        total_investment(portfolio)
        print("")

    elif user_data == "profit":
        calculate_profit(portfolio)
    elif user_data == "update":
        print("-----------   ||    ------------")
        name = input("Enter company name: ")

        if not bool(is_there(portfolio, name)):
                print("SHARE NOT FOUND!")
                continue

        choice = input("UPDATE X -> current_price / Y -> shares:  ").lower()
        if choice == "x":
            current_price = input("Enter current price: ")
            if is_digit(current_price):
                update_current_price(portfolio,name,float(current_price))
            else:
                print("Enter valid inputs")
        elif choice == "y":
            shares = input("Enter shares: ")
            if is_digit(shares):
                update_share(portfolio,name,int(shares))
            else:
                print("Enter valid input")

        else:
             print("command NOT FOUND!")
        print('')


    else:
        print("This command NOT FOUND!")

