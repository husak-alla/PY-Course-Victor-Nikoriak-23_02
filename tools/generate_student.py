#!/usr/bin/env python3
"""
Instructor Mode — Student Notebook Generator
=============================================

Перетворює MASTER-ноутбук (з рішеннями) на STUDENT-версію (без рішень).

ТЕГИ КЛІТИНОК:
  solution    → код між # BEGIN SOLUTION / # END SOLUTION замінюється на # YOUR CODE HERE
  instructor  → клітинка повністю видаляється зі student-версії

МАРКЕРИ У КОДІ:
  # BEGIN SOLUTION
  ... повне рішення ...
  # END SOLUTION

USAGE:
  # Один ноутбук
  python tools/generate_student.py 04_boolean_logic_and_control/python_lesson_bool_logic.ipynb

  # Всі ноутбуки у проєкті
  python tools/generate_student.py --all

  # Вказати вихідний файл
  python tools/generate_student.py lesson.ipynb --output lesson_student.ipynb
"""

import json
import sys
import os
import glob
import re
import argparse
from pathlib import Path

# ── Налаштування ──────────────────────────────────────────────────────────────

SOLUTION_PLACEHOLDER = "# YOUR CODE HERE\n"
PASS_PLACEHOLDER = "pass\n"

SOLUTION_PATTERN = re.compile(
    r"[ \t]*# BEGIN SOLUTION.*?# END SOLUTION[ \t]*\n?",
    flags=re.DOTALL,
)

TAG_SOLUTION = "solution"
TAG_INSTRUCTOR = "instructor"


# ── Утиліти ───────────────────────────────────────────────────────────────────

def get_tags(cell: dict) -> list:
    return cell.get("metadata", {}).get("tags", [])


def source_to_str(source) -> str:
    if isinstance(source, list):
        return "".join(source)
    return source or ""


def str_to_source(text: str) -> list:
    lines = text.splitlines(keepends=True)
    return lines if lines else [""]


def strip_solution(source) -> list:
    """Замінює блоки BEGIN/END SOLUTION на placeholder."""
    text = source_to_str(source)
    result = SOLUTION_PATTERN.sub(SOLUTION_PLACEHOLDER, text)
    # Якщо весь код між маркерами — додаємо pass
    if result.strip() == SOLUTION_PLACEHOLDER.strip():
        result = SOLUTION_PLACEHOLDER + PASS_PLACEHOLDER
    return str_to_source(result)


def clear_outputs(cell: dict) -> dict:
    cell = dict(cell)
    cell["outputs"] = []
    cell["execution_count"] = None
    return cell


# ── Основна логіка ────────────────────────────────────────────────────────────

def process_notebook(nb: dict) -> dict:
    """Обробляє notebook: видаляє instructor-клітинки, замінює рішення."""
    student_cells = []
    stats = {"removed": 0, "blanked": 0, "kept": 0}

    for cell in nb.get("cells", []):
        tags = get_tags(cell)

        if TAG_INSTRUCTOR in tags:
            # Повністю видалити клітинку
            stats["removed"] += 1
            continue

        cell = dict(cell)

        if TAG_SOLUTION in tags and cell["cell_type"] == "code":
            # Замінити рішення на placeholder
            cell["source"] = strip_solution(cell.get("source", ""))
            cell = clear_outputs(cell)
            stats["blanked"] += 1
        else:
            # Залишити як є, але очистити виводи (опційно)
            stats["kept"] += 1

        student_cells.append(cell)

    nb = dict(nb)
    nb["cells"] = student_cells
    return nb, stats


def generate_student(
    master_path: str,
    output_path: str = None,
    verbose: bool = True,
) -> str:
    master_path = Path(master_path)

    if output_path is None:
        output_path = master_path.parent / (master_path.stem + "_student" + master_path.suffix)
    output_path = Path(output_path)

    with open(master_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    student_nb, stats = process_notebook(nb)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(student_nb, f, ensure_ascii=False, indent=1)

    if verbose:
        print(f"✅ {master_path.name}")
        print(f"   → {output_path}")
        print(f"   🗑  видалено (instructor):  {stats['removed']} клітинок")
        print(f"   ✏️  замінено (solution):    {stats['blanked']} клітинок")
        print(f"   📄 збережено:              {stats['kept']} клітинок")

    return str(output_path)


def find_master_notebooks(base_dir: str = ".") -> list:
    """Знаходить усі master-ноутбуки (виключає _student версії)."""
    all_nb = glob.glob(f"{base_dir}/**/*.ipynb", recursive=True)
    return [nb for nb in sorted(all_nb) if "_student" not in nb]


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Generate student version of Jupyter notebooks"
    )
    parser.add_argument(
        "notebook",
        nargs="?",
        help="Шлях до master-ноутбука (або --all для всіх)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Обробити всі ноутбуки у поточній директорії",
    )
    parser.add_argument(
        "--output",
        help="Вихідний файл (тільки для одного ноутбука)",
    )
    parser.add_argument(
        "--base",
        default=".",
        help="Базова директорія для --all (за замовчуванням: .)",
    )
    args = parser.parse_args()

    if args.all:
        notebooks = find_master_notebooks(args.base)
        if not notebooks:
            print("❌ Ноутбуків не знайдено")
            sys.exit(1)
        print(f"Знайдено {len(notebooks)} ноутбуків:\n")
        for nb in notebooks:
            generate_student(nb)
            print()
    elif args.notebook:
        generate_student(args.notebook, args.output)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
