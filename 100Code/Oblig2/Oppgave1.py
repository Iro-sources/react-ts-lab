def live_42(num):

    if num == 42:
        return "Det stemmer, meningen med livet er 42!"
    elif num > 30 and num < 50:
        return "Nærme, men feil"
    else:
        return "FEIL!"

num = int(input("Hva er svaret på det ultimate spørsmålet om livet, universet og alle ting? "
                "Hint: Det er et tall:"))
result = live_42(num)
print(result)