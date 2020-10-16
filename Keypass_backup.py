import os
import shutil

source_directory = r'C:\Users\Michael\Documents\Accounts_Passes.kdbx'
file_name = source_directory.split('\\')[-1]
cloud_backup = r'C:\Users\Michael\Dropbox\Backup'
pendrive_backup = r'J:'


def backup(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    shutil.copy(source, destination)


if __name__ == '__main__':
    if os.path.exists(pendrive_backup.split('\\')[0]):
        backup(source_directory, pendrive_backup)
        print(f"{file_name} file backed up to pendrive!")
    else:
        print(f"Pendrive disconnected, couldn't backup {file_name} to it")
    backup(source_directory, cloud_backup)
    print(f"{file_name} file backed up to Dropbox!")
    print("DONE!")
