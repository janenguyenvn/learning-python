def ask():
    while True:
        try:
            num = int(input("Input a integer: "))

        except:
            print('An error occured. Pls try again!')
            continue
        else:
            print('Thank you, your number squared is {}'. format(num ** 2))
            break


print(ask())


