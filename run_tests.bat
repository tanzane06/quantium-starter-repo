@echo off
REM This batch script activates the virtual environment, runs the test suite,
REM and exits with an appropriate status code.

ECHO --- Activating virtual environment ---
CALL venv\Scripts\activate.bat

REM Check if the virtual environment was successfully activated
IF NOT DEFINED VIRTUAL_ENV (
    ECHO ERROR: Failed to activate the virtual environment. Make sure the 'venv' folder exists.
    EXIT /B 1
)

ECHO --- Running Pytest test suite ---
pytest

REM Check the exit code of the last command (pytest).
REM ERRORLEVEL 0 means success, any other value means failure.
IF ERRORLEVEL 1 (
    ECHO ERROR: Pytest reported failing tests.
    EXIT /B 1
)

ECHO --- All tests passed successfully! ---
EXIT /B 0
```

### What This Script Does:

* `@echo off`: Prevents the commands themselves from being displayed in the terminal, keeping the output clean.
* `ECHO ...`: Prints a status message to the screen.
* `CALL venv\Scripts\activate.bat`: Activates your Python virtual environment.
* `pytest`: Runs your test suite using the Pytest framework.
* `IF ERRORLEVEL 1 (...)`: Checks the result of the `pytest` command. If it fails, the script prints an error message and exits with code `1`.
* `EXIT /B 0`: If the tests pass, the script exits with code `0`, indicating success.

### How to Run the Script

1.  Open your **Command Prompt** (not PowerShell).
2.  Navigate to your project folder.
3.  Simply type the name of the script and press Enter:
    ```cmd
    run_tests.bat
    
