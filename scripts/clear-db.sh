find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm - rf
rm -r db.sqlite3