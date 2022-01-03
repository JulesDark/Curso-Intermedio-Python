def run():
    my_list = [1 , "Hello", True, 4.5]
    My_dic = {"Firstname" : "FAcundo", "Lastname" : "Garcia"}

    super_list = [
            {"Firstname" : "FAcundo", "Lastname" : "Garcia"},
            {"Firstname" : "Pedro", "Lastname" : "Garcia"},
            {"Firstname" : "Laura", "Lastname" : "Perez"},
            {"Firstname" : "jose", "Lastname" : "Muñoz"},
            {"Firstname" : "Pedro", "Lastname" : "Romero"},
    ] 

    super_dic = {
        "natural_nums": [1,2 , 3 , 4 ,5 , 8 ,9],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1 , 4.5 , 6.4],
        }


    for key, value in super_dic.items():
        print(key," = ", value)

if __name__ == "__main__":
    run()