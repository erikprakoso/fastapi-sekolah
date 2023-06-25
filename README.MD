FASTAPI + POSTGRESQL

CARA RUNNING
cd /app
source ../venv/bin/active
pip install -r requirements.txt #PERTAMA KALI CLONE
uvicorn main:app --reload

DATABASE
tidak perlu membuat table
otomatis di create oleh framework