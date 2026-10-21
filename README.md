# HandMouse

Управление курсором мыши жестами руки через веб-камеру (OpenCV + MediaPipe).
![how it works](https://user-images.githubusercontent.com/96628641/216154664-38c2e8a6-c96e-4dcc-8d66-76f3226630bd.jpg)

## Требования

- Python 3.12
- Веб-камера
- Графическая сессия (для управления курсором)

## Установка

```bash
python3.12 -m venv .venv
source .venv/bin/activate
make install
```

`make install` автоматически скачивает модель `models/hand_landmarker.task`.

## Запуск

```bash
make run
```

## Проверка

```bash
make check
```

## Жесты

- Большой + указательный близко: зажать левую кнопку мыши.
- Большой + средний близко: правый клик.
- Большой + мизинец близко: остановка программы.
