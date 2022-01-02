
# x = int(input("Ingresa un numero limite : "))
# squat = [i*i for i in range(1, x) if i%2 == 0]
# print(squat)

def run():
    squares = [ i for i in range(1, 10001) if i%4 == 0 and i%6 ==0 and i%9 == 0]
    print(squares)  



    # for i in range(1,101):
    #     if i%3 != 0:
    #         squares.append(i**2)
    
    print(squares)
if __name__ == "__main__":
    run()