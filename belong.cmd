@echo off
cd /d C:\Project_Belong
call C:\Project_Belong\venv\Scripts\activate.bat

set FLASK_APP=belong:create_app
set FLASK_ENV=development

flask run
