from dataclasses import dataclass, field
import logging
from datetime import datetime
from typing import List

_NEXT_ID = 0



logger = logging.getLogger(__name__)
logger.propagate = False # Aynı mesajın 2 kez root'a yazılmasını engeller
logger.setLevel('DEBUG')
formatter = logging.Formatter("{asctime} - {levelname} - {message}",
                              style="{",
                              datefmt="%Y-%m-%d %H:%M",
                              )
file_handler = logging.FileHandler(filename='file.log', mode='a', encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)




@dataclass
class TodoItem:
    text : str
    _done : bool = False  # task'ın tamamlanma durumu.
    id : int = field(repr=False, init=False)

    def mark_done(self) -> None:
        self._done = True

    def __post_init__(self):
        global _NEXT_ID
        self.id = _NEXT_ID
        _NEXT_ID += 1

        try:
            if not self.text.strip():
                raise ValueError("Görev açıklaması boş olamaz!")
        except ValueError:
            logger.error(ValueError, exc_info=True)
        else:
            logger.info("ID atama işlemi başarılı!")


class TodoManager:
    def __init__(self):
        self._tasks: List[TodoItem] = []
    
    
    def add(self, task_text: str) -> TodoItem:
        task = TodoItem(task_text, False)
        self._tasks.append(task)
        with open("tasks.txt", "a+", encoding='utf-8') as file:
            file.write(task.text)
            file.write("\n")
        logger.info("Görev başarıyla eklendi!")
        return task
    
    def get_todo_item(self, task_id):
        task = next((t for t in self._tasks if t.id == task_id),None)
        try:
            if task is None:
                raise TypeError("ID bulunamadı")
        except TypeError:
            logger.error(TypeError, exc_info=True)
        else:
            return task

    def remove(self, task_id: int):
        task = self.get_todo_item(task_id)
        if task == None:
            logger.warning("kaldırılacak task tipi None! get_todo_item taskı bulamadı None döndürdü!")
        self._tasks = [t for t in self._tasks if task_id != t.id]
        logger.info("Görev kaldırma başarılı!")


    def list(self):
        print(f"{len(self._tasks)} görev listelendi!")
        logger.info(f"{len(self._tasks)} görev listelendi!")
        for task in self._tasks:
            print(f"Görev ID:{task.id}\nGörev Açıklaması:{task.text}\nTamamlanma Durumu: {'✓' if task._done == True else '✗'}")

        
    def mark_done(self, task_id:int):
        try:
            task = self.get_todo_item(task_id)
            task.mark_done()
            logger.info(f"Görev tamamlandı olarak işaretlendi! ID: {task_id}")
        except ValueError as v:
            logger.error(f"Görev işaretleme hatası: {v}")
            raise



