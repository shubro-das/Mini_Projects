# project_todo_app/ui/interface.py

from core.todo_manager import TodoManager

def run_todo_app():
    manager = TodoManager()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ").strip()

        if choice == "1":
            task_id = input("Enter Task ID (e.g., T001): ").strip()
            description = input("Enter Task Description: ").strip()
            if manager.add_task(task_id, description):
                print("✅ Task added successfully.")
            else:
                print("❌ Task ID already exists.")

        elif choice == "2":
            task_id = input("Enter Task ID to mark as done: ").strip()
            if manager.mark_task_done(task_id):
                print("✅ Task marked as done.")
            else:
                print("❌ Task not found.")

        elif choice == "3":
            task_id = input("Enter Task ID to delete: ").strip()
            confirm = input("Are you sure? (y/n): ").strip().lower()
            if confirm == "y":
                if manager.delete_task(task_id):
                    print("🗑️ Task deleted.")
                else:
                    print("❌ Task not found.")
            else:
                print("Cancelled.")

        elif choice == "4":
            tasks = manager.list_tasks()
            if not tasks:
                print("📭 No tasks found.")
            else:
                print("\n📋 Your Tasks:")
                for task in tasks:
                    print(task.to_string())

        elif choice == "5":
            manager.save_to_file()
            print("Data saved. 👋 Exiting To-Do App. Goodbye!")
            break

        else:
            print("⚠️ Invalid input. Please enter a number between 1 and 5.")
