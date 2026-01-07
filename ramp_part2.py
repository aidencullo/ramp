# Level 1: Implement basic CRUD operations for tasks, focusing on creation, updating, deletion, and retrieval.
# Level 2: Extend the system to support multi-key sorting of tasks based on priority and creation order.


from simple_task_management_system import SimpleTaskManagementSystem
from datetime import datetime

class Task:
    def __init__(self, desc: str, priority: int = 0):
        self.desc = desc
        self.priority = priority
        self.creation_date = datetime.now()

    def set_priority(self, priority):
        self.priority = priority

    def update_description(self, new_description):
        self.desc = new_description

    def get_desc(self):
        return self.desc
        
class SimpleTaskManagementSystemImpl(SimpleTaskManagementSystem):

    def __init__(self):
        self.ids = {}

    def create_task(self, timestamp: int, task_id: str, description: str) -> bool:
        """
        Creates a new task with the specified task_id and description. Returns True if the task was created successfully, or False if a task with the task_id already exists.
        """
        if task_id in self.ids:
            return False

        task = Task(description)

        self.ids[task_id] = task
        return True

    def update_task(self, timestamp: int, task_id: str, new_description: str) -> bool:
        """
        Updates the description of the task with the specified task_id. Returns True if the task was updated successfully, or False if the task does not exist.
        """
        if task_id not in self.ids:
            return False

        self.ids[task_id].update_description(new_description)
        return True

    def get_task(self, timestamp: int, task_id: str) -> str | None:
        """
        Retrieves the description of the task with the specified task_id. Returns the task description if it exists, or None otherwise.
        """
        return self.ids.get(task_id).get_desc() if task_id in self.ids else None 

    def delete_task(self, timestamp: int, task_id: str) -> bool:
        """
        Deletes the task with the specified task_id. Returns True if the task was deleted successfully, or False if the task does not exist.
        """
        return task_id in self.ids and self.ids.pop(task_id) is not None

    def set_task_priority(self, timestamp: int, task_id: str, priority: int) -> bool:
        """
        Sets the priority of the task with the specified task_id. Returns True if the priority was set successfully, or False if the task does not exist. Tasks without an explicitly set priority are considered to have a default priority of 0.
        """
        if task_id not in self.ids:
            return False

        self.ids[task_id].set_priority(priority)
        return True
    

    def list_tasks_sorted(self, timestamp: int) -> list[str]:
        """
        Returns a list of all task IDs sorted by multiple keys: first by priority in descending order (highest priority first), then by creation order in ascending order (earliest created first) for tasks with the same priority. Returns an empty list if no tasks exist.
        """
        return [f'task{i}' for i in sorted(self.ids.items(), key=lambda kv: (-kv[1].priority, kv[1].creation_date))]
