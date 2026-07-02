@echo off

set PYTHON=.\.venv\Scripts\python.exe

watchmedo auto-restart --patterns="*.py" --recursive -- ^
"%PYTHON%" sandbox\free_fall.py