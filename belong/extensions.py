# belong/extensions.py
"""
프로젝트 전역에서 사용할 Flask Extensions 모음.
- SQLAlchemy
- Migrate
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

