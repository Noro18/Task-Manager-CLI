import argparse
from services.task_services import add_task, list_tasks, mark_done, delete_task
# thsi is the parser 

def run():
    parser = argparse.ArgumentParser(description="A simple script parser") # 
    sub = parser.add_subparsers(dest="command")
    # add arguments 

    add = sub.add_parser("add") # this is the commands 
    add.add_argument("title")
    add.add_argument("--due")

    list_cmd = sub.add_parser('list')
    list_cmd.add_argument('--status')

    # Mark Done command 

    done = sub.add_parser('done')
    done.add_argument("id", type=int)

    delete = sub.add_parser('delete')
    delete.add_argument('id', type=int)

    args = parser.parse_args()


    if args.command == 'add':
        task = add_task(args.title)
        print("Added: ", task)

    elif args.command == 'list':
        
        for t in list_tasks(args.status):
            print(t)
    elif args.command == 'done':
        task = mark_done(args.id)
        print(f"Done: {task}")
    else:
        parser.print_help()
