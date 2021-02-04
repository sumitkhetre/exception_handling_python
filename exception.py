class AgeError(Exception):
    pass


class SalaryError(Exception):
    pass


def function1(p1, p2):
    try:
        result = p1 / p2
        print(f"result = {result}")
    except:
        print("divide by zero is handled here")

# function1(10, 5)
# function1(10, 0)

def function2(file_name):
    try:
        file = open(file_name, 'r')
        # file.write("hello python")
        print(f"data = {file.read()}")
        file.close()
    except FileNotFoundError as error:
        print(error)


# function2('/tmp/python-test/newfile.txt')
# function2('myfile.txt')


def function3():
    print("enter age: ")
    age = int(input())
    if (age < 25) or (age > 60):
        # raise Exception("age is invalid")
        raise AgeError("age is invalid")

    print(f"age = {age}")

    print("enter salary: ")
    salary = int(input())
    if salary > 10000:
        # raise Exception("too high salary")
        raise SalaryError("too high salary")

    print(f"salary = {salary}")

    return {"age": age, "salary": salary}


try:
    # contains the code that might raise an error(s)
    person = function3()
except AgeError as age_error:
    # gets called if there is an error
    print(age_error)
except SalaryError as salary_error:
    # gets called if there is an error
    print(salary_error)
else:
    # gets called if there is no error
    print(person)
finally:
    # gets called irrespective of error being raised
    print("finally block is called")

