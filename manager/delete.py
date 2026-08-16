from manager.todo_manager import TaskManager


def main(user_input):
	manager = TaskManager()
	manager.delete(user_input.id)
