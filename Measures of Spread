## calculating measures of spread (variance and standard deviation for a list)
def spread(list, std_dev= True):
    mean= sum(list)/len(list)
    variance= 0
    for i in list:
        variance += ((mean - i) ** 2)/len(list)
    if std_dev:
        return round(variance ** (1/2), 2)
    else:
        return variance

# To get standard deviation we only need to pass a list
# To get variance we need to pass second arguement as False, e.g
# spread([1,2,3,4,5]) will return standard deviation. 
#Whereas spread([1,2,3,4,5], False) will return variance.
