# belong/__init__.py

from flask import Flask

from belong.extensions import db, migrate     # ⭐ migrate 반드시 import
from belong.config import *                  # 환경 설정 불러오기

def create_app():
    app = Flask(__name__)
    app.config.from_object("belong.config")

    # --------------------------
    # 핵심: DB & Migration 연결
    # --------------------------
    db.init_app(app)
    migrate.init_app(app, db)

    # --------------------------
    # Blueprint 등록
    # --------------------------
    from belong.views.auth_views import bp as auth_bp
    from belong.views.main_views import bp as main_bp
    from belong.views.question_views import bp as question_bp
    from belong.views.predict_views import bp as predict_bp
    from belong.views.correlation_views import bp as correlation_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(question_bp)
    app.register_blueprint(predict_bp)
    app.register_blueprint(correlation_bp)
    return app
