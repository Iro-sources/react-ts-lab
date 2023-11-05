# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


num = int(input("Hva er svaret på det ultimate spørsmålet om livet, universet og alle ting? "
                "Hint: Det er et tall:"))
if num == 42:
    print("Det stemmer, meningen med livet er 42!")
elif num > 30 and num < 50:
    print("Nærme, men feil")
else:
    print( "FEIL!")

