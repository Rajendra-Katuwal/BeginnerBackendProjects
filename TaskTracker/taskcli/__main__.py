import argparse
from taskcli.todo import Todo
from taskcli.json_utils import Status, init_json_file
import json


def main():
    # Ensure that the file is ccreated initiall
    init_json_file()

    # Parser setup and configuration for our cli
    parser = argparse.ArgumentParser(
        description="A CLI Todo management tool",
        epilog='Example task-cli add "Buy Groceries"',
    )
    subparsers = parser.add_subparsers(title="Operators", dest="operator")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="New task title")

    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("id", type=int, help="id of the task to be updated")
    update_parser.add_argument("title", type=str, help="updated task title")

    delete_parser = subparsers.add_parser("delete", help="delete an existing task")
    delete_parser.add_argument("id", type=int, help="id of the task to be deleted")

    mark_in_progress_parser = subparsers.add_parser(
        "mark-in-progress", help="mark an existing task as in_progress"
    )
    mark_in_progress_parser.add_argument(
        "id", type=int, help="id of the task to be mark as in_progress"
    )

    mark_done_parser = subparsers.add_parser(
        "mark-done", help="mark an existing task as done"
    )
    mark_done_parser.add_argument(
        "id", type=int, help="id of the task to be mark as done"
    )

    list_parser = subparsers.add_parser("list", help="List all the existing tasks")
    list_parser.add_argument("status", type=Status, help="status to filter the task by")

    # Using the parser and using the functions to perform the actions
    args = parser.parse_args()
    todo = Todo()

    if args.operator == "add":
        new_task = todo.add_todo(args.title)
        print(f"New Task = {json.dumps(new_task, indent=2)}")

    if args.operator =="update":
        updated_task = todo.update_todo(id=args.id, title=args.title)
        print(f"Task updated successfully") if updated_task else print(f"Update unsucessful")


if __name__ == "__main__":
    main()
