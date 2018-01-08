"""File IO Test"""

def open_input_file():
    """Function to open the test input file."""
    print("--------------Function to open the test input file--------------")
    file = open("input.txt", "r")
    content = file.read()
    file.seek(0)
    content = file.readlines()
    content = [i.rstrip("\n") for i in content]
    file.close()
    print("--------------Function End--------------")


def write_file_test():
    """Function to write to the test input file."""
    print("--------------Function to write to the test input file--------------")
    file = open("input.txt", "r")
    content = file.readlines()
    file.close()
    file = open("output.txt", "w")
    content = [i.rstrip("\n") for i in content]
    file.writelines(content)
    file.close()
    print("--------------Function End--------------")

def append_file_test():
    """Function to append to the test input file."""
    print("--------------Function to append to the test input file--------------")
    file = open("input.txt", "r")
    content = file.readlines()
    file.close()
    file = open("output.txt", "a")
    file.writelines(content)
    file.close()
    print("--------------Function End--------------")


def with_file_test():
    """Function to test 'with'."""
    print("--------------Function to test 'with'--------------")
    with open("input.txt", "r") as file:
        content = file.readlines()
    file = open("output.txt", "a")
    file.writelines(content)
    file.close()
    print("--------------Function End--------------")


if __name__ == "__main__":
    open_input_file()
    write_file_test()
    append_file_test()
    with_file_test()
