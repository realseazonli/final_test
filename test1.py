def find_max(a_list):
    i = 0
    result = 0
    if a_list == '':
        print(result)
    else :
        for i in range(len(a_list) - 1):
            if a_list[i] >= a_list[i + 1]:
                result = a_list[i]
            else :
                result = a_list[i + 1]
            i += 1
        return result


print(find_max([1, 3, 2, 5, 18, 11, 9, 29, 6]))