.PHONY: help install run demo check

MODEL_DIR := models
MODEL_FILE := $(MODEL_DIR)/hand_landmarker.task
MODEL_URL := https://media.githubusercontent.com/media/tenstorrent/pytorch2.0_ttnn/7fb5bbaaff3b056c06a96ee3111b827729d7f6c6/tests/models/hand_landmark/hand_landmarker.task

help:
	@echo "Доступные цели:"
	@echo "  make install  - установить зависимости и модель"
	@echo "  make run      - запустить управление мышью"
	@echo "  make demo     - запустить демо модуля трекинга руки"
	@echo "  make check    - проверить синтаксис Python-файлов"

$(MODEL_FILE):
	@mkdir -p $(MODEL_DIR)
	@echo "Скачивание модели hand_landmarker.task..."
	python3 -c "import urllib.request; urllib.request.urlretrieve('$(MODEL_URL)', '$(MODEL_FILE)')"

install: $(MODEL_FILE)
	python3 -m pip install -r requirements.txt

run:
	python3 main.py

demo:
	python3 HandTrackingModule.py

check:
	python3 -m py_compile main.py HandTrackingModule.py
