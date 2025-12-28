from datetime import datetime
from storage.json_store import load_tasks, save_tasks


def add_task(title, due=None):
    tasks = load_tasks()
    next_id = max([t["id"] for t in tasks], default=0) + 1
    
    task = {
        "id": next_id,
        "title": title,
        "status": "pending",
        "due": due,
        "created_at": datetime.utcnow().isoformat()
    }

    tasks.append(task) # bele append tanba nene list of dictionary ida 
    save_tasks(tasks) # deposi de append ba tasks ita save fial fali ba iha tasks

    return tasks
def list_tasks(status=None):
    tasks = load_tasks()

    if status:
        tasks = [t for t in tasks if t["status"] == status]
    
    return tasks

def mark_done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t['id'] == task_id:
            t['status'] = 'done'
            save_tasks(tasks)
            return t
    raise ValueError("Task not Found")

def delete_task(task_id):

    tasks = load_tasks()
    new_deleted_task = [t for t in tasks if t["id"] != task_id]

    if len(tasks) == len(new_deleted_task):
        raise ValueError("Task not found")
    save_tasks(new_deleted_task)


