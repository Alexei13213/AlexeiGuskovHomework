import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaH
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc

ball mall hall wall tall
'''
sentence = 'Start a sentence and then bring it to an end Start'

# # Number 1
# color = re.match(r'#[0-9A-Fa-f]{6}', input('Enter Color Code:'))
# if color is None:
#     print('code is not correct')
# else:
#     print('Code is correct')

# # Number 2
# pattern1 = re.compile(r'(\d)[^\+]')
# matches = pattern1.finditer(text_to_search)
# for match in matches:
#     print(match.group(1))

# # Number 3
# que3 = re.findall(r'(([0-3]\d|[0-1]):[0-5]\d)', 'Завтрак в 09:00')
# print(que3)

# Number 4
with open('people.txt', 'r', encoding='utf8') as file:
    data1 = file.read()
    pattern = re.compile(r'[\w*][A-Za-z-]')
    matches = pattern.finditer(data1)
    for mat in matches:
        print(mat)


