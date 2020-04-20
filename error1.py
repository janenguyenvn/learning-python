class Adding():
    def __init__(self,a):
        self.a = a
    def add_number(self):
        try:
            result = 10 + self.a
        except:
            print('Whoops, you are adding wrong')
        else:
            print('Adding went well')
            print(result)

num = Adding('10')
print(num.add_number())