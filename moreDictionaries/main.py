from collections import defaultdict

my_dict = defaultdict(int)
print(my_dict)
print((my_dict['age']))
my_dict['some_other_value'] += 20
print(my_dict)

values = {
    "person1": 122,
    "person2": 0,
    "person3": 87,
}

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = defaultdict(int)
for element in mylist:
    counter[str(element)] += 1
print(counter)

words = ["apple", "banana", "grapes", "carrot", "avocado"]
grouped_words = defaultdict(list)
for word in words:
    grouped_words[word[0]].append(word)
print(grouped_words)