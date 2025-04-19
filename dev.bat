@echo off
setlocal

echo 🔍 Checking for running Django dev servers...

:: Kill any existing runserver processes
tasklist /v /fo csv > _tasklist.txt
findstr /i "runserver" _tasklist.txt > _runservers.txt

for /f "tokens=2 delims=," %%a in (_runservers.txt) do (
    echo 🛑 Killing old Django server process: PID %%a
    taskkill /F /PID %%a >nul 2>&1
)

del _tasklist.txt
del _runservers.txt

:: Set up environment
set VENV_PATH=venv\Scripts\activate.bat

if "%1"=="" (
    echo ❌ No command provided.
    exit /b 1
)

call %VENV_PATH%

:: Handle startapp (this is the magic)
if /i "%1"=="startapp" (
    if "%2"=="" (
        echo ❌ No application name provided.
        exit /b 1
    )
    set "APP_NAME=%2"
  
    echo 🔍 Starting Django app creation process for: %APP_NAME%
  
    shift
    shift
    pushd core
    echo 🔨 Creating Django app: %APP_NAME%
    poetry run django-admin startapp %2
    popd
    goto :eof
)

:: Other manage.py commands
poetry run py -m core.manage %*
