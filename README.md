# HandMouse

Проект для управления курсором мыши с помощью жестов руки через веб-камеру (OpenCV + MediaPipe).

## Быстрый старт

```bash
make install
make run
```

## Что делает проект

- отслеживает ключевые точки руки;
- двигает курсор по координатам пальца;
- выполняет клик/правый клик по жестам;
- останавливает работу по отдельному жесту.

## Замеченные ошибки с устаревшими/неактуальными объектами библиотек

1. `QtWidgets.QApplication.desktop()` в `main.py` — устаревший API Qt (deprecated), в новых версиях Qt рекомендуется получать экран через `QGuiApplication.primaryScreen()`.
2. `mp.solutions.hands.Hands(...)` в `HandTrackingModule.py` вызывается позиционными аргументами в старом стиле; для актуальных версий MediaPipe безопаснее использовать именованные параметры (`static_image_mode`, `max_num_hands`, `model_complexity`, `min_detection_confidence`, `min_tracking_confidence`).
3. В `requirements.txt` одновременно указаны `opencv-python` и `opencv-contrib-python` одной версии — это конфликтующий/избыточный набор пакетов для одного пространства `cv2`.
