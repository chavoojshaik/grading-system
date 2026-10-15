(a)
mkdir grading-system
cd grading-system
nano grading.py
nano students.csv
nano test_grading.py
nano README.md
git remote set-url origin git@github.com:chavoojshaik/grading-system.git
git remote -v
git add .
git commit -m "Add initial student grading system"
git status
git push -u origin main

(b)
git branch feature-grading
git branch feature-report
git branch

(c)
git switch feature-grading
nano grading.py
git add grading.py
git commit -m "Improve grading input validation"
git switch feature-report
nano grading.py
git add grading.py
git commit -m "Add student grade report"

(d)
 git switch main
 git merge feature-grading
 git merge feature-report
 git status
 
(e)
 nano grading.py
 git add .
 git commit -m "Merge report feature and resolve grading conflict"
 git log --oneline --graph --all
 
(f)
 nano test_grading.py
 python3 -m unittest discover -v
 git add .
 git commit -m "commit .csv file"
 
(g)
 nano test_grading.py
 python3 -m unittest discover -v
 git add .
git commit -m "Fix integration errors and finalize tests"
git status

(h)
git switch main
git merge feature-grading
git merge feature-report
git status
nano grading.py
git add grading.py
git commit -m "merge report and solve grading conflict"
git status
git push

