cd ..
find . -name *_initial.py -delete
find . -name __pycache__ -exec rm -rf {} \;
rm -r db.sqlite3