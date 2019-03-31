#!/usr/bin/env python
# coding: utf-8

# ## pathlib
# * [pathlib docs](https://docs.python.org/3/library/pathlib.html)
# * [Practical Business Python: Using Python's Pathlib module](https://pbpython.com/pathlib-intro.html)
# * [PEP 428: The pathlib module](https://www.python.org/dev/peps/pep-0428/)
# 
# File handling operations to check for the existence of a file and such are handled in a variety of built-in libraries, such as ``os``, ``os.path`` and ``shutil``. Traditionally in Python you'd have to hunt around to find which library provided what functionality. This is a legacy of C-based APIs and is not at all Pythonic, in that we'd expect a file object that handles all this stuff in one place.
# 
# All that functionality is still there in those various libraries, but as of Python 3.4, there is now the ``pathlib`` library which provides a file object (``Path``) in the manner that you'd expect. I strongly recommend using this libary, as I've found it has a significant impact on cleaning up code and making code more intuitive and Pythonic.
# 
# This is the standard way to import the Path object:

# In[14]:


from pathlib import Path
from helping import info

info(Path)


# ### Creating Paths
# Creating a ``Path`` object with no arguments gives you a ``Path`` object for the *current working directory*. The ``absolute()`` method prints the absolute version of the path (that is, any links are resolved so you get the true path for the file):

# In[15]:


path = Path()
print(path.absolute())


# To get a file in the current working directory, you can just use the filename:

# In[16]:


path = Path('stanford.txt')
print(path.absolute())


# One of the nice features of ``Path`` is how easy it is to build up a path by simply passing multiple arguments when you create the ``Path`` object:

# In[17]:


path = Path('/tmp', 'mydir', 'file.txt')
print(path.absolute())


# You can also use Path objects to build up the path:

# In[18]:


root = Path('input')

path = Path(root, 'data.csv')

print(path.absolute())


# ### Working with files
# Here are some common operations with Paths:

# In[22]:


path = Path('stanford.txt')
print(path.exists())
print(path.is_dir())


# In[23]:


print(path.read_text())


# ``Path.open()`` is the equivalent of calling the ``open()`` function:

# In[ ]:


for line in path.open():
    print(line)


# In[ ]:


path = Path('output.txt')
path.write_text("Hello, this is my output!")


# In[ ]:


print(path.read_text())


# ### Working with directories
# Use ``iterdir()`` to iterate over a single directory:

# In[ ]:


path = Path()

for item in path.iterdir():
    print(item)


# Use ``glob()`` to list items in a directory that match a pattern:

# In[ ]:


for item in path.glob('*.py'):
    print(item)


# Use ``mkdir()`` to create a directory. Passing ``parents=True`` causes all missing segments of the path to be created, and ``exist_ok=True`` doesn't raise an error if the directory already exists, both of which are usually what you want:

# In[ ]:


newdir = Path(path, 'new_dir')
newdir.mkdir(parents=True, exist_ok=True)

print(newdir.exists())


# To walk through all files in a directory structure, use ``glob()`` with the pattern ``**/*.*``:

# In[ ]:


for item in path.glob('**/*.*'):
    print(item)


# ## Exercise: ex_3_lines.py
# 1. Print out the contents of ``stanford.txt``.
# 
# 2. How many lines are in the file?
# 
# 3. How many words are in the file? (Hint: There's a string method that will help with this...)

# In[ ]:


with open('stanford.txt', 'r', errors = "ignore") as file:
    data = file.read()
    print(data)


# In[ ]:


num_lines = sum(1 for line in open('stanford.txt', errors ="ignore"))
print(num_lines)
count = sum(1 for line in data if line == '\n')
print(count)

# Answer to number two. last line in the file doesnt contain a carriage return, so its 52 on that count instead of 53. 


# In[ ]:


print("Character count is: ", len(data))
list1 = data.split()
print("Total word count is: ", len(list1))
print("Total unique words is: ",len(set(list1)), end = "\n \n")
for item in list1:
    print(item)


# ## Exercise: ex_4_home.py
# 
# Using ``pathlib.Path``, answer these questions:
# 
# 1. How many files (not directories!) are in your home directory?
# 2. How many directories (not files!) are in your home directory?
# 
# *Hint: You'll need to look at the info() for Path to see how to get your home directory...*

# In[ ]:


import pathlib
from os import path
import helping
help(pathlib.Path.is_file)


# In[ ]:


home = pathlib.Path.home()
files, dirs = 0, 0
for item in pathlib.Path.iterdir(home):
    if pathlib.Path.is_file(item):
        files +=1
    if pathlib.Path.is_dir(item):
        dirs +=1
print(f'You have {files} files and {dirs} directories.')


# In[ ]:


type(pathlib.Path())


# In[ ]:




