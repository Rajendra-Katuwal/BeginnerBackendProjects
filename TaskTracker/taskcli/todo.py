from taskcli.json_utils import Status, read_json_file, write_json_file


class Todo:
    def __init__(self):
        pass

    # 1. Add, Update, and Delete tasks
    def add_todo(self, title: str):
        data = read_json_file()
        tasks = data["tasks"]
        curr_id = 1 if len(tasks) == 0 else int(tasks[-1]["id"]) + 1

        new_task = {"id": curr_id, "title": title, "status": "todo"}

        tasks.append(new_task)
        data["tasks"] = tasks

        write_json_file(data=data)
        return new_task

    def update_todo(self, id: int, title: str) -> bool:
        data = read_json_file()
        tasks = data["tasks"]
        for task in tasks:
            if task["id"] == id:
                task["title"] = title
                data["tasks"] = tasks
                write_json_file(data=data)
                return True

        return False

    def delete_todo(self, id: int, title: str):
        data = read_json_file()
        tasks = data["tasks"]
        for task in tasks:
            if task["id"] == id:
                tasks.remove(task)
                data["tasks"] = tasks
                write_json_file(data=data)
                return True
        return False

    # 2. Mark a task as in progress or done
    def mark_task(self, id: int, status: Status):
        data = read_json_file()
        tasks = data["tasks"]
        for task in tasks:
            if task["id"] == id:
                task["status"] = status
                data["tasks"] = tasks
                write_json_file(data=data)
                return True
        return False

    # 3. List all tasks
    def list_all(self):
        data = read_json_file()
        tasks = data["tasks"]

        if not tasks:
            print("No tasks found.")
            return

        # Print table header
        print(f"\n{'ID':<5} {'Title':<50} {'Status':<15}")
        print("-" * 70)

        # Print each task as a row
        for task in tasks:
            task_id = task["id"]
            title = task["title"]
            status = task["status"]
            print(f"{task_id:<5} {title:<50} {status:<15}")

    # 4. List all tasks that are done
    def list_done_tasks(self):
        data = read_json_file()
        tasks = data["tasks"]

        if not tasks:
            print("No tasks found with status--Done.")
            return

        # Print table header
        print("Tasks with Done status")
        print(f"\n{'ID':<5} {'Title':<50} {'Status':<15}")
        print("-" * 70)

        # Print each task as a row
        for task in tasks:
            if task["status"] == "done":
                task_id = task["id"]
                title = task["title"]
                status = task["status"]
                print(f"{task_id:<5} {title:<50} {status:<15}")

    # 5. List all tasks that are not done
    def list_todo_tasks(self):
        data = read_json_file()
        tasks = data["tasks"]

        if not tasks:
            print("No tasks found with status--ToDo.")
            return

        # Print table header
        print("Tasks with ToDo status")
        print(f"\n{'ID':<5} {'Title':<50} {'Status':<15}")
        print("-" * 70)

        # Print each task as a row
        for task in tasks:
            if task["status"] == "todo":
                task_id = task["id"]
                title = task["title"]
                status = task["status"]
                print(f"{task_id:<5} {title:<50} {status:<15}")

    # 6. List all tasks that are in progress
    def list_in_progress_tasks(self):
        data = read_json_file()
        tasks = data["tasks"]

        if not tasks:
            print("No tasks found with status--InProgress.")
            return

        # Print table header
        print("Tasks with InProgress status")
        print(f"\n{'ID':<5} {'Title':<50} {'Status':<15}")
        print("-" * 70)

        # Print each task as a row
        for task in tasks:
            if task["status"] == "in_progress":
                task_id = task["id"]
                title = task["title"]
                status = task["status"]
                print(f"{task_id:<5} {title:<50} {status:<15}")
