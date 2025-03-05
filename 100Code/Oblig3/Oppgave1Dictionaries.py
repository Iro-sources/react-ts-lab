
student = {
    "first name" : "Ola",
    "last name" : "Nordmann",
    "favourite course" : "Programmering 1"
}

full_name = student["first name"] + " " + student["last name"]
student["favourite course"] = "ITF10219 Programmering 1"
student["age"] = 20

print(f"Jeg er {full_name} and my cousrse is {favourite course}")

print(student)


def prime_checker(number):
    for num in range(2, number):
        if number % num == 0:
            print("is not a prime number")
            return  # exit the function immediately

    print("is a prime number")

n = int(input())  # check this number
prime_checker(number=n)

















