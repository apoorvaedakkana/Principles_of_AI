# Python program to find the sum of natural using recursive function

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num = 16

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))



## Experiment No. 01: Setting Up and Basic Commands

# Initialize a new Git repository
# git init

# Create a new file and add it to the staging area
# touch filename.txt
# git add filename.txt

# Commit the changes
# git commit -m "Initial commit"

# Push the changes to a remote repository
# git push origin main


## Experiment No. 02: Creating and Managing Branches

# Create a new branch and switch to it
# git branch feature-branch
# git checkout feature-branch

# Add and commit changes
# git add .
# git commit -m "Add new feature"

# Switch to the master branch and merge changes
# git checkout master
# git merge feature-branch

# Stash changes, switch branches, and apply stashed changes
# git stash
# git checkout feature-branch
# git stash apply


## Experiment No. 03: Collaboration and Remote Repositories

# Clone a remote repository
# git clone <repository_url>

# Create and switch to a new branch
# git checkout -b feature-branch

# Fetch the latest changes and rebase
# git fetch origin
# git rebase origin/<branch_name>

# Merge feature branch into master with a custom commit message
# git checkout master
# git merge --no-ff feature-branch -m "Custom commit message"


