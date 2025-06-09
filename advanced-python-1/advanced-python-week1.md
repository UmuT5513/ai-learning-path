# 🐍 Advanced Python - Week 1 Plan  
> Topics: OOP · Decorators · Iterators & Generators  
> Duration: 7 Days | Goal: Strengthen real-world Python fluency for AI/Data projects

---

## 📅 Weekly Breakdown

| Day | Topic | Description | Practice |
|-----|-------|-------------|----------|
| **Day 1** | 🧱 OOP Basics: Classes & Objects | Learn how to define a class, use `__init__`, create instances | ✔️ Create a `Book` class with attributes like `title`, `author`, `pages` |
| **Day 2** | 🧬 Inheritance & Polymorphism | Inherit base class, use `super()`, override methods | ✔️ `Vehicle`, `Car`, `Motorcycle` with custom `start_engine()` |
| **Day 3** | 🔐 Abstraction & Encapsulation | Use `@abstractmethod`, encapsulate with `_` and `__` | ✔️ `Shape` abstract class, implement `Circle`, `Rectangle` |
| **Day 4** | 🔁 Iterators | Implement `__iter__()`, `__next__()`, custom iterators | ✔️ Write `EvenNumbers(limit)` iterator |
| **Day 5** | ⚡ Generators | Use `yield`, compare with list-based memory | ✔️ Create a Fibonacci number generator |
| **Day 6** | 🎯 Decorators | Learn `@decorator`, wrap functions, use `*args` and `**kwargs` | ✔️ `@timer` and `@error_logger` decorators |
| **Day 7** | 💻 Mini Project: Grade System CLI | Combine all concepts into a practical CLI program | ✔️ CLI input with OOP, input validation decorator, grade generator |

---

## 🛠️ Mini Project - Grade System CLI

### Features:
- `Student` and `Course` classes  
- `@validate_grade` decorator to ensure valid input  
- `grades_generator()` to yield student grades  
- CLI Input:  
```bash
python grade_cli.py --student "Ali" --course "Math" --grade 78
