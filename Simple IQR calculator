def IQR(list):
    list= sorted(list)
    if len(list) % 2 != 0:
        first_quart= list[0 : len(list)//2]
        second_quart= list[ (len(list)// 2) + 1 : ]
    else:
        first_quart= list[0 : int(len(list)/2) ]
        second_quart= list[int(len(list)/2) :  ]
    if len(first_quart) % 2 == 0:
        first_med= (first_quart[int(len(first_quart)/2)] + first_quart[(int(len(first_quart)/2)) - 1])/2
        second_med= (second_quart[int(len(second_quart)/2)] + second_quart[(int(len(second_quart)/2)) - 1])/2
    else:
        first_med= first_quart[len(first_quart)//2]
        second_med= second_quart[len(second_quart) // 2]
    IQR= second_med - first_med
    return IQR
