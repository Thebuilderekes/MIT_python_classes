"""showing how python dictionaries work"""
student = {
    'name': 'david',
    'age': 34,
    'courses' : ['maths', 'english', 'economics' ]
}

print(student['name'])

##operations on dictionaries
d= {}
d.setdefault('a', {}).setdefault('b', []).append(1) ## the chaining is creating values for the previous
d.update(g=20) #same as d.update({'g': 20})
d.update({'h': 80})
print(d.get('g')) # same as print(d['g'])

print(d)



student = {"name": "Alice", "age": 20, "school": "UCLA", 'DOB': '22-8-1999'}
student.pop("age")# removes age
key, value = student.popitem()  # Removes last inserted item
print(student)
print(key, value)
