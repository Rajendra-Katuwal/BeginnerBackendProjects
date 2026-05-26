import argparse
from taskcli.todo import Todo
from taskcli.json_utils import Status, init_json_file
import json


def setup_parser() -> argparse.ArgumentParser:
    # Parser setup and configuration for our cli
    parser = argparse.ArgumentParser(
        description="A CLI Todo management tool",
        epilog='Example taskcli add "Buy Groceries"',
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
    list_parser.add_argument(
        "status", type=str, nargs="?", default=None, help="status to filter the task by"
    )

    return parser


def command_to_method_mapping(parser: argparse.ArgumentParser, todo: Todo):
    args = parser.parse_args()

    if args.operator == "add":
        new_task = todo.add_todo(args.title)
        print(f"New Task = {json.dumps(new_task, indent=2)}")

    if args.operator == "update":
        updated_task = todo.update_todo(id=args.id, title=args.title)
        (
            print(f"Task updated successfully")
            if updated_task
            else print(f"Update unsucessful")
        )

    if args.operator == "delete":
        deleted_task = todo.delete_todo(id=args.id)
        (
            print(f"Task Deleted successfully")
            if deleted_task
            else print(f"Task Deletion unsucessful")
        )

    if args.operator == "mark-in-progress":
        marked = todo.mark_task(id=args.id, status="in_progress")
        (
            print(f"Task Marked as in-progress successfully")
            if marked
            else print(f"Task Mark as in-progress unsucessful")
        )

    if args.operator == "mark-done":
        marked = todo.mark_task(id=args.id, status="done")
        (
            print(f"Task Marked as done successfully")
            if marked
            else print(f"Task Mark as done unsucessful")
        )

    if args.operator == "list":
        if args.status == None:
            todo.list_all()
        if args.status == "todo":
            todo.list_todo_tasks()
        if args.status == "in_progress":
            todo.list_in_progress_tasks()
        if args.status == "done":
            todo.list_done_tasks()


def main():
    # Ensure that the file is created initially
    init_json_file()

    # Setup cli parser and command and subcommands along with the arguments required
    parser = setup_parser()

    # Todo instance to access all the required method
    todo = Todo()

    # Using the parser and using the functions to perform the actions
    command_to_method_mapping(parser=parser, todo=todo)


if __name__ == "__main__":
    main()
