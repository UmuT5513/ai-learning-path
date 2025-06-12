from abc import ABC, abstractmethod

class FileHandler(ABC):
    def __init__(self, path):
        self.file_path = path

    @abstractmethod
    def read_file(self):
        pass


class TxtFileHandler(FileHandler):
    def read_file(self):
        with open(self.file_path, "r", encoding="utf-8") as f_obj:
            content = f_obj.read()
        return content
            

class CsvFileHandler(FileHandler):
    def read_file(self):
        import csv
        with open(self.file_path, "r", encoding="utf-8") as f_obj:
            reader = csv.reader(f_obj)
            content = [row for row in reader]
        return content


class JsonFileHandler(FileHandler):
    def read_file(self):
        with open(self.file_path, "r", encoding="utf-8") as f_obj:
            import json
            content = json.load(f_obj)
        return f_obj




def print_file_content(FileHandler):
    content = FileHandler.read_file()
    print(content)


print_file_content(TxtFileHandler("sample.txt"))
print_file_content(CsvFileHandler("sample.csv"))
print_file_content(JsonFileHandler("sample.json"))

