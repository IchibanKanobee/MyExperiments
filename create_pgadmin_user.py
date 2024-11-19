# Run with sudo python
from pgadmin4 import create_app
from pgadmin4.setup import setup_db, create_user

app = create_app()
with app.app_context():
    setup_db()
    create_user('admin@admin.com', 'admin')

