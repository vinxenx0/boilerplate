python3 -m venv .venv
source .venv/bin/activate

pip install flask flask-sqlalchemy flask-login flask-migrate flask-wtf flask-bootstrap pytest python-dotenv

flask db init
flask db migrate -m "Inicializar base de datos"
flask db upgrade

python run.py
