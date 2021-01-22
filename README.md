# nocommit
Python script to look for '//nocommit' comments in my code so I don't accidentally push bad code to github. Inspired by Jon Blow's svn 'nocheckin'.

## Instructions
It's fairly simple to use, all you do is run the script in the highest level of the project directory you are working in and it will look for your specified word (default is "//nocommit"). 

If you want to change the word or phrase it searches for, all you have to do is change the line: 

```python

if '//nocommit' in line:

```
You can also change the file type it searches through by changing:

```python

if name.endswith('.cpp'):

```
