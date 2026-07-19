# =================================================== -РАБОТА-С-ИЗОБРАЖЕНИЯМИ- ==========================================================

from PIL import Image, ImageFilter, ImageDraw, ImageFont

def work_with_images():
    """Демонстрация работы с изображениями"""
    
    print("\n" + "="*60)
    print("🖼️ РАБОТА С ИЗОБРАЖЕНИЯМИ")
    print("="*60)
    
    # 1. СОЗДАНИЕ НОВОГО ИЗОБРАЖЕНИЯ
    print("\n1. Создание нового изображения:")
    
    # Создаем красный квадрат 200x200
    img = Image.new('RGB', (200, 200), color='red')
    img.save('red_square.png')
    print("✅ Создан красный квадрат: red_square.png")
    
    # 2. ОТКРЫТИЕ И ИЗМЕНЕНИЕ РАЗМЕРА
    print("\n2. Изменение размера изображения:")
    
    # Создаем изображение с градиентом
    img_gradient = Image.new('RGB', (400, 200))
    pixels = img_gradient.load()
    for x in range(400):
        for y in range(200):
            pixels[x, y] = (x // 2, y, 100)  # Красивый градиент
    img_gradient.save('gradient.png')
    print("✅ Создан градиент: gradient.png")
    
    # Изменяем размер
    img_resized = img_gradient.resize((200, 100))
    img_resized.save('gradient_small.png')
    print("✅ Изменен размер: gradient_small.png")
    
    # 3. ПРИМЕНЕНИЕ ФИЛЬТРОВ
    print("\n3. Применение фильтров:")
    
    # Загружаем изображение и применяем фильтр размытия
    if img_gradient:
        img_blur = img_gradient.filter(ImageFilter.BLUR)
        img_blur.save('gradient_blur.png')
        print("✅ Применен фильтр размытия: gradient_blur.png")
    
    # 4. РИСОВАНИЕ НА ИЗОБРАЖЕНИИ
    print("\n4. Рисование на изображении:")
    
    img_draw = Image.new('RGB', (300, 200), color='white')
    draw = ImageDraw.Draw(img_draw)
    
    # Рисуем прямоугольник
    draw.rectangle([50, 50, 250, 150], outline='blue', width=3)
    # Рисуем текст
    draw.text((100, 80), "Python", fill='red')
    img_draw.save('drawing.png')
    print("✅ Создан рисунок с текстом: drawing.png")
    
    # 5. ОБЪЕДИНЕНИЕ ИЗОБРАЖЕНИЙ
    print("\n5. Объединение изображений:")
    
    # Создаем два изображения
    img1 = Image.new('RGB', (100, 100), color='red')
    img2 = Image.new('RGB', (100, 100), color='blue')
    
    # Создаем новое изображение и вставляем два других
    combined = Image.new('RGB', (220, 120), color='black')
    combined.paste(img1, (10, 10))
    combined.paste(img2, (120, 10))
    combined.save('combined.png')
    print("✅ Изображения объединены: combined.png")
    
    print("\n📁 Все изображения сохранены в папке проекта!")

# =================================================== -РАБОТА-СО-ЗВУКОМ- ==========================================================

import pygame
import time
import os

def work_with_sound():
    """Демонстрация работы со звуком"""
    
    print("\n" + "="*60)
    print("🔊 РАБОТА СО ЗВУКОМ")
    print("="*60)
    
    # Инициализируем pygame
    pygame.init()
    pygame.mixer.init()
    
    # 1. СОЗДАНИЕ ПРОСТОГО ЗВУКА (синтез)
    print("\n1. Создание простого звука:")
    
    # Создаем папку для звуков если её нет
    os.makedirs("sounds", exist_ok=True)
    
    # Создаем звуковой файл с помощью простого метода
    # Для создания реального звука нужна библиотека numpy
    # Но мы создадим пустой WAV файл как пример
    with open("sounds/beep.wav", "wb") as f:
        # Записываем заголовок WAV файла (очень простой пример)
        f.write(b'RIFF')
        f.write((36).to_bytes(4, 'little'))  # Размер
        f.write(b'WAVE')
        f.write(b'fmt ')
        f.write((16).to_bytes(4, 'little'))  # Размер fmt
        f.write((1).to_bytes(2, 'little'))   # Audio format (PCM)
        f.write((1).to_bytes(2, 'little'))   # Mono
        f.write((44100).to_bytes(4, 'little'))  # Sample rate
        f.write((44100 * 2).to_bytes(4, 'little'))  # Byte rate
        f.write((2).to_bytes(2, 'little'))   # Block align
        f.write((16).to_bytes(2, 'little'))  # Bits per sample
        f.write(b'data')
        f.write((0).to_bytes(4, 'little'))   # Размер данных (пусто)
    
    print("✅ Создан звуковой файл: sounds/beep.wav")
    
    # 2. ВОСПРОИЗВЕДЕНИЕ ЗВУКА (если файл существует)
    print("\n2. Воспроизведение звука:")
    
    # Создаем простой звук для теста (длительный сигнал)
    try:
        # Создаем простой звук с помощью писка
        import winsound  # Только для Windows
        print("🔔 Воспроизвожу звук... (будет сигнал)")
        winsound.Beep(440, 500)  # 440 Гц, 500 мс
        print("✅ Звук воспроизведен!")
    except:
        print("⚠️ Функция Beep доступна только на Windows")
        print("💡 На Linux/Mac используйте другие методы")
    
    # 3. РАБОТА С MP3/OGG (пример)
    print("\n3. Создание звука с помощью встроенных средств:")
    
    # Создаем простой звуковой сигнал с помощью print (шутка)
    print("🔊 *Звуковой сигнал* (представьте, что это звук)")
    time.sleep(0.5)
    
    # 4. ВОСПРОИЗВЕДЕНИЕ ЧЕРЕЗ PYGAME
    print("\n4. Воспроизведение через Pygame:")
    
    # Создаем простой звук через pygame
    try:
        # Создаем пустой звук (для демонстрации)
        sound = pygame.mixer.Sound(buffer=bytes([0]) * 1000)
        # sound.play()  # Раскомментируйте для воспроизведения
        print("✅ Pygame готов к воспроизведению звуков")
    except Exception as e:
        print(f"⚠️ Не удалось создать звук в pygame: {e}")
    
    pygame.quit()
    
    print("\n📁 Папка 'sounds' создана для ваших звуковых файлов!")

# =================================================== -ЗАГРУЗКА-ИЗОБРАЖЕНИЙ-ИЗ-ПАПКИ- ==========================================================

def load_images_from_folder():
    """Загрузка всех изображений из папки"""
    
    print("\n" + "="*60)
    print("📂 ЗАГРУЗКА ИЗОБРАЖЕНИЙ ИЗ ПАПКИ")
    print("="*60)
    
    # Создаем папку images если её нет
    os.makedirs("images", exist_ok=True)
    
    # Создаем несколько тестовых изображений
    for i in range(3):
        img = Image.new('RGB', (100, 100), color=(i*50, i*30, i*80))
        img.save(f'images/test_image_{i}.png')
        print(f"✅ Создано тестовое изображение: test_image_{i}.png")
    
    # Загружаем все изображения
    print("\n📖 Загрузка изображений из папки 'images':")
    image_files = []
    for file in os.listdir("images"):
        if file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                img = Image.open(os.path.join("images", file))
                image_files.append(file)
                print(f"  ✅ Загружено: {file} ({img.size[0]}x{img.size[1]})")
            except Exception as e:
                print(f"  ❌ Ошибка загрузки {file}: {e}")
    
    print(f"\n📊 Всего загружено изображений: {len(image_files)}")

# =================================================== -ОБНОВЛЕННАЯ-ОСНОВНАЯ-ФУНКЦИЯ- ==========================================================

def main():
    """Главная функция для демонстрации всех возможностей"""
    
    print("""
    ╔═══════════════════════════════════════════════════════════════════╗
    ║        РАБОТА С ФАЙЛАМИ В PYTHON - ПОЛНОЕ РУКОВОДСТВО           ║
    ╚═══════════════════════════════════════════════════════════════════╝
    """)
    
    # Базовые операции с файлами
    demonstrate_basic_file_operations()
    
    # Работа с JSON (данные игроков)
    print("\n" + "="*60)
    print("2. РАБОТА С JSON (ДАННЫЕ ИГРОКОВ)")
    print("="*60)
    
    manager = PlayerDataManager("data/player_data.json")
    manager.update_player_coins("player_1", 150)
    manager.update_player_coins("player_1", 80)
    manager.update_player_coins("player_2", 500)
    
    # Показываем сохраненные данные
    print("\n📊 Текущие данные игроков:")
    all_players = manager.get_all_players()
    for player_id, data in all_players.items():
        print(f"  {player_id}: {data}")
    
    demonstrate_csv_operations()
    demonstrate_path_operations()
    demonstrate_error_handling()
    
    # НОВЫЕ ФУНКЦИИ!
    work_with_images()
    work_with_sound()
    load_images_from_folder()
    
    print("\n" + "="*60)
    print("✅ ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА!")
    print("="*60)
