

def run():
    my_dic = {i: i**3 for i in range(1,101) if i%3 != 0 }
    print(my_dic)


if __name__ == "__main__":
    run()