#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for i in range(list_length):
            try:
                num1 = float(my_list_1[i]) if i < len(my_list_1) else 0
                num2 = float(my_list_2[i]) if i < len(my_list_2) else 0

                if num2 == 0:
                    result.append(0)
                    print("division by 0")
                else:
                    result.append(num1 / num2)
            except (ValueError, TypeError):
                result.append(0)
                print("wrong type")
            except IndexError:
                result.append(0)
                print("out of range")
    finally:
        return result
