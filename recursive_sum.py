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


## Experiment No. 04: Git Tags and Releases

# View commit history
# git log

# Create a lightweight tag
# git tag v1.0 <commit_id>

# Show the tag details
# git show v1.0

# Push the tag to a remote repository
# git push origin v1.0


## Experiment No. 05: Advanced Git Operations

# Create and switch to a source branch, make changes, add, and commit
# git checkout -b source-branch
# touch filename.txt
# git add filename.txt
# git commit -m "Add file for cherry-pick example"

# Switch to the main branch and cherry-pick a commit
# git checkout main
# git cherry-pick <commit_hash>

# Cherry-pick a range of commits
# git cherry-pick <commit_hash_start>..<commit_hash_end>

# Continue cherry-pick after resolving conflicts
# git cherry-pick --continue


## Experiment No. 06: Analyzing and Changing Git History

# View details of a specific commit
# git show <commit_id>

# List commits by a specific author within a date range
# git log --author="JohnDoe" --after="2023-01-01" --before="2023-12-31"

# Display the last five commits
# git log -n 5

# Undo changes introduced by a specific commit
# git revert abc123
