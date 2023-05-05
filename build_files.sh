# build_files.sh
pip install --upgrade pip
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
