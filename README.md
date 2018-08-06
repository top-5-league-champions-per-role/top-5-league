# Top 5 League Champions
Top 5 League Champions per role + their builds and runes.

# How to Use the Git Script
## Pre-Steps:
**NOTE:** You only have to do the following steps ONCE! After the steps are successfully executed, you do not have to do these steps again in your local repository.

1. Clone the repository into your local folder. 
2. Set your 2 config settings
  * `git config --global user.email "your GitHub email here"`
  * `git config --global user.name "your GitHub username here"`

## Actual git-script usage test:
1. Open up your git-bash. In Windows, you can right-click and click on "Open Git-Bash here." If this option is not available, please re-download Git.
2. Type into the git-bash:
```
./push_to_git.sh "Your commit message here"
```
Please make sure you include the double quotes!


# How to Install Kivy (Our GUI Framework)
https://kivy.org/docs/installation/installation-windows.html

# Using Flake8 as a Python linter
http://flake8.pycqa.org/en/latest/
If you are using Atom, you can install Flake8 as an extension. Otherwise, you can type in `flake8 your_python_file.py` and it will print out the lint messages.

# Useful git commands
Git can be downloaded [here](https://git-scm.com/downloads). Useful git commands are:
  1. `git clone github_link_here` - Clone a github directory to your local computer
  2. `git pull` - Use this before you code. Will pull the latest updates to your local directory
  3. `git status` - See all files that you changed.
  4. `git add *` - Add all files that were changed and get them ready to be pushed to the repository.
  5. `git commit -m "insert commit message here"` - Commit the changes while adding a useful comment to what you changed.
  6. `git push` - Push all the committed changes
  7. `git reset hard` - If you screw up, use this to delete EVERYTHING and go back to where you last pulled. WARNING: This WILL delete any changes that you made!
  8. `ls` - List all files in current directory
  9. `cat filename` - Display the contents of <filename> on the terminal.
  10. `cd directory_path` - Change your current directory to directory_path
