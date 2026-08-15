from manager.todo_manager import TaskManager


def main(user_input):
	if not user_input.description and not user_input.status:
		print("No fields provided to update")
		print("Both fields can't be empty")
		return

	manager = TaskManager()
	manager.update_task(user_input.id, user_input.description, user_input.status)
