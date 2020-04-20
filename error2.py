while True:
    try:
        result = int(input('Please provide a number: '))
    except:
        print('Its not a number')
        continue
    else:
        print('Yes, thank you')
        break
    finally:
        print('End of try/ except/ finally')




