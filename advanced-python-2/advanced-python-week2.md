# 🚀 Advanced Python - Week 2 Plan  
> Topics: Error Handling & Logging · Typing & Dataclasses  
> Duration: 7 Days | Goal: Build solid foundations for scalable Python development

---

## 📅 Weekly Breakdown

| Day | Topic | Description | Practice |
|-----|-------|-------------|----------|
| **Day 1** | ⚠️ Error Types & Try-Except | Learn common Python errors, `try-except-finally` blocks | ✔️ Handle division, file reading, key errors |
| **Day 2** | 🔁 Custom Exceptions | Define and raise your own exceptions with context | ✔️ Create `InvalidAgeError`, use in validation logic |
| **Day 3** | 🪵 Logging Basics | Learn `logging` module, log levels, formatting logs | ✔️ Log info/errors to file instead of using `print()` |
| **Day 4** | ⚙️ Logging Configuration | Set up advanced configs, handlers, and log to multiple files | ✔️ Separate logs for errors and debug |
| **Day 5** | 📏 Type Hinting | Use static typing with `int`, `str`, `List`, `Dict`, `Optional`, `Union` | ✔️ Annotate functions with type hints |
| **Day 6** | 🧩 Dataclasses | Define classes with less boilerplate using `@dataclass` | ✔️ Create `User`, `Book` models with auto `__init__`, `__repr__` |
| **Day 7** | 💻 Mini Projects | Apply both concepts in small, clean code examples | ✔️ User form validator (with logging & custom error), Book manager (with dataclass & typing) |

---

## 🛠️ Mini Project Ideas

### 1. **User Input Validator**
- Input: `name`, `age`, `email`
- Features:
  - Custom exception if age < 18
  - Logging to `errors.log` if exception occurs
  - Valid entries are logged to `valid_users.log`

### 2. **Book Manager**
- `Book` class with `@dataclass`
- Load/save book data from JSON
- Use type hints everywhere
- CLI:
```bash
python book_manager.py add --title "1984" --author "Orwell" --year 1949
