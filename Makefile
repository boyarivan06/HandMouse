.PHONY: help install run demo check

help:
	@echo "Доступные цели:"
	@echo "  make install  - установить зависимости"
	@echo "  make run      - запустить управление мышью"
	@echo "  make demo     - запустить демо модуля трекинга руки"
	@echo "  make check    - проверить синтаксис Python-файлов"

install:
	python3 -m pip install -r requirements.txt

run:
	python3 main.py

demo:
	python3 HandTrackingModule.py

check:
	python3 -m py_compile main.py HandTrackingModule.py
