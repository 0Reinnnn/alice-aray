
names = [
    ['Alice', 'Bob', 'Charlie'],
     ['David', 'Eve', 'Frank'],
      ['Grace', 'Heidi', 'Ivan'],
       ['Judy', 'Ken', 'Laura'],
]

alice_found = False

for sublist in names:
    if 'Alice' in sublist:
        sublist.remove('Alice')
        alice_found = True

if not alice_found:
    new_name = input("Alice not found. Please enter a new name to add to the array: ")
    names[0].append(new_name)

print("updated names array:")
print(names)
