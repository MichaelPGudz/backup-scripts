@echo off
echo Backup scripts launched in:
timeout /T 5
"C:\Program Files (x86)\Python38-32\python.exe" "C:\Users\Michael\OneDrive - Jacobs\Python Project\Backup Scripts\Keypass_backup.py"
"C:\Program Files (x86)\Python38-32\python.exe" "C:\Users\Michael\OneDrive - Jacobs\Python Project\Backup Scripts\MMEX_DB_Backup.py"
pause