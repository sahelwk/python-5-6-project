# exersice number 1
marks = [85, 45, 90, 60, 35]

print("All Marks:")

for mark in marks:
    print(mark)

total = sum(marks)
print("Total Marks:", total)

average = total / len(marks)
print("Average Marks:", average)

print("Passing Marks:")

for mark in marks:
    if mark >= 50:
        print(mark)

marks.append(75)

marks.remove(45)

print(marks)

# exercise number 2

products = ["Apple", "Orange", "Kiwi", "Banana"]
products.append("Peach")
products.insert(1, "Tomato")
products.remove("Apple")
removed_item = products.pop()
products.sort()
print("Final List:", products)
