COMMON_METHODS = {
	'str': [
		'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'find',
		'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit',
		'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
		'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex',
		'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
		'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
	],
	'list': [
		'append', 'extend', 'insert', 'remove', 'pop', 'clear', 'index', 'count',
		'sort', 'reverse', 'copy'
	],
	'tuple': [
		'count', 'index'
	],
	'dict': [
		'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
		'setdefault', 'update', 'values'
	],
	'set': [
		'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
		'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
		'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union',
		'update'
	],
	'file': [
		'close', 'detach', 'fileno', 'flush', 'isatty', 'read', 'readable', 'readline',
		'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines'
	],
	'builtins': [
		'abs', 'all', 'any', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr',
		'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'filter', 'float', 'format',
		'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'len', 'list', 'map',
		'max', 'min', 'next', 'oct', 'open', 'ord', 'pow', 'print', 'range', 'repr',
		'reversed', 'round', 'set', 'slice', 'sorted', 'str', 'sum', 'type', 'zip'
	]
}


# user = {
#     "id": 1,
#     "name": "John Doe",
#     "grade": 85
# }
# print(user)
# print(user['grade'])



# settings = {
#     "theme": "dark",
#     "language": "en",
#     "notifications": True
# }

product = {
    "id": 101,
    "title": "Laptop",
    "price": 999.99,
    "in_stock": True
}
# product["discount"] = 40
# product["id"] = 597
# # del product["price"]
# product.pop("price")
# product.popitem()
# print(product.get("title", "Title не существует"))
# print(product.get("email", "Email не существует"))
# print(product)
# print(product.keys())
# print(product.values())


# for i in product:
#     print(i)

# for i in product.keys():
#     print(i)

# for i in product.values():
#     print(i)

# for key, value in product.items():
#     print(key, value)


# numbers = [1,2,2,2,3,4,5,5,6,7,8,9,9]
# unique_numbers = set(numbers)
# new_numbers = list(unique_numbers)
# print(new_numbers)

# skills = {Python, Java,}
# skills.add("C++")
# print(skills)

# skills = {"Python", "Java"}
# skills.update({"C++", "JavaScript"})
# print(skills)

# skills = {"Python", "Java"}
# skills.remove("Java")   # remove throws KeyError if element is not present
# print(skills)


# skills = {"Python", "Java"}
# skills.discard("Java")  # discard does nothing if element is not present
# print(skills)

# numbers = [1,2,2,2,3,4,5,5,6,7,8,9,9]
# item = numbers.pop()  # removes and returns the last item
# print(item)  # Output: 9
# print(numbers)  # Output: [1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9]


group_a = {1, 2, 3, 4}
group_b = {3, 4, 5, 6}
result = group_a.union(group_b)
print(result)  