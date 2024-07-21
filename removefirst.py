my_list = [1, 2, 3, 4, 5]
first_element = my_list.pop(0)  

print("List after removing the first element:", my_list)
print("Removed element:", first_element)


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
