# Instructor Mode — Посібник викладача

## Загальна ідея

Ви пишете **один MASTER-ноутбук** з повними рішеннями та нотатками для себе.
Скрипт автоматично генерує **STUDENT-версію** — без рішень, без нотаток.

```
python_lesson_bool_logic.ipynb          ← MASTER (редагуєте ви)
python_lesson_bool_logic_student.ipynb  ← STUDENT (генерується автоматично)
```

---

## Система тегів

### Тег `solution` — замінити рішення на заготовку

Додайте тег `solution` до клітинки, яка містить завдання для студентів.
Усередині коду позначте рішення маркерами:

```python
# Якийсь стартовий код (студент його бачить)
user_input = "456"

# BEGIN SOLUTION
if user_input.isdigit():
    print("Число:", int(user_input))
else:
    print("Помилка")
# END SOLUTION
```

**Що побачить студент:**

```python
user_input = "456"

# YOUR CODE HERE
```

---

### Тег `instructor` — видалити клітинку повністю

Клітинки з тегом `instructor` **не потрапляють** у student-версію.

Використовуйте для:
- Нотаток для себе (`# 📋 INSTRUCTOR NOTES`)
- Answer key (`# 🔑 ANSWER KEY`)
- Складних прикладів, які студент не повинен бачити до заняття

---

## Як додати тег у Jupyter

### JupyterLab

```
View → Cell Toolbar → Tags
```

Введіть `solution` або `instructor` у поле і натисніть Enter.

### PyCharm

Відкрийте Cell Metadata панель або відредагуйте `.ipynb` напряму:

```json
"metadata": {
  "tags": ["solution"]
}
```

---

## Генерація student-версії

### Один ноутбук

```bash
python tools/generate_student.py 04_boolean_logic_and_control/python_lesson_bool_logic.ipynb
```

Результат: `python_lesson_bool_logic_student.ipynb` поруч із оригіналом.

### Всі ноутбуки

```bash
cd C:\Users\victo\PycharmProjects\PY-Course-Victor-Nikoriak-23_02
python tools/generate_student.py --all
```

### Вказати вихідний файл

```bash
python tools/generate_student.py lesson.ipynb --output lesson_for_students.ipynb
```

---

## Workflow занять

### Підготовка до уроку

```
1. Відкриваєте MASTER-ноутбук
2. Додаєте/оновлюєте матеріал та рішення
3. Запускаєте: python tools/generate_student.py <notebook.ipynb>
4. Пушите student-версію на GitHub (main)
```

### Під час уроку

```
Ви:        відкриваєте MASTER  → бачите всі рішення + нотатки
Студенти:  відкривають STUDENT → бачать # YOUR CODE HERE
```

### Здача домашньої роботи

```
Студент:
  1. git checkout -b homework-02
  2. Виконує завдання у student-ноутбуку
  3. git commit + git push
  4. Pull Request → homework-02 → main
```

---

## Структура MASTER-ноутбука

```
[🔒 Системна клітинка]       ← hide_input: true (студент бачить тільки "System ready")
[👤 Представтесь]            ← видима студенту
[Конспект]                   ← видимий студенту
[✅ Task N — опис]           ← видимий студенту
  [🔮 Прогноз]               ← студент вводить відповідь
  [🐍 Reveal]                ← hide_input: true (пояснення після run)
  [TODO клітинка]  ← тег: solution  ← студент пише код тут
  [📋 INSTRUCTOR NOTES]  ← тег: instructor  ← тільки для викладача
[🔑 ANSWER KEY]              ← тег: instructor  ← тільки для викладача
[Висновок]                   ← видимий студенту
```

---

## Що де зберігати в Git

```
main branch:
  ├ *_student.ipynb   ← студенти бачать (без рішень)
  ├ docs/
  └ requirements.txt

(особисто / не пушити публічно):
  └ *_master.ipynb    ← з повними рішеннями
```

**Або** якщо репо приватне — можна пушити обидва.

---

## Швидка шпаргалка

| Дія | Команда |
|-----|---------|
| Згенерувати student-версію | `python tools/generate_student.py <nb.ipynb>` |
| Всі ноутбуки одразу | `python tools/generate_student.py --all` |
| Перевірити що витікло | відкрити `*_student.ipynb` і пошукати `INSTRUCTOR` |
