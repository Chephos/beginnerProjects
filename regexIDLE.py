Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '\d'
'\\d'
>>> '\\d'
'\\d'
>>> '\'
SyntaxError: EOL while scanning string literal
>>> '\\'
'\\'
>>> '\\'
'\\'
>>> '\\n'
'\\n'
>>> '\d\d\d\d'
'\\d\\d\\d\\d'
>>> r'\d\d\d'
'\\d\\d\\d'
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
NameError: name 're' is not defined
>>> import re
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> print(mo)
<re.Match object; span=(13, 25), match='415-555-4242'>
>>> print(f'Phone number found: {mo.group()}')
Phone number found: 415-555-4242
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> mo.group()
'415-555-4242'
>>> mo.group(1)
'415'
>>> mo.group('2')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    mo.group('2')
IndexError: no such group
>>> mo.group(2)
'555-4242'
>>> mo.group(0)
'415-555-4242'
>>> mo.groups()
('415', '555-4242')
>>> areaCode, mainNumber = mo.groups()
>>> areaCode
'415'
>>> print(areaCode)
415
>>> print(mainNumber)
555-4242
>>> phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
>>> mo = phoneNumRegex.search('My phoie number is (415) 555-4242.')
>>> mo.groups()
('(415)', '555-4242')
>>> mo.groups(1)
('(415)', '555-4242')
>>> mo.groups(2)
('(415)', '555-4242')
>>> heroRegex =  re.compile(r'Batman|Tina Fey')
>>> mo1 = heroRegex.search('Batman and Tina Fey')
>>> mo1.group()
'Batman'
>>> mo1.group(2)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    mo1.group(2)
IndexError: no such group
>>> mo2 = heroRegex.search('Tina Fey and Batman')
>>> mo2.group()
'Tina Fey'
>>> mo2.findall()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    mo2.findall()
AttributeError: 're.Match' object has no attribute 'findall'
>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat|\))')
>>> mo = batRegex.search('Bat) lost a wheel')
>>> mo.group()
'Bat)'
>>> mo.group(1)
')'
>>> batRegex = re.compile(r'Bat(wo)?man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'
>>> mo2 = batRegex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'
>>> phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
>>> mo1 = phoneRegex.search('My number is 415-555-4242')
>>> mo1.group()
'415-555-4242'
>>> mo2 = phoneRegex.search('My number is 555-4242')
>>> mo2.group()
'555-4242'
>>> batRegex = re.compile(r'Bat(wo)*man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'
>>> mo2 = batRegex.search('TheAdventures of Batwoman')
>>> mo2.group()
'Batwoman'
>>> mo3 = batRegex.search('The Adventures of Batwowowowoman')
>>> mo3.group()
'Batwowowowoman'
>>> batRegex= re.compile(r'Bat(wo)+man')
>>> mo1 = batRegex.search('The Adventures of Batwoman')
>>> mo1.group()
'Batwoman'
>>> mo2 = batRegex.search('The Adventures of Batwowowoman')
>>> mo2.group()
'Batwowowoman'
>>> mo3 = batRegex.search('The Adventures of Batman')
>>> mo2.group()
'Batwowowoman'
>>> mo3.group()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    mo3.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> mo3 == None
True
>>> 