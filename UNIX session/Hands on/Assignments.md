

**Assignment 1: File and Directory Basics**

**Objective:** To practice basic file and directory manipulation commands.

**Instructions:**

1. Create a directory named "unix_assignment" in your home directory.

2. Inside "unix_assignment," create the following files:
   - `file1.txt`
   - `file2.txt`
   - `file3.txt`

3. Rename `file2.txt` to `renamed_file.txt`.

4. List the contents of the "unix_assignment" directory.

**Answers:**

```bash
# Navigate to the home directory
cd ~

# Create the directory
mkdir unix_assignment

# Change into the directory
cd unix_assignment

# Create files
touch file1.txt file2.txt file3.txt

# Rename a file
mv file2.txt renamed_file.txt

# List directory contents
ls
```

---

**Assignment 2: Text File Manipulation**

**Objective:** To practice basic text file manipulation commands.

**Instructions:**

1. Create a new file named "mytext.txt" and add the following text:
   ```
   This is a sample text file.
   Welcome to UNIX.
   ```

2. Display the contents of "mytext.txt."

3. Append the text "UNIX is powerful!" to "mytext.txt."

4. Display the modified contents of "mytext.txt."

**Answers:**

```bash
# Create and edit the file
echo "This is a sample text file." > mytext.txt
echo "Welcome to UNIX." >> mytext.txt

# Display file contents
cat mytext.txt

# Append text to the file
echo "UNIX is powerful!" >> mytext.txt

# Display modified contents
cat mytext.txt
```

---

**Assignment 3: File Deletion and Cleanup**

**Objective:** To practice file and directory deletion commands.

**Instructions:**

1. Remove the file "file1.txt."

2. Create a directory named "temp" inside "unix_assignment."

3. Remove the entire "temp" directory and its contents.

**Answers:**

```bash
# Remove a file
rm file1.txt

# Create a directory
mkdir temp

# Remove a directory and its contents
rm -r temp
```

---

**Assignment 4: Process Management**

**Objective:** To practice basic process management commands.

**Instructions:**

1. Open a terminal and run a command (e.g., `sleep 60`) in the background.

2. List all running processes.

3. Terminate the background process you started in step 1.

**Answers:**

```bash
# Run a command in the background
sleep 60 &

# List all running processes
ps aux

# Terminate the background process (replace [PID] with the actual process ID)
kill [PID]
```

---

**Assignment 5: File Permissions**

**Objective:** To practice file permission manipulation.

**Instructions:**

1. Create a new file named "secret.txt" in "unix_assignment."

2. Change the permissions of "secret.txt" so that only the owner can read and write to it.

3. Attempt to open "secret.txt" using a different user or switch to a different user to verify the permissions.

**Answers:**

```bash
# Create the file
touch secret.txt

# Change permissions (read and write only for the owner)
chmod 600 secret.txt

# Attempt to open the file as a different user (replace [username] with the actual username)
su [username]
cat secret.txt
```

---

**Assignment 6: File Compression**

**Objective:** To practice file compression and decompression.

**Instructions:**

1. Create a new directory named "compressed" in "unix_assignment."

2. Compress the "compressed" directory into a file named "compressed.tar.gz."

3. Decompress "compressed.tar.gz" into a directory named "decompressed."

**Answers:**

```bash
# Create the directory
mkdir compressed

# Compress the directory
tar -czvf compressed.tar.gz compressed

# Decompress the file
tar -xzvf compressed.tar.gz
```

---

**Assignment 7: File Transfer**

**Objective:** To practice file transfer between local and remote machines.

**Instructions:**

1. Create a new directory named "transfer" in "unix_assignment."

2. Transfer the "transfer" directory to a remote machine using `scp`.

3. Transfer the "transfer" directory to a remote machine using `rsync`.

**Answers:**

```bash
# Create the directory
mkdir transfer

# Transfer using scp
scp -r transfer [username]@[hostname]:/path/to/destination

# Transfer using rsync
rsync -avz transfer [username]@[hostname]:/path/to/destination
```

---

**Assignment 8: File Searching**

**Objective:** To practice file searching using `find` and `grep`.

**Instructions:**

1. Create a new directory named "search" in "unix_assignment."

2. Create a new file named "search.txt" in "search" and add the following text:
   ```
   This is a sample text file.
   Welcome to UNIX.
   UNIX is powerful!
   ```
3. Search for all files named "search.txt" in "unix_assignment."

4. Search for all files containing the word "UNIX" in "unix_assignment."

**Answers:**

```bash
# Create the directory
mkdir search

# Create and edit the file
echo "This is a sample text file." > search/search.txt
echo "Welcome to UNIX." >> search/search.txt
echo "UNIX is powerful!" >> search/search.txt

# Search for files
find unix_assignment -name search.txt

# Search for text
grep -r UNIX unix_assignment
```

---

**Assignment 9: File Editing**

**Objective:** To practice file editing using `sed` and `awk`.

**Instructions:**

1. Create a new file named "edit.txt" in "unix_assignment" and add the following text:
   ```
   This is a sample text file.
   Welcome to UNIX.
   UNIX is powerful!
   ```
2. Replace all occurrences of "UNIX" with "Linux" in "edit.txt."

3. Display the first line of "edit.txt."

4. Display the last line of "edit.txt."

**Answers:**

```bash
# Create and edit the file
echo "This is a sample text file." > edit.txt
echo "Welcome to UNIX." >> edit.txt
echo "UNIX is powerful!" >> edit.txt

# Replace text
sed -i 's/UNIX/Linux/g' edit.txt

# Display the first line
head -n 1 edit.txt

# Display the last line
tail -n 1 edit.txt
```

---

**Assignment 10: File Sorting**

**Objective:** To practice file sorting using `sort` and `uniq`.

**Instructions:**

1. Create a new file named "sort.txt" in "unix_assignment" and add the following text:
   ```
   This is a sample text file.
   Welcome to UNIX.
   UNIX is powerful!
   ```
2. Sort the lines of "sort.txt" in alphabetical order.

3. Sort the lines of "sort.txt" in reverse alphabetical order.

4. Sort the lines of "sort.txt" in reverse alphabetical order and remove duplicate lines.

**Answers:**

```bash
# Create and edit the file
echo "This is a sample text file." > sort.txt
echo "Welcome to UNIX." >> sort.txt
echo "UNIX is powerful!" >> sort.txt

# Sort in alphabetical order
sort sort.txt

# Sort in reverse alphabetical order
sort -r sort.txt

# Sort in reverse alphabetical order and remove duplicates
sort -r sort.txt | uniq
```

---

**Assignment 11: File Statistics**

**Objective:** To practice file statistics using `wc` and `du`.

**Instructions:**

1. Create a new file named "stats.txt" in "unix_assignment" and add the following text:
   ```
   This is a sample text file.
   Welcome to UNIX.
   UNIX is powerful!
   ```
2. Display the number of lines in "stats.txt."

3. Display the number of words in "stats.txt."

4. Display the number of characters in "stats.txt."

5. Display the size of "stats.txt."

**Answers:**

```bash
# Create and edit the file
echo "This is a sample text file." > stats.txt
echo "Welcome to UNIX." >> stats.txt
echo "UNIX is powerful!" >> stats.txt

# Display the number of lines
wc -l stats.txt

# Display the number of words
wc -w stats.txt

# Display the number of characters
wc -c stats.txt

# Display the size
du -h stats.txt
```

---

**Assignment 12: File Permissions**

**Objective:** To practice file permission manipulation.

**Instructions:**

1. Create a new file named "permissions.txt" in "unix_assignment."

2. Change the permissions of "permissions.txt" so that only the owner can read and write to it.

3. Attempt to open "permissions.txt" using a different user or switch to a different user to verify the permissions.

**Answers:**

```bash
# Create the file
touch permissions.txt

# Change permissions (read and write only for the owner)
chmod 600 permissions.txt

# Attempt to open the file as a different user (replace [username] with the actual username)
su [username]
cat permissions.txt
```

---

**Assignment 13: Creat a Shell Script**

**Objective:** To practice shell scripting.

**Instructions:**

1. Create a new file named "script.sh" in "unix_assignment" and add the following text:
   ```bash
   #!/bin/bash
   echo "Hello, world!"
   ```
2. Make "script.sh" executable.

3. Run "script.sh."

**Answers:**

```bash
# Create and edit the file
echo '#!/bin/bash' > script.sh
echo 'echo "Hello, world!"' >> script.sh

# Make the file executable
chmod +x script.sh

# Run the script
./script.sh
```

---

**Assignment 14: Create a Shell Script with Arguments**

**Objective:** To practice shell scripting with arguments.

**Instructions:**

1. Create a new file named "script.sh" in "unix_assignment" and add the following text:
   ```bash
   #!/bin/bash
   echo "Hello, $1!"
   ```
2. Make "script.sh" executable.

3. Run "script.sh" with your name as an argument.

**Answers:**

```bash
# Create and edit the file
echo '#!/bin/bash' > script.sh
echo 'echo "Hello, $1!"' >> script.sh

# Make the file executable
chmod +x script.sh

# Run the script
./script.sh [your name]
```

---

**Assignment 15: Create a Shell Script with User Input**

**Objective:** To practice shell scripting with user input.

**Instructions:**

1. Create a new file named "script.sh" in "unix_assignment" and add the following text:
   ```bash
   #!/bin/bash
   echo "What is your name?"
   read name
   echo "Hello, $name!"
   ```
2. Make "script.sh" executable.

3. Run "script.sh."

**Answers:**

```bash
# Create and edit the file
echo '#!/bin/bash' > script.sh
echo 'echo "What is your name?"' >> script.sh
echo 'read name' >> script.sh
echo 'echo "Hello, $name!"' >> script.sh

# Make the file executable
chmod +x script.sh

# Run the script
./script.sh
```

---

**Assignment 16: Create a Shell Script with Conditional Logic**

**Objective:** To practice shell scripting with conditional logic.

**Instructions:**

1. Create a new file named "script.sh" in "unix_assignment" and add the following text:
   ```bash
   #!/bin/bash
   echo "What is your name?"
   read name
   if [ "$name" == "John" ]; then
     echo "Hello, John!"
   else
     echo "Hello, $name!"
   fi
   ```

2. Make "script.sh" executable.

3. Run "script.sh" with your name as an argument.

**Answers:**

```bash
# Create and edit the file
echo '#!/bin/bash' > script.sh
echo 'echo "What is your name?"' >> script.sh
echo 'read name' >> script.sh
echo 'if [ "$name" == "John" ]; then' >> script.sh
echo '  echo "Hello, John!"' >> script.sh
echo 'else' >> script.sh
echo '  echo "Hello, $name!"' >> script.sh
echo 'fi' >> script.sh

# Make the file executable
chmod +x script.sh

# Run the script
./script.sh [your name]
```

---

**Assignment 17: Create a Shell Script with a Loop**

**Objective:** To practice shell scripting with a loop.

**Instructions:**

1. Create a new file named "script.sh" in "unix_assignment" and add the following text:
   ```bash
   #!/bin/bash
   for i in {1..10}
   do
     echo "Hello, world!"
   done
   ```

2. Make "script.sh" executable.

3. Run "script.sh."

**Answers:**

```bash
# Create and edit the file

echo '#!/bin/bash' > script.sh
echo 'for i in {1..10}' >> script.sh
echo 'do' >> script.sh
echo '  echo "Hello, world!"' >> script.sh
echo 'done' >> script.sh

# Make the file executable
chmod +x script.sh

# Run the script
./script.sh
```

---

**Assignment 18: Create a Shell Script with a Function**

**Objective:** To practice shell scripting with a function.

**Instructions:**

1. Create a new file named "script.sh" in "unix_assignment" and add the following text:
   ```bash
   #!/bin/bash
   function hello {
     echo "Hello, world!"
   }
   hello
   ```

2. Make "script.sh" executable.

3. Run "script.sh."

**Answers:**

```bash
# Create and edit the file
echo '#!/bin/bash' > script.sh
echo 'function hello {' >> script.sh
echo '  echo "Hello, world!"' >> script.sh
echo '}' >> script.sh
echo 'hello' >> script.sh

# Make the file executable
chmod +x script.sh

# Run the script
./script.sh
```

---

**Assignment 19: Create a Shell Script with an sequence of commands and arguments**

**Objective:** To practice shell scripting with an sequence of commands and arguments.

**Instructions:**

1. Create a new file named "script.sh" in "unix_assignment" and add the following text:
   ```bash
   #!/bin/bash
   echo "What is your name?"
   read name
   if [ "$name" == "John" ]; then
     echo "Hello, John!"
   else
     echo "Hello, $name!"
   fi
   ```

2. Make "script.sh" executable.

3. Run "script.sh" with your name as an argument.

**Answers:**

```bash
# Create and edit the file
echo '#!/bin/bash' > script.sh
echo 'echo "What is your name?"' >> script.sh
echo 'read name' >> script.sh
echo 'if [ "$name" == "John" ]; then' >> script.sh
echo '  echo "Hello, John!"' >> script.sh
echo 'else' >> script.sh
echo '  echo "Hello, $name!"' >> script.sh
echo 'fi' >> script.sh

# Make the file executable
chmod +x script.sh

# Run the script
./script.sh [your name]
```

---

**Assignment 20: Create a Shell Script with a Loop and conditional logic function**

**Objective:** To practice shell scripting with a loop and conditional logic function.

**Instructions:**

1. Create a new file named "script.sh" in "unix_assignment" and add the following text:
   ```bash
   #!/bin/bash
   function hello {
     echo "Hello, world!"
   }
   for i in {1..10}
   do
     hello
   done
   ```

2. Make "script.sh" executable.

3. Run "script.sh."

**Answers:**

```bash

# Create and edit the file
echo '#!/bin/bash' > script.sh
echo 'function hello {' >> script.sh
echo '  echo "Hello, world!"' >> script.sh
echo '}' >> script.sh
echo 'for i in {1..10}' >> script.sh
echo 'do' >> script.sh
echo '  hello' >> script.sh
echo 'done' >> script.sh

# Make the file executable
chmod +x script.sh

# Run the script
./script.sh
```

---


