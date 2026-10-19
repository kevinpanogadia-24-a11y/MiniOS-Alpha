# MiniOS Alpha — Technical Documentation

## 1. Project Overview

MiniOS Alpha is a command-line operating system simulator developed using Python. It demonstrates basic operating system concepts through text-based commands.

## 2. Objectives

- To simulate a command-line interface.
- To implement basic user login.
- To provide simulated file management.
- To demonstrate process management.
- To demonstrate memory management.
- To handle invalid commands and user input.

## 3. Technologies Used

- Programming Language: Python
- Code Editor: Visual Studio Code
- Interface: Command-Line Interface (CLI)

## 4. System Architecture

MiniOS Alpha receives commands from the user through the terminal. The program processes each command, performs the corresponding simulated operation, and displays the result.

The main program is stored in `main.py`.

## 5. Main Components

### 5.1 User Authentication

The login component checks the username and password before allowing access to the command interface.

### 5.2 Command-Line Shell

The shell accepts commands such as `help`, `date`, `time`, `whoami`, `systeminfo`, and `exit`.

### 5.3 File Management

File commands include `dir`, `mkdir`, `create`, `read`, `write`, and `delete`. These commands demonstrate basic file operations according to the implemented code.

### 5.4 Process Management

The commands `process`, `run`, and `kill` simulate process listing, starting, and termination.

### 5.5 Memory Management

The commands `memory`, `allocate`, and `free` simulate memory usage and allocation.

### 5.6 Error Handling

The program should handle unknown commands and missing or invalid input by displaying appropriate messages.

## 6. Execution Procedure

1. Install Python 3.
2. Open the MiniOS project folder in Visual Studio Code.
3. Open the integrated terminal.
4. Execute `py main.py`.
5. Log in using a valid account.
6. Enter commands and observe the output.
7. Enter `exit` to close the program.

## 7. Testing

The project should be tested using valid and invalid commands. Test login, basic shell commands, file operations, process commands, memory commands, and program exit. Record the actual results and include screenshots as evidence.

## 8. Limitations

MiniOS Alpha is a learning project and does not replace a real operating system. Process and memory operations are simulated. Some behavior depends on the implementation in `main.py`.

## 9. Conclusion

MiniOS Alpha provides a practical introduction to command-line interfaces and basic operating system concepts using Python.

## 10. Project Developers

Group Members: Add the names of all group members.

