def group_by_owners(files):
	dictionary = {}
	for key, value in files.items():
		if value not in dictionary:
			dictionary[value] = [key]
		else:
			dictionary[value].append(key)
	return dictionary
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))
#{
#    'Randy': ['Input.txt', 'Output.txt'],        Should return
#    'Stan': ['Code.py']
#}
