import argparse
from services.task_services import add_task, list_tasks, mark_done, delete_task
# thsi is the parser 

def run():
    parser = argparse.ArgumentParser(description="A simple script parser")
    sub = parser.add_subparsers(dest="command")
    # add arguments 

    add = sub.add_parser("add")
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
        task = add_task(args.title, args.due)
        print("Added: ", task)
    else:
        parser.print_help()
