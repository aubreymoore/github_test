cd /home/aubrey/Desktop/git_test
source .venv/bin/activate
# /home/aubrey/Desktop/git_test/.venv/bin/python /home/aubrey/Desktop/git_test/test.py
python test.py
git pull
git add .
git commit -m 'added by gitpush.sh'
git push
