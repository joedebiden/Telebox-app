@echo off
title (app) Telegram-Telebox - by Baudelaire
chcp 65001 >nul
mode con: cols=175 lines=45
setlocal EnableDelayedExpansion
set "ESC="

call :banner
if not exist ".venv\Scripts\activate.bat" (
    echo python virtual environment not found, creating it...
    python -m venv .venv
    call .venv\Scripts\activate
    pip install -r requirements.txt
) else (
    call .venv\Scripts\activate
)

:start
call :banner

:menu
call :banner
for /f %%A in ('"prompt $H &echo on &for %%B in (1) do rem"') do set BS=%%A
echo.
echo.
echo                ╔══(1) Manage Telegram Account
echo                ║
echo                ╠═══(2) Manage Proxies
echo                ║
echo                ╠════(3) Telegram-Scraper
echo                ║
echo                ╠═════(4) Telegram-Adder
echo                ║
echo                ╚═╦════(5) Telegram-Message-Sender
echo                  ║
set /p input=.%BS%                 ╚════════^>
if /I %input% EQU 1 python account.py
if /I %input% EQU 2 python auth.py
if /I %input% EQU 3 python scraper.py
if /I %input% EQU 4 python adder.py
if /I %input% EQU 5 python sender.py
cls
goto start

set "colors[1]=%ESC%[38;2;128;0;128m"  rem Violet
set "colors[2]=%ESC%[38;2;102;0;153m"
set "colors[3]=%ESC%[38;2;76;0;179m"
set "colors[4]=%ESC%[38;2;51;0;204m"
set "colors[5]=%ESC%[38;2;25;0;230m"
set "colors[6]=%ESC%[38;2;0;0;255m"   rem Bleu


:banner
cls
echo.
echo.
echo !colors[1]!       ████████╗███████╗██╗     ███████╗ ██████╗ ██████╗  █████╗ ███╗   ███╗   ████████╗ ██████╗  ██████╗ ██╗     ██████╗  ██████╗ ██╗  ██╗
echo !colors[2]!       ╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗████╗ ████║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔══██╗██╔═══██╗╚██╗██╔╝
echo !colors[3]!          ██║   █████╗  ██║     █████╗  ██║  ███╗██████╔╝███████║██╔████╔██║█████╗██║   ██║   ██║██║   ██║██║     ██████╔╝██║   ██║ ╚███╔╝ 
echo !colors[4]!          ██║   ██╔══╝  ██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║╚════╝██║   ██║   ██║██║   ██║██║     ██╔══██╗██║   ██║ ██╔██╗ 
echo !colors[5]!          ██║   ███████╗███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║      ██║   ╚██████╔╝╚██████╔╝███████╗██████╔╝╚██████╔╝██╔╝ ██╗
echo !colors[6]!          ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝
echo.
echo %ESC%[0m


