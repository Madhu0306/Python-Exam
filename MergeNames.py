

def unique_names(names1, names2):
    list_1= set(names1+names2)

    unique_list = (list(list_1))

    for x in unique_list:
        names1 = ["Ava", "Emma", "Olivia"]
        names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))
# should print Ava, Emma, Olivia, Sophia

#names1 = ["Ava", "Emma", "Olivia"]
#names2 = ["Olivia", "Sophia", "Emma"]
#print(unique_names(names1, names2))
# should print Ava, Emma, Olivia, Sophia
