from utils.connector_db import *


def menu():
    print("All contacts -> 0")
    print("Search contact -> 1")
    print("Create contact -> 2")
    print("Delete contact -> 3")
    print("Exit -> 4")
    a = None
    try:
        a = int(input())
        if a != 0 and a != 1 and a != 2 and a != 3 and a != 4:
            raise Exception
    except(Exception):
        print("Try again!!!")
        menu()
    return a


def create_contact():
    name = str(input("Please enter the name : "))
    phone = str(input("Please enter the phone (+9989********) : "))
    create_contact_db(name=name, phone=phone)


def print_row(row):
    try:
        for index, item in enumerate(row):
            print(f'{index + 1} -> Name : {item[0]} \t Phone : {item[1]}')
    except (Exception):
        print("Something wrong!!!")

def all_contacts():
    row = get_all_contact()
    print_row(row)


def search_contact():
    arg = str(input("Please enter something like name or phone for searching :"))
    row = search_contact_db(arg=arg)
    print_row(row)


def delete_contact():
    row = get_all_contact()
    print_row(row)
    a = int(input("Please select one of the contacts :"))
    delete_contact_db(name=row[a - 1][0], phone=row[a - 1][1])


def switch(menu: int):
    switcher = {
        0: all_contacts,
        1: search_contact,
        2: create_contact,
        3: delete_contact,
    }
    func = switcher.get(menu)
    return func()


def run():
    menu_ = menu()
    if menu_ != 4:
        switch(menu_)
        return run()


if __name__ == '__main__':
    run()
