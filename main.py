import cv2

# Загрузка изображения
image = cv2.imread('image.png')

# Преобразование изображения в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применение алгоритма поиска квадратов
# Например, используем метод Хафа для поиска прямоугольников
squares = cv2.HoughLinesP(gray, 1, 3.14/180, 50, minLineLength=50, maxLineGap=5)

# Рисование квадратов на изображении
if squares is not None:
    for square in squares:
        x1, y1, x2, y2 = square[0]
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Отображение результата
cv2.imshow('Squares', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
