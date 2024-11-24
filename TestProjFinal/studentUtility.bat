@echo off
@REM PathToPythonExe PathToStudentUtilityPythonScriptLocation
if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
"C:/Python3.11.1/python.exe" "C:/path/to/the/script/studentUtility.py"
exit
