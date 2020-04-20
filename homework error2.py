x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print('Cannot divide number by 0')
finally:
    print('All done')



