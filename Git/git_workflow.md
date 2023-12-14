# Git work-flow
1. **Clone the Repository:**
   ```bash
   $ git clone <repository-url>
   ```
   Clone the repository to your local machine.

2. **Create a New Branch:**
   ```bash
   $ git checkout -b <branch-name>
   ```
   Create a new branch for your feature or bug fix.

3. **Make Changes:**
   Make the necessary changes to the codebase.

4. **Add Changes:**
   ```bash
   $ git add .
   ```
   Stage the changes you want to commit.

5. **Commit Changes:**
   ```bash
   $ git commit -m "Your descriptive commit message"
   ```
   Commit your changes with a meaningful message.

6. **Push Changes to Remote:**
   ```bash
   $ git push origin <branch-name>
   ```
   Push your branch and make changes to the remote repository.

7. **Merge Changes:**
   - Visit the repository on the Git hosting platform `GitHub Desktop`, or (https://github.com).
   - Create a pull request or merge request from your branch.
   - Review changes, and discuss with collaborators if needed.
   - Merge the changes into the main branch.

This straightforward workflow works well for individual contributors working on feature branches. It's a good practice to create a branch for each logical unit of work to keep changes isolated and easily manageable. The merge step typically involves collaboration and code review before integrating changes into the main branch.

