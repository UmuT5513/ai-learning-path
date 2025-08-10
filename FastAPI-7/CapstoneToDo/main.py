from fastapi import FastAPI, HTTPException
from schemas import Task, TaskCreate, TaskUpdate
from datetime import datetime

app = FastAPI()

tasks = [] # Task sınıfından objelerin dict türünden listesi
id_counter = 0

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate)->Task:
    """
    sistem tarafından atanan bir id ile task oluşturup db ye kaydeder.

    Args:
        task (TaskBaser): oluşturulan task.

    Returns:
        Task: ID atanmış haliyle oluşturulan task
    """
    
    global id_counter
    task_dict = task.model_dump()
    task_dict["id"] = id_counter #yeni id key ekledim. value sını id_counter.
    id_counter += 1
    tasks.append(task_dict) 
    return task_dict # Task sınıfını return eder.

@app.get("/tasks", response_model=list[Task])
def list_tasks()->list[Task]:
    return tasks
        

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id:int)->Task:
    """
    verilen task_id ye göre taski return eder.

    Args:
        task_id: int türünde task_id

    Returns:
        TaskBaser: task_id ye göre bulunan task

    Raises:
        HTTPException: 404 status code and "Task not found" detail if task not found
    """
    for t in tasks:
        if t["id"] == task_id:
            return t # parametre olarak verlien task_id eğer tasks ların içindeki bir taska mukabil geliyorsa o taski return eder.
            # verimlilik açısından pek elverişli değil çünkü eğer aranan task id si listenin en sonundaysa oraya kadar dönmek zorunda kalacak.
    raise HTTPException(status_code=404, detail="Task bulunamadı, girdiğiniz task_id yi kontrol edin!")
        

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id:int, updated_task:TaskUpdate)->Task:
    """
    verilen task_id ye göre taski update eder.
    
    sadece gönderilen alanları günceller.

    Args:
        task_id: int türünde task_id
        updated_task: yeni task değerleri

    Returns:
        güncellenmiş taskı döndürür.

    Raises:
        HTTPException: task_id, herhangi bir task ile eşleşmiyorsa "task not found" hatası
    """
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            current_task = t.copy()
            updated_dict = updated_task.model_dump(exclude_unset=True) # atanmamış parametreleri dahil etmez.

            #güncelleme verileri mevcut taska uygula
            for field, value in updated_dict.items():
                current_task[field] = value

            #zorunlu alanlar, missing errordan kaçınmak için    
                #güncellendiğine dair timestamp ekle
            current_task["updated_at"] = datetime.now()
            current_task["id"] = task_id

            #task listesine ekle ve döndür
            tasks[i] = current_task
            return current_task
    raise HTTPException(status_code=404, detail="Task bulunamadı, girdiğiniz task_id yi kontrol edin!")

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    """
    verilen task_id ye göre taski siler.

    Args:
        task_id: int türünde task_id

    Raises:
        HTTPException: task_id, herhangi bir task ile eşleşmiyorsa "task not found" hatası
    """
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            deleted_task = tasks.pop(i)
            return {"message": f"Task silindi: {deleted_task['title']}"}
                    
    raise HTTPException(status_code=404, detail="Task bulunamadı, girdiğiniz task_id yi kontrol edin!")


        
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)