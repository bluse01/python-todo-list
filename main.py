import argparse

from manager.create import main as create
from manager.delete import main as delete
from manager.list import main as list_todos
from manager.update import main as update

parser = argparse.ArgumentParser(prog="task-tracker-cli")

subparsers = parser.add_subparsers(dest="command", required=True)

progress_choices = ["todo", "in-progress", "done"]

parser_add = subparsers.add_parser("add", help="create new todo")
parser_add.add_argument("description", help="todos description")
parser_add.add_argument(
	"-s",
	"--status",
	choices=progress_choices,
	default="in-progress",
	help="todos status",
)

parser_delete = subparsers.add_parser(
	"update", help="updates the selected todos description"
)
parser_delete.add_argument("id", type=str, help="the id of the todo")
parser_delete.add_argument("description", help="the description u want to update with")

parser_delete = subparsers.add_parser("delete", help="deletes the todo by id")
parser_delete.add_argument("id", type=int, help="the id of the todo")

parser_delete = subparsers.add_parser("list", help="list selected todos")
parser_delete.add_argument(
	"-s",
	"--status",
	choices=progress_choices,
	help="get the todos by the status",
)
parser_delete.add_argument(
	"-l",
	"--limit",
	type=int,
	default=10,
	help="how many todos to display. default = 10",
)

args = parser.parse_args()

match args.command:
	case "add":
		create(args)
	case "delete":
		delete(args)
	case "list":
		list_todos(args)
	case "update":
		update(args)
