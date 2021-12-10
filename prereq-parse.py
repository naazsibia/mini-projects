import json
import re

prereqs = {}
with open('prereqs.json') as f:
    prereqs = json.loads(f.read().replace('\'', '"'))


def invert(prereqs: dict[str, list[str]]) -> dict[str, list[str]]:
    '''
    Invert dictionary so you map courses to courses they can be prereqs.


    >>> invert({'CSC263H5': ['CSC236H5', '(STA256H5 or STA107H5)']})
    {('CSC236H5', 'ORSTA256STA107'): ['CSC263H5]}
    '''
    inverted = {}
    course_set = set()
    for key, courses in prereqs.items():
        course_key = []
        for course in courses:
            p = r'(\w{3,}\d{3,}(H|Y)5)'
            matches = re.findall(p, course)
            matches = [match[0] for match in matches]
            course_set.update(matches + [key])
            if len(matches) <= 1:
                course_key.extend(matches)
            else:
                course = 'OR_{}'.format('/'.join(matches))
                course_key.append(course)
        inverted.setdefault(tuple(sorted(course_key)), []).append(key)
    return inverted, course_set

new_dict = {}
inverted = invert(prereqs)

actual = {}

for courses, lst in inverted[0].items():
    if len(courses) == 0:
        lst = ['CSC108H5']
    if len(courses) == 1:
        actual.setdefault(courses[0], []).extend(lst)
        continue
    and_str = 'and_{}'.format('-'.join(courses))
    for course in courses:
        actual.setdefault(course, []).append(and_str)
    actual[and_str] = lst

keys = list(actual.keys())
for key in keys:
    if key.startswith('OR'): 
        courses = key[3:].split('/')
        for course in courses:
            actual.setdefault(course, []).append(key)

mappings = []
courses = []



def get_child(name: str, actual: dict) -> dict:
    d = {}
    identity = name
    if name.startswith('and'):
        name = 'and'
    if name.startswith('OR'):
        name = 'or'
    d['name'] = name
    d['id'] = identity

    for child in actual.get(identity, []):
        d.setdefault('children', []).append(get_child(child, actual))
    return d    

print(get_child('and_', actual))
#print(mappings)

'''
 children: [
          {
            name: 'MAT135H5',
            children: [{name: 'STA256H5'}]
          },
          {
            name: 'CSC108H5',
            children: ['''