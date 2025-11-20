# belong/config.py

import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = "oracle+cx_oracle://scott:tiger@localhost:1521/xe"

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev-secret-key"
