with open('wtbl.txt', 'r') as f:
    my_list = []
    for line in f:
        words = line.split()
        my_list.extend(words)
print(my_list)