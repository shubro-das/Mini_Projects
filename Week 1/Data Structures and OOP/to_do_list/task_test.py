from models.task import Task

t1 = Task("01", "Complete the project documentation")

print(t1.to_string())  # Should return "[01] Complete the project documentation - ❌ Not Done"

t1.mark_done()  # Mark the task as completed

print(t1.to_string())  # Should return "[01] Complete the project documentation - ✅ Done"