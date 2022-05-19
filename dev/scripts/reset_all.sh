#!/bin/bash -i

cwd=$(pwd)
# echo "Entering app directory..."
cd ${APPDIR}

echo 'Resetting db...'
python manage.py reset_db --noinput

echo "Cleaning pyc files..."
python manage.py clean_pyc

echo "Clearing cache..."
python manage.py clear_cache

echo 'Clearing migrations folders...'
rm -r */migrations/0* \
      */__pycache__ \
      */*/__pycache__ \
      *.sqlite3

# echo "Leaving app directory"
cd ${cwd} 
