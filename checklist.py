checklist = list()


def create(item):
    checklist.append(item)


def read(index):
    item = checklist[index]
    return item


def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    # print(read(1))


def do_not_use():
    print("Hello world")
    my_fun_function('Hello World')
    checklist.append('Blue')
    print(checklist)
    checklist.append('Orange')
    print(checklist)


def my_fun_function(say_this):
    print(say_this)


test()
