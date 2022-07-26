##Given a string, write a Python program to find the largest substring of uppercase characters and print the length of that substring.

string = input()
count= 0
lis=[]
for i in range(len(string)):
    if string[i].isupper():
        count += 1
        if i == len(string) -1:
            lis.append(count)
    else:
        lis.append(count)
        count= 0
print(max(lis))
