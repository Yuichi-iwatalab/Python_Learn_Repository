class Square:

    object_list = []

    def __init__(self,name):
        self.object_list.append(name)

    def print_permeter(self, len):
        print("{} by {} by {} by {}".format(len,len,len,len))
    
    def judge(self, a, b):
        if a is b:
            print(True)
        else:
            print(False)

a_square = Square("Yuichi")
b_square = Square("Mizukoshi")

print(Square.object_list)
b_square.print_permeter(1)


same_b_square = b_square
b_square.judge(a_square,b_square)
b_square.judge(b_square,same_b_square)