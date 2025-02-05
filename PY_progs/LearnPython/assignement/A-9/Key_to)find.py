my_dict = {'person': {'name': 'John' , 'age':   30}}
key_to_find = 'name'


for i in my_dict:
    if key_to_find in my_dict:
        print("Key Found")
        break
    else:
        for j in my_dict[i]:
            if j == key_to_find :
                