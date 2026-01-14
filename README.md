# Online Store - Интернет-магазин на Django

Учебный проект интернет-магазина с полным функционалом каталога товаров, корзины покупок, системы пользователей и REST API.

## 🚀 Технологический стек

- **Backend Framework**: Django 5.2.8
- **API**: Django REST Framework
- **Аутентификация**: JWT (djangorestframework-simplejwt)
- **Документация API**: drf-yasg (Swagger/OpenAPI)
- **База данных**: PostgreSQL
- **Кэширование**: Redis
- **Асинхронные задачи**: Celery
- **OAuth**: Google OAuth2 (social-auth-app-django)
- **Язык**: Python 3

## 📦 Основные возможности

### Веб-интерфейс
- Каталог товаров с фильтрацией по категориям и поиском
- Детальная страница товара
- Корзина покупок с добавлением/удалением товаров
- Система регистрации и авторизации пользователей
- Личный кабинет пользователя
- OAuth авторизация через Google

### REST API
- Полный CRUD для товаров
- Управление корзиной через API
- Регистрация и авторизация через JWT токены
- Swagger документация API
- Аутентификация через JWT

### Дополнительные функции
- Кэширование с использованием Redis
- Асинхронные задачи через Celery
- Логирование запросов
- Middleware для измерения времени обработки запросов
- Пагинация товаров

## 📁 Структура проекта

```
online-store/
├── api/              # REST API приложение
├── cart/             # Приложение корзины покупок
├── pages/            # Статические страницы (главная, о нас)
├── shop/             # Приложение каталога товаров
├── users/            # Приложение пользователей
├── store/            # Основные настройки проекта
│   ├── settings.py   # Конфигурация Django
│   ├── celery.py     # Конфигурация Celery
│   └── middleware/   # Пользовательские middleware
├── static/           # Статические файлы (CSS, JS, изображения)
├── templates/        # HTML шаблоны
├── manage.py         # Django management скрипт
└── requirements.txt  # Зависимости проекта
```

## 🛠️ Установка и запуск

### Предварительные требования

- Python 3.8+
- PostgreSQL
- Redis
- Виртуальное окружение (рекомендуется)

### Шаги установки

1. **Клонируйте репозиторий** (если есть) или перейдите в директорию проекта:
   ```bash
   cd online-store
   ```

2. **Создайте виртуальное окружение**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # или
   venv\Scripts\activate  # Windows
   ```

3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Создайте файл `.env`** в корне проекта со следующими переменными:
   ```env
   SECRET_KEY=your-secret-key-here
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=localhost
   DB_PORT=5432
   GOOGLE_ID=your-google-oauth-client-id
   GOOGLE_SECRET_KEY=your-google-oauth-secret
   ```

5. **Примените миграции**:
   ```bash
   python manage.py migrate
   ```

6. **Создайте суперпользователя** (опционально):
   ```bash
   python manage.py createsuperuser
   ```

7. **Запустите сервер разработки**:
   ```bash
   python manage.py runserver
   ```

8. **Запустите Redis** (в отдельном терминале):
   ```bash
   redis-server
   ```

9. **Запустите Celery worker** (в отдельном терминале):
   ```bash
   celery -A store worker -l info
   ```

10. **Запустите Celery beat** (для периодических задач, в отдельном терминале):
    ```bash
    celery -A store beat -l info
    ```

## 📚 Использование

### Веб-интерфейс

После запуска сервера откройте в браузере:
- Главная страница: `http://127.0.0.1:8000/`
- Админ-панель: `http://127.0.0.1:8000/admin/`
- Каталог товаров: `http://127.0.0.1:8000/`
- Корзина: `http://127.0.0.1:8000/cart/cart/`
- Регистрация: `http://127.0.0.1:8000/user/register/`
- Вход: `http://127.0.0.1:8000/user/login/`

### REST API

#### Документация API

В режиме разработки доступна интерактивная документация:
- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

#### Основные эндпоинты

**Аутентификация:**
- `POST /api/register/` - Регистрация нового пользователя
- `POST /api/token/` - Получение JWT токена
- `POST /api/token/refresh/` - Обновление токена
- `POST /api/logout/` - Выход (blacklist токена)

**Товары:**
- `GET /api/products/` - Список всех товаров
- `GET /api/products/<id>/` - Детали товара
- `POST /api/products/` - Создание товара (требует аутентификации)
- `PUT /api/products/<id>/` - Обновление товара
- `DELETE /api/products/<id>/` - Удаление товара

**Корзина:**
- `GET /api/cart/` - Получить корзину пользователя
- `POST /api/cart/` - Добавить товар в корзину
- `PATCH /api/cart/<product_id>/` - Обновить количество товара
- `DELETE /api/cart/<product_id>/` - Удалить товар из корзины

#### Пример использования API

```bash
# Регистрация
curl -X POST http://127.0.0.1:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "user", "email": "user@example.com", "password": "password123"}'

# Получение токена
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "user", "password": "password123"}'

# Получение списка товаров (с токеном)
curl -X GET http://127.0.0.1:8000/api/products/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 🔧 Управление данными

### Создание миграций

```bash
python manage.py makemigrations
python manage.py migrate
```

### Заполнение базы данных

В проекте есть management команда для заполнения товаров:
```bash
python manage.py fill_item
```

## 🧪 Тестирование

Запуск тестов:
```bash
python manage.py test
```

## 📝 Модели данных

### Product (Товар)
- `name` - Название товара
- `description` - Описание
- `price` - Цена
- `count` - Количество на складе
- `product_types` - Категория товара
- `image` - Изображение товара

### Cart (Корзина)
- `user` - Пользователь (OneToOne)

### CartItem (Элемент корзины)
- `cart` - Корзина
- `product` - Товар
- `quantity` - Количество

## 🔐 Безопасность

- JWT токены для API аутентификации
- CSRF защита для веб-форм
- Валидация паролей
- OAuth2 для социальной авторизации
- Blacklist для отозванных токенов

## 📄 Лицензия

Это учебный проект.

## 👤 Автор

Проект создан в учебных целях.

## 🤝 Вклад

Проект находится в стадии разработки. Предложения и замечания приветствуются!

---

**Примечание**: Убедитесь, что все сервисы (PostgreSQL, Redis) запущены перед запуском приложения.
