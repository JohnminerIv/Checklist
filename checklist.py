checklist = list()
running = True

def create(item):
    checklist.append(item)


def read(index):
    item = checklist[index]
    return item


def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


def mark_completed(index):
    checklist[index] = "√" + checklist[index]


def user_input(prompt):
    user_input = input(prompt)
    return user_input


def select(function_code):

    if function_code == "C" or function_code == "c":
        input_item = user_input("What item would you like to input? ")
        create(input_item)

    elif function_code == "R" or function_code == "r":
        item_index = int(user_input("Please give the index number to read: "))

        if item_index < 0 or item_index > len(checklist) - 1:
            print("That is not an item yet.")

        else:
            print(read(item_index))

    elif function_code == "P" or function_code == "p":
        list_all_items()

    elif function_code == "D" or function_code == "d":
        item_index = int(user_input("Please give the index number to delete:"))

        if item_index < 0 or item_index > len(checklist) - 1:
            print("That is not an item yet.")

        else:
            destroy(item_index)

    elif function_code == "CH" or function_code == "ch":
        item_index = user_input("Please give the index number to check off: ")

        if item_index < 0 or item_index > len(checklist) - 1:
            print("That is not an item yet.")

        else:
            mark_completed(int(item_index))

    elif function_code == "Q" or "q":
        return False

    else:
        print("Incorrect Input")


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    # print(read(1))
    list_all_items()
    mark_completed(0)
    list_all_items()
    select("C")
    list_all_items()
    select("R")
    list_all_items()


while running is True:
    selection = user_input('''Please enter C to add an item or
     R to read a specific item or
     P to print all of the items or
     D to delete an item or
     CH to check off an item or
     Q to quit.''')
    if select(selection) is False:
        running = False
    pass
