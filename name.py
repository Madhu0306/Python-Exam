def unique_names(names1, names2):

    unique_names = list(set().union(names1, names2))

    return unique_names

names1 = ["Ava", "Emma", "Olivia"]

names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))

# should print Ava, Emma, Olivia, Sophia
