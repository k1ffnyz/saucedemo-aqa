# AQA Python — SauceDemo Login Tests

Автоматизированные UI-тесты авторизации для сайта  
👉 https://www.saucedemo.com/

Проект выполнен в рамках тестового задания на позицию **Junior AQA Python**.

---

## 🧪 Проверяемые сценарии

Реализовано **5 автотестов**, покрывающих основные сценарии логина:

1. **Успешная авторизация**
   - Пользователь: `standard_user`
   - Пароль: `secret_sauce`
   - Проверка корректного перехода на страницу товаров (`inventory.html`)

2. **Логин с неверным паролем**
   - Проверка отображения сообщения об ошибке

3. **Логин заблокированного пользователя**
   - Пользователь: `locked_out_user`
   - Проверка сообщения о блокировке аккаунта

4. **Логин с пустыми полями**
   - Проверка валидации и сообщения об ошибке

5. **Логин пользователем performance_glitch_user**
   - Проверка успешного перехода на страницу товаров
   - Учет возможных задержек загрузки страницы

---

# успешный логин
login.login("standard_user", "secret_sauce")

# заблокированный пользователь
login.login("locked_out_user", "secret_sauce")

# performance пользователь
login.login("performance_glitch_user", "secret_sauce")

---

## 🛠 Используемый стек

- **Python 3.10**
- **Selenium 4** (Selenium Manager)
- **Pytest**
- **Page Object Model**
- **Allure** (отчёты)
- **Docker**

---

## 📁 Структура проекта

```text
saucedemo-aqa/
├── pages/          # Page Object'ы
├── tests/          # Тесты и фикстуры
├── utils/          # Конфигурация
├── pytest.ini      # Настройки pytest
├── requirements.txt
├── Dockerfile
└── README.md
```

---

##🐳 Запуск в Docker
```bash
docker build -t saucedemo-tests .
docker run saucedemo-tests
```

---

## 📌 Примечания
- Используется Selenium Manager, поэтому не требуется ручная установка WebDriver
- Проект поддерживает запуск в headless-режиме
- Структура соответствует реальным AQA-проектам
