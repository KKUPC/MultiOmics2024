# MultiOmics2024
---
<div style="display: flex; justify-content: center; align-items: center;">
   <a >
      <img src="./elements/img/PMU-B.png" alt="PMU-B" width="85" height=100% href="https://pmu-hr.or.th">
      <img src="./elements/img/KKU.png" alt="KKU" width="85" height=100% href="https://th.kku.ac.th">
      <img src="./elements/img/MDKKU.png" alt="MD KKU" width="85" height=100% href="https://md.kku.ac.th">
      <img src="./elements/img/Systems%20Biosciences.jpg" alt="Systems Biosciences" width="85" height=100% href="https://www.facebook.com/systemsbiosciences">
      <img src="./elements/img/KKUPC_text.png" alt="AKKUPC" width="85" height=100% href="https://kkuipl.wordpress.com">
      <img src="./elements/img/si-lol.png" alt="Si-LoL" width="85" height=100% href="https://www.longreadlab.com">
      <img src="./elements/img/DMB+logo-color1.png" alt="DMB" width="85" height=100% href="https://www.sidmb.org">
      <img src="./elements/img/SynBio_Consortium_logo.webp" alt="SynBio" width="85" height=100% href="https://www.th-synbioconsortium.com">
      <img src="./elements/img/KUSynBio.jpg" alt="KU-SynBio" width="85" height=100% href="https://www.facebook.com/kusynbio/">
   </a>
</div>

---
# Table of Contents
- [Introduction](#introduction)
- [How to contribute to this repository via GitHub Desktop](#how-to-contribute-to-this-repository-via-gitHub-desktop)
- [How to contribute to this repository via Git commands](#how-to-contribute-to-this-repository-via-git-commands)
- [How to perform document with Mark down language (using .md file)](#how-to-perform-document-with-mark-down-language-using-md-file)

---
# Introduction
This repository is for the MultiOmics2024 course.
Please read the following instructions carefully before you start working on the repository.

---
# How to contribute to this repository via GitHub Desktop
Collaborating on GitHub involves working with others on a shared project. Here's a general guide on how to collaborate using GitHub:

1. **Create a GitHub Account:**
   - If you don't have a GitHub account, sign up at [github.com](https://github.com/)
   - If you already have a GitHub account, log in at [github.com](https://github.com/)

2. **Install GitHub Desktop:**
   - Download and install GitHub Desktop at [desktop.github.com](https://desktop.github.com/).

3. **Clone the Repository:**
   - First step you need to go to local folder where you want to clone the repository.
   For example
   ```bash
   cd /home/username/Documents #you can change the path to any path you want
   ```
   ```bash
   mkdir GitHub; cd GitHub
   ```
   - Clone the repository to your local machine using GitHub Desktop. This creates a local copy of the project.
   - Click on the "Clone a repository from the Internet..." button.
   - Select the "URL" tab and enter the repository URL.
   - Choose the local path where you want to clone the repository.
   - Click on the "Clone" button.

4. **Create a Branch:**
   - Always work in a branch to avoid making changes directly to the main branch. Use the GitHub Desktop interface to create a branch.

     ```bash
     git branch <branch-name>
     git checkout <branch-name>
     ```

     Or, you can use the shorthand:

     ```bash
     git checkout -b <branch-name>
     ```

5. **Make Changes:**
   - Make your changes to the code locally.
   for this step you need to create a new folder with your subject name and add your files there.
   or you can duplicate the template folder `Master` and rename it with your subject name.
   
   to edit `.md` files you can use any text editor or IDE.

6. **Commit Changes:**
   - Commit your changes to your branch. This stages your changes locally.

     ```bash
     git add .
     git commit -m "Your commit message here"
     ```

7. **Push Changes:**
   - Push your branch to the GitHub repository.

     ```bash
     git push origin <branch-name>
     ```

8. **Create a Pull Request (PR):**
   - On the GitHub repository, click on the "New Pull Request" button.
   - Select the base branch (usually `main`) and the branch with your changes.
   - Write a description of your changes and create the pull request.

9. **Code Review:**
   - Collaborators can review your changes and leave comments.

10. **Merge Changes:**
    - If the changes are approved, merge your branch into the main branch through the GitHub interface.

11. **Pull the Latest Changes:**
      - Regularly pull the latest changes from the main branch to your local branch to keep it up-to-date.
   
      ```bash
      git pull origin main
      ```

---

# How to contribute to this repository via Git commands
Collaborating on GitHub involves working with others on a shared project. Here's a general guide on how to collaborate using GitHub:

1. **Create a GitHub Account:**
   - If you don't have a GitHub account, sign up at [github.com](https://github.com/)
   - If you already have a GitHub account, log in at [github.com](https://github.com/)

2. **Clone the Repository:**

   - First step you need to go to local folder where you want to clone the repository.
   For example
   ```bash
   cd /home/username/Documents #you can change the path to any path you want
   ```
   ```bash
   mkdir GitHub; cd GitHub
   ```
   - Clone the repository to your local machine using `git clone` in the command line. This creates a local copy of the project.

     ```bash
     git clone <repository-url>
     ```
     for this project it will be:
     ```bash
       git clone https://github.com/CliNaP/MultiOmics2024.git
     ```
     
3. **Create a Branch:**
   - Always work in a branch to avoid making changes directly to the main branch. Use `git branch` and `git checkout` commands.

     ```bash
     git branch <branch-name>
     git checkout <branch-name>
     ```

     Or, you can use the shorthand:

     ```bash
     git checkout -b <branch-name>
     ```

4. **Make Changes:**
   - Make your changes to the code locally.
   for this step you need to create a new folder with your subject name and add your files there.
   or you can duplicate the template folder `Master` and rename it with your subject name.
   
   to edit `.md` files you can use any text editor or IDE.

5. **Commit Changes:**
   - Commit your changes to your branch. This stages your changes locally.

     ```bash
     git add .
     git commit -m "Your commit message here"
     ```

6. **Push Changes:**
   - Push your branch to the GitHub repository.

     ```bash
     git push origin <branch-name>
     ```

7. **Create a Pull Request (PR):**
   - On the GitHub repository, click on the "New Pull Request" button.
   - Select the base branch (usually `main`) and the branch with your changes.
   - Write a description of your changes and create the pull request.

8. **Code Review:**
   - Collaborators can review your changes and leave comments.

9. **Merge Changes:**
    - If the changes are approved, merge your branch into the main branch through the GitHub interface.

10. **Pull the Latest Changes:**
    - Regularly pull the latest changes from the main branch to your local branch to keep it up-to-date.

     ```bash
     git pull origin main
     ```

Remember that this is a basic workflow, and depending on the project, you might encounter variations such as rebasing, squashing commits, or using forks. Familiarize yourself with Git and GitHub documentation for more advanced collaboration techniques.

---
# How to perform document with Mark down language (using .md file)

1. **Headers:**

   ```markdown
   # Header 1
   ## Header 2
   ### Header 3
   ```

   This creates headers of different levels.

2. **Emphasis:**

   ```markdown
   *italic* or _italic_
   **bold** or __bold__
   ```

   Use asterisks `*` or underscores `_` to make text italic or bold.

3. **Lists:**

   **Unordered List:**

   ```markdown
   - Item 1
   - Item 2
     - Subitem 2.1
   ```

   **Ordered List:**

   ```markdown
   1. First item
   2. Second item
   ```

4. **Links:**

   ```markdown
   [Link Text](http://www.example.com)
   ```

   You can create clickable links.

5. **Images:**

   ```markdown
   ![Alt Text](image-url)
   ```

   Embed images using the above syntax.

6. **Blockquotes:**

   ```markdown
   > This is a blockquote.
   ```

7. **Code:**

   Inline code: \`code\`

   Code block:

   \```
   code block
   \```

   You can specify the language for syntax highlighting after the opening triple backticks, like \```python.

8. **Horizontal Rule:**

   ```markdown
   ---
   ```

   Creates a horizontal rule.

9. **Tables:**

   ```markdown
   | Header 1 | Header 2 |
   | -------- | -------- |
   | Cell 1   | Cell 2   |
   | Cell 3   | Cell 4   |
   ```
   | Header 1 | Header 2 |
   | -------- | -------- |
   | Cell 1   | Cell 2   |
   | Cell 3   | Cell 4   |
   
   Creates a simple table.

11. **Escaping Characters:**

    If you want to display special characters as plain text, you can use the backslash `\` to escape them.

   ```markdown
   \*This is not italic\*
   ```


