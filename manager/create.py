import json

from manager.todo_manager import Todo

FILE_NAME = "config.json"


def write_empty_object():
	with open(FILE_NAME, "w") as config:
		json.dump({}, config)


# if we have a exception where the json is empty and we read it the code crashes, to prevent the crash we write empty object to the json if its empty
def check_for_empty():
	with open(FILE_NAME, "r") as config:
		if not config.read():
			write_empty_object()


def create_file():
	try:
		with open(FILE_NAME, "x"):
			pass
		write_empty_object()
	except FileExistsError:
		check_for_empty()


def create_save(todo: Todo):
	create_file()

	# read and cache already loaded json so we can update it
	config_parsed: dict
	with open(FILE_NAME, "r") as config:
		config_parsed = json.load(config)

	# update logic
	dict_id = len(config_parsed) + 1
	config_parsed.update({dict_id: todo.to_dict()})
	with open(FILE_NAME, "w") as config:
		json.dump(config_parsed, config)


def main(user_input):
	print(user_input)

	todo = Todo(user_input.description, user_input.status)

	create_save(todo)
