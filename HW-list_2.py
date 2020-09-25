import random
def random_numbers():
    list_of_numbers = [random.randint(0, 9) for i in range(15)]
    print("list of random numbers: " + str(list_of_numbers))
    return list_of_numbers


list_of_random_numbers = random_numbers()
# print(x)