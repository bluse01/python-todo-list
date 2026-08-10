import argparse

from manager.create import main as create
from manager.delete import main as delete

parser = argparse.ArgumentParser(prog="task-tracker-cli")

subparsers = parser.add_subparsers(dest="command", required=True)

parser_add = subparsers.add_parser("add", help="create new todo")
parser_add.add_argument("description", help="todos description")
parser_add.add_argument(
    "--status",
    choices=["todo", "in-progress", "done"],
    default="in-progress",
    help="todos status",
)

parser_delete = subparsers.add_parser("delete", help="deletes the todo by id")
parser_delete.add_argument("id", type=int, help="the id of the todo")

args = parser.parse_args()

match args.command:
    case "add":
        create()
    case "delete":
        delete()
