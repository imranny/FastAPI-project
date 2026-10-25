# Учебный проект FastAPI
Он нужен для того чтобы ты научился:
1. FastAPI
2. Docker
3. Git
4. Правильной структуре проекта

## Создайте свой собственный проект с нуля (обязательно создайте свой со своим функционалом)
 > Мой проект это лишь тестовый проект, чтобы вы познакомились с тем как работает FastAPI. Чтобы точнее разобраться - необходимо с нуля написать свой.
 > Для того, чтобы сделать свой проект, нужно ознакомиться со всеми материалами из роадмапа по infra, а также выполнить ряд домашек из гайдов.
 > Домашки это подводящий этап к своему проекту.

## Чтобы протестировать как работает FastAPI и вообще разобраться с ним, можно сделать Fork или Clone моего учебного проекта.
 > **Fork** — это копия репозитория в вашем аккаунте GitHub. Это нужно, чтобы у вас была своя версия проекта, которую вы сможете менять.
 
## Как сделать Fork
1. Откройте репозиторий проекта на GitHub
2. Нажмите кнопку **"Fork"** в правом верхнем углу страницы
3. Выберите свой аккаунт — GitHub создаст копию репозитория у вас

## Как склонировать репозиторий 
 > **Клонирование** — это скачивание репозитория на ваш компьютер.

```bash
# Замените YOUR_USERNAME на ваш GitHub-ник
git clone https://github.com/YOUR_USERNAME/fastapi-main.git
cd fastapi-main
```

---

## Запустите проект локально

### Установите Python

Убедитесь, что установлен **Python 3.10 или новее**:

```bash
python --version
```

### Создайте виртуальное окружение

Виртуальное окружение изолирует зависимости проекта от системы.

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Установите зависимости

```bash
pip install -r requirements.txt
```

### Запустите сервер

```bash
uvicorn app.main:app --reload
```

После запуска откройте в браузере:
- **http://127.0.0.1:8000/docs** — интерактивная Swagger-документация
- **http://127.0.0.1:8000/users** — список пользователей

---

## Запустите проект в Docker

### Установите Docker

- **Windows / macOS**: установите [Docker Desktop](https://www.docker.com/products/docker-desktop/)
  - Если Docker работает через **WSL** (Windows Subsystem for Linux), используйте команды с `wsl docker ...`
- **Linux**: установите [docker Engine](https://docs.docker.com/engine/install/)

Проверьте установку:

```bash
docker --version
```

### Соберите образ и запустите контейнер

**Собрать образ:**
```bash
docker build -t fastapi-app .
```

**Запустить контейнер:**
```bash
docker run -d --name fastapi-app -p 8000:8000 fastapi-app
```

**Если Docker в WSL:**
```bash
wsl docker build -t fastapi-app .
wsl docker run -d --name fastapi-app -p 8000:8000 fastapi-app
```

После запуска откройте **http://127.0.0.1:8000/docs**.

## Как пользоваться API

### Через Swagger (визуально)

1. Откройте **http://127.0.0.1:8000/docs**
2. Нажмите на нужный эндпоинт -> кнопка **"Try it out"**
3. Для `POST /users` введите JSON и нажмите **"Execute"**

### Через curl (терминал)

**Создать пользователя:**
```bash
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Иван","age":30,"sex":"M","job":"Developer"}'
```

**Получить всех пользователей:**
```bash
curl http://127.0.0.1:8000/users
```

## Структура проекта

```
fastapi-main/
├── app/                         # Основной код приложения
│   ├── __init__.py
│   ├── main.py                  # Точка входа FastAPI
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py            # Маршруты API (эндпоинты)
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py            # Настройки приложения
│   ├── database/
│   │   ├── __init__.py
│   │   └── db.py                # Подключение к базе данных
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py              # SQLAlchemy модель (таблица БД)
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── user_repo.py         # Репозиторий (работа с БД)
│   └── schemas/
│       ├── __init__.py
│       └── user.py              # Pydantic схемы (валидация)
├── Makefile                     # Команды для Docker
├── Dockerfile                   # Конфигурация Docker-образа
├── requirements.txt             # Зависимости Python
├── .dockerignore                # Файлы, исключённые из Docker
└── .gitignore                   # Файлы, исключённые из Git
```
