# 🐍 PY_Course_Victor-Nikoriak-23_02

## Python Course — 23.02.2026

Ласкаво просимо 👋  

Цей репозиторій містить:

✅ матеріали занять  
✅ практичні завдання  
✅ домашні роботи  
✅ workflow роботи через GitHub (як у реальній IT-команді)

---

# ⚙️ 0. Встановлення Git (ОБОВʼЯЗКОВО)

Git — це система контролю версій, через яку ми:

- отримуємо матеріали курсу
- здаємо домашні завдання
- отримуємо фідбек

---

## 🪟 Windows

🔗 Офіційна сторінка:
https://git-scm.com/install/windows

🔗 Пряме завантаження:
https://github.com/git-for-windows/git/releases/latest

Завантажте:

```

Git for Windows/x64 Setup

````

### Під час встановлення
✅ Просто натискайте **Next** (налаштування за замовчуванням).

---

## 🍎 macOS

🔗 Інструкція:
https://git-scm.com/install/mac

Відкрийте Terminal:

```bash
xcode-select --install
````

---

## 🐧 Linux

🔗 Інструкція:
[https://git-scm.com/install/linux](https://git-scm.com/install/linux)

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install git
```

### Fedora

```bash
sudo dnf install git
```

### Arch

```bash
sudo pacman -S git
```

---

## ✅ Перевірка встановлення

```bash
git --version
```

Очікуваний результат:

```
git version 2.xx.x
```

---

## ✅ Перше налаштування Git (1 раз)

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

⚠️ Email має співпадати з GitHub.

---

# 🧭 Як працює курс

* `main` → матеріали курсу (оновлює викладач)
* домашні роботи → окремі гілки
* здача → Pull Request (PR)
* студентський код **не додається** у main

👉 Pull Request = здача домашнього завдання.

---

# 🚀 Швидкий старт

---

## 1️⃣ Fork репозиторію

На GitHub натисніть:

```
Fork
```

У вас з’явиться копія:

```
github.com/<your-username>/PY_Course_Victor-Nikoriak-23_02
```

---

## 2️⃣ Clone у PyCharm

PyCharm →

```
File → New Project from Version Control
```

Вставте URL **вашого fork**.

---

## 3️⃣ Додати upstream (ОДИН РАЗ)

В Terminal:

```bash
git remote add upstream https://github.com/<TEACHER_USERNAME>/PY_Course_Victor-Nikoriak-23_02
```

Перевірка:

```bash
git remote -v
```

Повинно бути:

```
origin   → ваш repo
upstream → repo викладача
```

---

# 🔄 Перед кожним заняттям

Оновлення матеріалів:

```bash
git checkout main
git pull upstream main
git push origin main
```

---

# 📚 Домашнє завдання

## ❗ НЕ працюємо у main

---

## Кроки

### 1. Створити гілку

```bash
git checkout -b homework-01
```

---

### 2. Виконати завдання

Редагуйте файли або notebook.

---

### 3. Commit

```bash
git add .
git commit -m "Homework 01"
```

---

### 4. Push

```bash
git push origin homework-01
```

---

### 5. Здати через Pull Request

На GitHub:

```
Compare & Pull Request
```

PR:

```
homework-01 → main
```

---

# ✅ Отримання фідбеку

Після коментарів викладача:

```bash
git add .
git commit -m "Fix after review"
git push origin homework-01
```

PR оновиться автоматично.

---

# 📏 Правила курсу

✅ 1 домашка = 1 гілка
✅ нормальні commit messages
✅ оновлювати main перед заняттям

❌ не працювати в main
❌ не merge PR
❌ не видаляти матеріали курсу

---

# 🧯 Часті проблеми

## Не бачу нові уроки

```bash
git checkout main
git pull upstream main
```

---

## Зробив домашку в main

```bash
git checkout -b homework-XX
git checkout main
git pull upstream main
```

---

## Permission denied

Ви клонували repo викладача замість fork.

Переклонуйте свій fork.

---

# 🧰 Git шпаргалка

```bash
git status
git branch
git checkout branch_name
git log --oneline
```

---

# 🆘 Питання

Надсилайте:

* скрін помилки
* `git status`
* `git remote -v`

І проблема вирішиться швидко 🙂

```
