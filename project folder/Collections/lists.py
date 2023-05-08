
list_a = ["item1", "item2", "item3"]

print(list_a[0])
print(list_a[2])

list_a.append("item4")

print(list_a[3])

list_b = ["b_item 1", "b_item_2"]
list_c = [1, 2 , 3]

list_b.extend(list_a)
list_b.append(list_c)



print("-----------")
for item in list_b:
    print(item)
print("-----------")
print(list_b.pop[0])

