# 第一次做的时候条件看错了，导致第二和第三个cell写的代码比较丑陋，实际上signup处只需要添加一个function即可，谨慎参考

"""first cell"""
def import_and_create_bank(filename):
    # create an empty bank dictionary
    bank = {}
    # read the file
    f = open(filename, "r")
    # since every line represents one user, apply readlines() to create a list
    lines = f.readlines()
    # iterate over all the lines
    for line in lines:
        # strip white spaces and split line into list based on ":"
        lst = line.strip().split(":")
        # skip the line with only key or value
        if len(lst) <= 1:
            continue
        # assign name to key and deposit to value
        key = lst[0].strip()
        value = lst[1].strip()
        # skip if the deposit is not number
        try:
            value = float(value)
            bank[key] = bank.get(key, 0) + value
        except:
            continue
    # print(bank)
    # close the file
    f.close()
    return bank

"""second cell"""
def check_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False

def check_lower(password):
    for char in password:
        if char.islower():
            return True
    return False

def check_number(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def validation(user_accounts, username, password):
    """test whether the username and the password are both valid.
    User_accounts is a dictionary contains all user names"""
    if (username not in user_accounts) and len(password) >= 8 and check_upper(password) and check_lower(password) and check_number(password) and username != password:
        return True
    else:
        return False


def signup(user_accounts, log_in, username, password):

    if validation(user_accounts, username, password):
        user_accounts[username] = password
        log_in[username] = False
        return True
    else:
        return False

"""third cell"""
def import_and_create_accounts(filename):
    # Create an empty user accounts dictionary and an empty login dictionary
    user_accounts = {}
    log_in = {}
    # read the file
    f = open(filename, "r")
    # since every line represents one user, apply readlines() to create a list
    lines = f.readlines()
    # iterate over all the lines
    for line in lines:
        # strip white spaces and split line into list based on ":"
        lst = line.strip().split("-")
        # skip the line with only key or value
        if len(lst) <= 1:
            continue
        # assign name to key and deposit to value
        key = lst[0].strip()
        value = lst[1].strip()
        if validation(user_accounts, key, value):
            user_accounts[key] = value
            log_in[key] = False
        else:
            continue
    f.close()
    #print(user_accounts)
    #print(log_in)
    return user_accounts, log_in


"""fourth cell"""
def login(user_accounts, log_in, username, password):
    if (username not in user_accounts) or (password != user_accounts[username]):
        return False
    else:
        log_in[username] = True
        return True

"""fifth cell"""
def update(bank, log_in, username, amount):
    if log_in[username] != True:
        return False

    if username not in bank:
        bank[username] = 0

    if amount + bank[username] < 0:
        return False
    else:
        bank[username] += amount
        return True

"""sixth cell"""
def transfer(bank, log_in, userA, userB, amount):
    if userA not in bank or log_in[userA] != True:
        return False
    if userB not in log_in:
        return False
    if userB not in bank:
        bank[userB] = 0
    if bank[userA] - amount < 0:
        return False
    else:
        bank[userA] -= amount
        bank[userB] += amount
        return True

"""seventh cell"""
def change_password(user_accounts, log_in, username, old_password, new_password):
    if username not in user_accounts:
        return False
    elif log_in[username] != True:
        return False
    elif user_accounts[username] != old_password:
        return False
    elif old_password == new_password:
        return False
    elif len(new_password) >= 8 and check_upper(new_password) and check_lower(new_password) and check_number(new_password) and username != new_password:
        user_accounts[username] = new_password
        return True

"""eighth cell"""
def delete_account(user_accounts, log_in, bank, username, password):
    if username not in user_accounts or password != user_accounts[username] or log_in[username] != True:
        return False
    else:
        del user_accounts[username]
        del log_in[username]
        del bank[username]
        return True



def main():
    '''
    The main function is a skeleton for you to test if your overall programming is working.
    Note we will not test your main function. It is only for you to run and interact with your program.
    '''

    bank = import_and_create_bank("bank.txt")
    user_accounts, log_in = import_and_create_accounts("user.txt")

    while True:
        # for debugging
        print('bank:', bank)
        print('user_accounts:', user_accounts)
        print('log_in:', log_in)
        print('')
        #

        option = input("What do you want to do?  Please enter a numerical option below.\n"
        "1. login\n"
        "2. signup\n"
        "3. change password\n"
        "4. delete account\n"
        "5. update amount\n"
        "6. make a transfer\n"
        "7. exit\n")
        if option == "1":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to login
            login(user_accounts, log_in, username, password);
        elif option == "2":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to signup
            signup(user_accounts, log_in, username, password)
        elif option == "3":
            username = input("Please input the username\n")
            old_password = input("Please input the old password\n")
            new_password = input("Please input the new password\n")

            # add code to change password
            change_password(user_accounts, log_in, username, old_password, new_password)
        elif option == "4":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to delete account
            delete_account(user_accounts, log_in, bank, username, password)
        elif option == "5":
            username = input("Please input the username\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to update amount
                update(bank, log_in, username, amount)
            except:
                print("The amount is invalid. Please reenter the option\n")

        elif option == "6":
            userA = input("Please input the user who will be deducted\n")
            userB = input("Please input the user who will be added\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to transfer amount
                transfer(bank, log_in, userA, userB, amount)
            except:
                print("The amount is invalid. Please re-enter the option.\n")
        elif option == "7":
            break;
        else:
            print("The option is not valid. Please re-enter the option.\n")

#This will automatically run the main function in your program
#Don't change this
if __name__ == '__main__':
    main()
