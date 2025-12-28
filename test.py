from storage.json_store import load_tasks, save_tasks


tasks = load_tasks()
print(type(tasks))