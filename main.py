
import os
import time
from datetime import datetime

OS_NAME = "MiniOS Alpha"
VERSION = "1.0"
TOTAL_MEMORY = 1024

USERS = {
    "admin": "admin123",
    "student": "student123"
}

current_user = None
files = {}
directories = ["Documents"]
processes = {}
next_pid = 1
used_memory = 0


def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 40)
    print(f"       {OS_NAME} v{VERSION}")
    print("=" * 40)
    print("Welcome to MiniOS!\n")


def login():
    global current_user

    print("=" * 40)
    print("             MiniOS Login")
    print("=" * 40)

    for attempt in range(3):
        username = input("Username: ").strip()
        password = input("Password: ")

        if USERS.get(username) == password:
            current_user = username
            print(f"\nLogin successful. Welcome, {username}!")
            time.sleep(1)
            return True

        print("Invalid username or password.\n")

    print("Too many failed attempts. Exiting MiniOS.")
    return False


def show_help():
    print("""
Available Commands:
  help                  Show available commands
  clear                 Clear the screen
  date                  Show the current date
  time                  Show the current time
  whoami                Show the current user
  dir                   List files and directories
  mkdir <folder>        Create a directory
  create <file>         Create an empty file
  read <file>           Display file contents
  write <file>          Write or replace file contents
  delete <file>         Delete a file
  process               List simulated processes
  run <name>            Start a simulated process
  kill <PID>            Terminate a simulated process
  memory                Show simulated memory usage
  allocate <MB>         Allocate simulated memory
  free <MB>             Release simulated memory
  systeminfo            Show system information
  exit                  Shut down MiniOS
""")


def file_command(command, args):
    if command == "dir":
        print("\nDirectory listing:")
        for folder in directories:
            print(f"  <DIR>  {folder}")
        for name in files:
            print(f"         {name}")
        if not directories and not files:
            print("Directory is empty.")

    elif command == "mkdir":
        if len(args) != 1:
            print("Usage: mkdir <folder>")
        elif args[0] in directories or args[0] in files:
            print("Error: Name already exists.")
        else:
            directories.append(args[0])
            print("Directory created.")

    elif command == "create":
        if len(args) != 1:
            print("Usage: create <file>")
        elif args[0] in files or args[0] in directories:
            print("Error: Name already exists.")
        else:
            files[args[0]] = ""
            print("File created.")

    elif command == "read":
        if len(args) != 1:
            print("Usage: read <file>")
        elif args[0] not in files:
            print("Error: File does not exist.")
        else:
            print(files[args[0]] or "(File is empty)")

    elif command == "write":
        if len(args) < 2:
            print("Usage: write <file> <content>")
        elif args[0] not in files:
            print("Error: File does not exist.")
        else:
            files[args[0]] = " ".join(args[1:])
            print("File saved.")

    elif command == "delete":
        if len(args) != 1:
            print("Usage: delete <file>")
        elif args[0] not in files:
            print("Error: File does not exist.")
        else:
            del files[args[0]]
            print("File deleted.")


def process_command(command, args):
    global next_pid

    if command == "run":
        if len(args) != 1:
            print("Usage: run <name>")
            return

        pid = next_pid
        next_pid += 1
        processes[pid] = {"name": args[0], "status": "RUNNING"}

        print("\nProcess started.")
        print(f"PID: {pid}")
        print(f"Name: {args[0]}")
        print("Status: RUNNING")

    elif command == "process":
        print(f"\n{'PID':<8}{'NAME':<20}{'STATUS'}")
        print("-" * 40)
        if not processes:
            print("No processes.")
        for pid, proc in processes.items():
            print(f"{pid:<8}{proc['name']:<20}{proc['status']}")

    elif command == "kill":
        if len(args) != 1:
            print("Usage: kill <PID>")
            return
        try:
            pid = int(args[0])
        except ValueError:
            print("Error: PID must be a number.")
            return

        if pid not in processes:
            print("Error: Process does not exist.")
        else:
            processes[pid]["status"] = "TERMINATED"
            print(f"Process {pid} terminated.")


def memory_command(command, args):
    global used_memory

    if command == "memory":
        print("\nMemory Status")
        print("-" * 30)
        print(f"Total Memory: {TOTAL_MEMORY} MB")
        print(f"Used Memory:  {used_memory} MB")
        print(f"Free Memory:  {TOTAL_MEMORY - used_memory} MB")

    else:
        if len(args) != 1:
            print(f"Usage: {command} <MB>")
            return

        try:
            amount = int(args[0])
            if amount <= 0:
                print("Error: Amount must be positive.")
                return
        except ValueError:
            print("Error: Enter a valid number.")
            return

        if command == "allocate":
            if amount > TOTAL_MEMORY - used_memory:
                print("Error: Not enough free memory.")
            else:
                used_memory += amount
                print(f"{amount} MB allocated.")

        elif command == "free":
            if amount > used_memory:
                print("Error: Cannot release more memory than is used.")
            else:
                used_memory -= amount
                print(f"{amount} MB released.")


def system_info():
    print("\n" + "=" * 40)
    print("          SYSTEM INFORMATION")
    print("=" * 40)
    print(f"OS Name: {OS_NAME}")
    print(f"Version: {VERSION}")
    print("Architecture: 64-bit (simulated)")
    print("CPU: Virtual CPU")
    print(f"Memory: {TOTAL_MEMORY} MB")
    print(f"User: {current_user}")
    print("=" * 40)


def main():
    banner()

    if not login():
        return

    while True:
        try:
            user_input = input(f"\n{OS_NAME}> ").strip()
            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()
            args = parts[1:]

            if command == "help":
                show_help()
            elif command == "clear":
                os.system("cls" if os.name == "nt" else "clear")
            elif command == "date":
                print(datetime.now().strftime("%Y-%m-%d"))
            elif command == "time":
                print(datetime.now().strftime("%H:%M:%S"))
            elif command == "whoami":
                print(f"Current User: {current_user}")
            elif command in ("dir", "mkdir", "create", "read",
                             "write", "delete"):
                file_command(command, args)
            elif command in ("process", "run", "kill"):
                process_command(command, args)
            elif command in ("memory", "allocate", "free"):
                memory_command(command, args)
            elif command == "systeminfo":
                system_info()
            elif command == "exit":
                print("\nShutting down MiniOS...")
                print("Goodbye!")
                break
            else:
                print("Unknown command.")
                print("Type 'help' to see available commands.")

        except (EOFError, KeyboardInterrupt):
            print("\nShutting down MiniOS...")
            break
        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
