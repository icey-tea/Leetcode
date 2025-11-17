# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. 
# Your task is to transform this absolute path into its simplified canonical path.

# The rules of a Unix-style file system are as follows:

# A single period '.' represents the current directory.
# A double period '..' represents the previous/parent directory.
# Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# Any sequence of periods that does not match the rules above should be treated as a valid directory 
# or file name. For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:

# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to denote current or
# ]parent directories.
# Return the simplified canonical path.

class Solution:
    def simplifyPath(self, path: str) -> str:

        if len(path) == 1:
            return path

        simple = []
        new = path.split('/')

        for i in range(len(new)):
            if new[i] == '..' and simple:
                simple.pop()
            elif new[i] == '..' or new[i] == '.':
                continue
            elif not new[i]:
                continue
            else:
                simple.append(new[i])

        if not simple:
            return ('/')
        else:
            ans = '/' + '/'.join(simple)
        return ans
    
##Big helper was using the or statment in line 3 --> made code run faster
# What we do here is split the word by the '/'
# Then we loop through each portion of the spit text and just apply the rules regarding each non alphanum
# At the end all we do is check if the list is empty and return '/'
#         else we return the joined list, separated by the '/' but starting with a '/'