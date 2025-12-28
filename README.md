# Project Structure explain

```
.
├── cli
│   └── commands.py
├── data
│   └── tasks.json
├── main.py
├── models
│   └── task.py
├── README.md
├── services
│   └── task_services.py
└── storage
    └── json_store.py
```

1. `main.py`
   - Entry Point nia mak nanti route command ba iha backend nia logic
2. `cli/commands.py`
   1. Handle User input husi terminal 
   2. Translate command ba iha function call iha python 
3. models/task.py
   1. Define Task ida 
   2. fields: `id`. `title`, `status`, `due`, `created_at`
   3. Exemplo karik hanesan ho iha `models.py` iha django nian
4. services/task_service.py
   1. Contain funciotn sira hanesan `add_task()`, `list_task()`, `mark_done()`, `delete_task()`
   2. Nia mak contain nia bussiness logic 
5. storage/json_store.py
   1. Nia mak rai Data iha task.json
6. data/tasks.json
   1. Fatin ne'ebe sei store tasks sira iha laran


## models/task.py

