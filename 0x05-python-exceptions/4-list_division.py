#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    List = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ArithmeticError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            List.append(result)
    return (List)
