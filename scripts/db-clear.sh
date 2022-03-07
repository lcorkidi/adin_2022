cd ..
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -name __pycache__ -exec rm -rf {} \;
rm -r db.sqlite3