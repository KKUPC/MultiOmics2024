# UNIX_101
UNIX practise for HiTech-DS

## Install miniconda 

source: https://docs.conda.io/projects/miniconda/en/latest/


# Download miniconda (for Linux)
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
## Install miniconda
```
bash Miniconda3-latest-Linux-x86_64.sh
```

# install miniconda for Windows
Download: https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

## Install miniconda
```
Miniconda3-latest-Windows-x86_64.exe
```

# install miniconda for Mac
Download: https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg

or
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg
```
## Install miniconda
```
bash Miniconda3-latest-MacOSX-x86_64.pkg
```

# Enveronment management
## Create environment (Python environment)
```
conda create -n unix101 python=3.11
```
## Activate environment
```
conda activate unix101
```
## Deactivate enveroment
```
conda deactivate unix101
```


## 1. Basic commands
### 1.1. pwd
Print working directory
```
pwd
```
### 1.2. ls
List directory contents
``` 
ls
```
### 1.3. cd
Change directory
```
cd ./directory
```
### 1.4. mkdir
Make directory
```
mkdir ./new_directory
```
### 1.5. touch
Create file
```
touch ./new_file
```
### 1.6. cp
Copy file or directory
```
cp /path/to/file /path/to/new/file
```
### 1.7. mv
Move file or directory
```
mv /path/to/file /path/to/new/file
```
### 1.8. rm
Remove file or directory
```
rm /path/to/file
```
### 1.9. cat
Concatenate files and print on the standard output
```
cat /path/to/file
```
### 1.10. less
Opposite of more
```
less /path/to/file
```
### 1.11. head
Output the first part of files
```
head /path/to/file
```
### 1.12. tail
Output the last part of files
```
tail /path/to/file
```
### 1.13. grep
Print lines matching a pattern
```
grep /path/to/file pattern 
```
### 1.14. wc
Print newline, word, and byte counts for each file
```
wc /path/to/file 
```
### 1.15. sort
Sort lines of text files
```
sort /path/to/file 
```
### 1.16. uniq
Report or omit repeated lines
```
uniq /path/to/file
```
### 1.17. cut
Remove sections from each line of files
```
cut /path/to/file
```
### 1.18. paste
Merge lines of files
```
paste /path/to/file
```
### 1.19. join
Join lines of two files on a common field
```
join /path/to/file /path/to/file 
```
### 1.20. diff
Compare files line by line
```
diff /path/to/file /path/to/file 
```
### 1.21. tr
Translate or delete characters
```
tr /path/to/file /path/to/file
```
### 1.22. sed
Stream editor for filtering and transforming text
```
sed /path/to/file /path/to/file
```
### 1.23. awk
Pattern-directed scanning and processing language
```
awk /path/to/file /path/to/file
```
### 1.24. chmod
Change the mode of a file
```
chmod options permissions /path/to/file
```
### 1.25. chown
Change file owner and group
```
chown options owner:group /path/to/file
```
### 1.26. chgrp
Change group ownership
```
chgrp options group /path/to/file 
```
### 1.27. alias
Create an alias
```
alias 
```
### 1.28. source
Execute commands from a file
```
source 
```
### 1.29. history
Command History
```
history 
```
### 1.30. echo
Display a line of text
```
echo 'Hello World'
```
### 1.31. export
Set an environment variable
```
export 'Hello World'
```
### 1.32. env
Display, set, or remove environment variables
```
env
```
### 1.33. date
Display or change the date & time
```
date
```
### 1.34. cal
Display a calendar
```
cal
```
### 1.35. bc
An arbitrary precision calculator language
```
bc
```

## 2. Advanced commands
### 2.1. find
Search for files in a directory hierarchy
```
find
```
### 2.2. locate
Find files by name
```
locate
```
### 2.3. which
Locate a program file in the user's path
```
which
```
### 2.4. tar
Manipulate tape archives
```
tar
```
### 2.5. gzip
Compress or expand files
```
gzip
```
### 2.6. gunzip
Compress or expand files
```
gunzip
```
### 2.7. zcat
Compress or expand files
```
zcat
```
### 2.8. zless
File perusal filter for crt viewing of compressed text
```
zless
```
### 2.9. zgrep
File perusal filter for crt viewing of compressed text
```
zgrep
```
### 2.10. zdiff
File perusal filter for crt viewing of compressed text
```
zdiff
```

## 3. File system
### 3.1. File system
``` 
/
```
### 3.2. Home directory
```
~
```
### 3.3. Current directory
```
.
```
### 3.4. Parent directory
```
..
```
### 3.5. Absolute path
```
/
```

## 4. File permissions
### 4.1. Read
```
r
```
### 4.2. Write
```
w
```
### 4.3. Execute
```
x
```
### 4.4. User
```
u
```
### 4.5. Group
```
g
```
### 4.6. Others
```
o
```
### 4.7. All
```
a
```
### 4.8. Set user ID
```
s
```
### 4.9. Set group ID
```
s
```
### 4.10. Sticky bit
```
t
```

## 5. File types
### 5.1. Regular file
```
-
```
### 5.2. Directory
```
d
```
### 5.3. Symbolic link
```
l
```
### 5.4. Character device
```
c
```
### 5.5. Block device
```
b
```
### 5.6. Named pipe
```
p
```
### 5.7. Socket
```
s
```

## 6. File system hierarchy
### 6.1. /bin
Essential command binaries
```
/bin
```
### 6.2. /boot
Static files of the boot loader
```
/boot
```
### 6.3. /dev
Device files
```
/dev
```
### 6.4. /etc
Host-specific system configuration
```
/etc
```
### 6.5. /home
User home directories
```
/home
```
### 6.6. /lib
Essential shared libraries and kernel modules
```
/lib
```
### 6.7. /media
Mount point for removable media
```
/media
```
### 6.8. /mnt
Mount point for mounting a filesystem temporarily
```
/mnt
```
### 6.9. /opt
Add-on application software packages
```
/opt
```
### 6.10. /proc
Virtual filesystem providing process and kernel information as files
```
/proc
```
### 6.11. /root
Home directory for the root user
```
/root
```
### 6.12. /run
Run-time variable data
```
/run
```
### 6.13. /sbin
Essential system binaries
```
/sbin
```
### 6.14. /srv
Site-specific data served by this system
```
/srv
```
### 6.15. /sys
Contains information about devices, drivers, and some kernel features
```
/sys
```
### 6.16. /tmp
Temporary files
```
/tmp
```
### 6.17. /usr
Secondary hierarchy for read-only user data
```
/usr
```
### 6.18. /var
Variable data
```
/var
```

## 8. github
### 8.1. git clone
Clone a repository into a new directory
```
git clone
```
### 8.2. git add
Add file contents to the index
```
git add
```
### 8.3. git commit
Record changes to the repository
```
git commit
```
### 8.4. git push
Update remote refs along with associated objects
```
git push
```
### 8.5. git pull
Fetch from and integrate with another repository or a local branch
```
git pull
```
### 8.6. git status
Show the working tree status
```
git status
```
### 8.7. git log
Show commit logs
```
git log
```
### 8.8. git branch
List, create, or delete branches
```
git branch
```
### 8.9. git checkout
Switch branches or restore working tree files
```
git checkout
```
### 8.10. git merge
Join two or more development histories together
```
git merge
```
### 8.11. git reset
Reset current HEAD to the specified state
```
git reset
```
### 8.12. git revert
Revert some existing commits
```
git revert
```
### 8.13. git stash
Stash the changes in a dirty working directory away
```
git stash
```
### 8.14. git tag
Create, list, delete or verify a tag object signed with GPG
```
git tag
```
### 8.15. git show
Show various types of objects
```
git show
```
### 8.16. git fetch
Download objects and refs from another repository
```
git fetch
```
### 8.17. git remote
Manage set of tracked repositories
```
git remote
```
### 8.18. git diff
Show changes between commits, commit and working tree, etc
```
git diff
```
### 8.19. git config
Get and set repository or global options
```
git config
```
### 8.20. git init
Create an empty Git repository or reinitialize an existing one
```
git init
```
### 8.21. git rm
Remove files from the working tree and from the index
```
git rm
```
### 8.22. git mv
Move or rename a file, a directory, or a symlink
```
git mv
```
### 8.23. git grep
Print lines matching a pattern
```
git grep
```
### 8.24. gitk
The Git repository browser
```
gitk
```
### 8.25. git gui
A portable graphical interface to Git
```
git gui
```
### 8.26. git config
Get and set repository or global options
```
git config
```
### 8.27. git blame
Show what revision and author last modified each line of a file
```
git blame
```

## 9. nano
### 9.1. nano
Nano's ANOther editor, an enhanced free Pico clone
```
nano
```
### 9.2. Ctrl + O
Write out the current file contents
```
Ctrl + O
```
### 9.3. Ctrl + X
Exit nano
```
Ctrl + X
```
### 9.4. Ctrl + G
Display the help text
```
Ctrl + G
```
### 9.5. Ctrl + K
Cut the current line and store it in the cutbuffer
```
Ctrl + K
```
### 9.6. Ctrl + U
Uncut from the cutbuffer into the current line
```
Ctrl + U
```
### 9.7. Ctrl + W
Search for a string or a regular expression
```
Ctrl + W
```
### 9.8. Ctrl + C
Display current cursor position
```
Ctrl + C
```
### 9.9. Ctrl + \
Search and replace
```
Ctrl + \
```
### 9.10. Ctrl + T
Check spelling of the current file
```
Ctrl + T
```
### 9.11. Ctrl + J
Justify the current paragraph
```
Ctrl + J
```
### 9.12. Ctrl + R
Insert another file into the current one
```
Ctrl + R
```
### 9.13. Ctrl + Y
Move to the previous screen
```
Ctrl + Y
```
### 9.14. Ctrl + V
Move to the next screen
```
Ctrl + V
```
### 9.15. Ctrl + _
Go to line and column number
```
Ctrl + _
```
### 9.16. Ctrl + A
Go to the beginning of the current line
```
Ctrl + A
```
### 9.17. Ctrl + E
Go to the end of the current line
```
Ctrl + E
```
### 9.18. Ctrl + P
Move to the previous line
```
Ctrl + P
```
### 9.19. Ctrl + N
Move to the next line
```
Ctrl + N
```
### 9.20. Ctrl + F
Move forward one character
```
Ctrl + F
```
### 9.21. Ctrl + B
Move backward one character
```
Ctrl + B
```
### 9.22. Ctrl + Space
Set the mark
```
Ctrl + Space
```
### 9.23. Alt + Space
Move to the previous word
```
Alt + Space
```
### 9.24. Alt + 6
Copy the current line and store it in the cutbuffer
```
Alt + 6
```
### 9.25. Alt + 7
Cut the current line and store it in the cutbuffer
```
Alt + 7
```
### 9.26. Alt + 8
Paste the cutbuffer into the current line
```
Alt + 8
```
### 9.27. Alt + U
Undo the last operation
```
Alt + U
```



