@echo off

:: Sprawdzanie, czy Docker jest zainstalowany
echo Sprawdzanie, czy Docker jest zainstalowany...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Docker nie jest zainstalowany lub nie znajduje się w PATH. Zainstaluj Docker i spróbuj ponownie.
    pause
    exit /b
)

:: Menu wyboru
:MENU
cls
echo ========================================
echo        Zarządzanie programem
echo ========================================
echo 1. Włącz program
echo 2. Wyłącz program
echo 3. Wyjście
echo ========================================
set /p choice=Wybierz opcję (1-3): 

if "%choice%"=="1" goto START_PROGRAM
if "%choice%"=="2" goto STOP_PROGRAM
if "%choice%"=="3" goto EXIT
echo Nieprawidłowa opcja. Spróbuj ponownie.
pause
goto MENU

:START_PROGRAM
echo Włączanie programu....
docker-compose up -d
if %errorlevel% neq 0 (
    echo Wystąpił błąd podczas włączania programu.
    pause
    goto MENU
)
echo Program został włączony!
pause
goto MENU

:STOP_PROGRAM
echo Wyłączanie programu....
docker-compose down
if %errorlevel% neq 0 (
    echo Wystąpił błąd podczas wyłączania programu.
    pause
    goto MENU
)
echo Program został wyłączony!
pause
goto MENU

:EXIT
echo Do widzenia!
exit /b
