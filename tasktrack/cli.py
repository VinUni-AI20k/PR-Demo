import argparse

from .storage import Storage


def main() -> None:
    parser = argparse.ArgumentParser(prog="tasktrack")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add", help="Add a task")
    p_add.add_argument("title")

    sub.add_parser("list", help="List all tasks")

    p_done = sub.add_parser("done", help="Mark a task done")
    p_done.add_argument("task_id", type=int)

    args = parser.parse_args()
    store = Storage()

    if args.cmd == "add":
        t = store.add(args.title)
        print(f"[{t.id}] {t.title}")
    elif args.cmd == "list":
        for t in store.list():
            mark = "x" if t.done else " "
            print(f"[{mark}] {t.id:>3}  {t.title}")
    elif args.cmd == "done":
        store.mark_done(args.task_id)
        print(f"Marked task {args.task_id} done")

    store.close()


if __name__ == "__main__":
    main()
