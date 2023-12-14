
# Git Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Configuration](#configuration)
3. [Basic Git Concepts](#basic-git-concepts)
    - [Repositories](#repositories)
    - [Commits](#commits)
    - [Branches](#branches)
4. [Working with Git](#working-with-git)
    - [Cloning a Repository](#cloning-a-repository)
    - [Making Changes](#making-changes)
    - [Staging Changes](#staging-changes)
    - [Committing Changes](#committing-changes)
    - [Pushing Changes](#pushing-changes)
5. [Branching and Merging](#branching-and-merging)
    - [Creating a Branch](#creating-a-branch)
    - [Switching Branches](#switching-branches)
    - [Merging Branches](#merging-branches)
    - [Resolving Conflicts](#resolving-conflicts)
6. [Collaboration](#collaboration)
    - [Pull Requests](#pull-requests)
    - [Forking](#forking)
    - [Pulling Changes](#pulling-changes)
    - [Pushing to Remote](#pushing-to-remote)
7. [Git Best Practices](#git-best-practices)
    - [Commit Messages](#commit-messages)
    - [Branch Naming](#branch-naming)
    - [Git Ignore](#git-ignore)
    - [Interactive Rebase](#interactive-rebase)
8. [Troubleshooting](#troubleshooting)
    - [Undoing Changes](#undoing-changes)
    - [Resetting Branch](#resetting-branch)
    - [Git Log](#git-log)
9. [Advanced Topics](#advanced-topics)
    - [Submodules](#submodules)
    - [Git Hooks](#git-hooks)
    - [Git Workflows](#git-workflows)

## 1. Introduction <a name="introduction"></a>
Git is a distributed version control system that helps in tracking changes in source code during software development. This document provides a guide on using Git for version control in collaborative projects.

## 2. Getting Started <a name="getting-started"></a>

### Installation <a name="installation"></a>
To install Git, visit [Git Download Page](https://git-scm.com/downloads) and follow the installation instructions for your operating system.

### Configuration <a name="configuration"></a>
After installation, configure Git with your name and email:
```bash
$ git config --global user.name "Your Name"
$ git config --global user.email "your.email@example.com"
```

## 3. Basic Git Concepts <a name="basic-git-concepts"></a>

### Repositories <a name="repositories"></a>
A Git repository is a collection of files and the history of their changes. Create a new repository with:
```bash
$ git init
```

### Commits <a name="commits"></a>
A commit represents a snapshot of changes. Use:
```bash
$ git commit -m "Your commit message"
```

### Branches <a name="branches"></a>
Branches are independent lines of development. Create a new branch:
```bash
$ git branch new-feature
```

## 4. Working with Git <a name="working-with-git"></a>

### Cloning a Repository <a name="cloning-a-repository"></a>
Clone a repository to your local machine:
```bash
$ git clone <repository-url>
```

### Making Changes <a name="making-changes"></a>
Make changes to files in your working directory.

### Staging Changes <a name="staging-changes"></a>
Stage changes for commit:
```bash
$ git add <filename>
```

### Committing Changes <a name="committing-changes"></a>
Commit staged changes:
```bash
$ git commit -m "Your commit message"
```

### Pushing Changes <a name="pushing-changes"></a>
Push changes to the remote repository:
```bash
$ git push origin <branch-name>
```

## 5. Branching and Merging <a name="branching-and-merging"></a>

### Creating a Branch <a name="creating-a-branch"></a>
Create a new branch:
```bash
$ git branch <branch-name>
```

### Switching Branches <a name="switching-branches"></a>
Switch to a branch:
```bash
$ git checkout <branch-name>
```

### Merging Branches <a name="merging-branches"></a>
Merge changes from one branch to another:
```bash
$ git merge <branch-name>
```

### Resolving Conflicts <a name="resolving-conflicts"></a>
Resolve merge conflicts and commit changes.

## 6. Collaboration <a name="collaboration"></a>

### Pull Requests <a name="pull-requests"></a>
Create pull requests to propose changes.

### Forking <a name="forking"></a>
Fork a repository to create a personal copy.

### Pulling Changes <a name="pulling-changes"></a>
Pull changes from a remote repository:
```bash
$ git pull origin <branch-name>
```

### Pushing to Remote <a name="pushing-to-remote"></a>
Push changes to a remote repository:
```bash
$ git push origin <branch-name>
```

## 7. Git Best Practices <a name="git-best-practices"></a>

### Commit Messages <a name="commit-messages"></a>
Write clear and concise commit messages.

### Branch Naming <a name="branch-naming"></a>
Follow a consistent branch naming convention.

### Git Ignore <a name="git-ignore"></a>
Use a `.gitignore` file to exclude files from version control.

### Interactive Rebase <a name="interactive-rebase"></a>
Rewrite commit history with interactive rebase.

## 8. Troubleshooting <a name="troubleshooting"></a>

### Undoing Changes <a name="undoing-changes"></a>
Undo changes in working directory:
```bash
$ git checkout -- <filename>
```

### Resetting Branch <a name="resetting-branch"></a>
Reset branch to a specific commit:
```bash
$ git reset --hard <commit-hash>
```

### Git Log <a name="git-log"></a>
View commit history:
```bash
$ git log
```

## 9. Advanced Topics <a name="advanced-topics"></a>

### Submodules <a name="submodules"></a>
Manage submodules for external dependencies.

### Git Hooks <a name="git-hooks"></a>
Use Git hooks for custom workflows.

### Git Workflows <a name="git-workflows"></a>
Explore different Git workflows (e.g., Gitflow, GitHub Flow).

---

