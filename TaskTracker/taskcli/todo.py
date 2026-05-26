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
        for i, task in tasks:
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
        for i, task in tasks:
            if task["id"] == id:
                tasks["status"] = status
                data["tasks"] = tasks
                write_json_file(data=data)
                return True
        return False

    # 3. List all tasks
    def list_all(self):
        data = read_json_file()
        tasks = data["tasks"]

        print(f"")
        

    # 4. List all tasks that are done
    def list_done_tasks(self):
        pass

    # 5. List all tasks that are not done
    def list_not_done_tasks(self):
        pass

    # 6. List all tasks that are in progress
    def list_in_progress_tasks(self):
        pass
