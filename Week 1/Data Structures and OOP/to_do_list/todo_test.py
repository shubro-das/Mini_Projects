from core.todo_manager import TodoManager
from models.task import Task

todo = TodoManager()
for task in todo.list_tasks():
    print(task.to_string())
 
todo.add_task("T001", "Follow the data science roadmap")
todo.add_task("T002", "Research paper writing")


# print("Checking the list of tasks after adding two tasks:")
# for task in todo.list_tasks():
#     print(task.to_string())

# todo.mark_task_done("T001") # Mark the first task as completed
# print("After marking T001 done:")
# for task in todo.list_tasks():  
#     print(task.to_string())


# print("Attempting to add a non-duplicate task:  T003")

# if todo.add_task("T003", "Duplicate task attempt"):
#     print("Task added successfully.")
# else:
#     print("Task with this ID already exists. Cannot add duplicate.")

# for task in todo.list_tasks():
#     print(task.to_string())



# print("Attempting to get a task with ID T001:")
# todo.get_task("T002")  # Should return the task with ID T001
# print(todo.get_task("T002").to_string())  # Print the task details


# print("Deleting task T001:")
# todo.delete_task("T001")  # Delete the task with ID T001
# print("Current task list after deletion:")  
# for task in todo.list_tasks():
#     print(task.to_string())  # Print remaining tasks after deletion