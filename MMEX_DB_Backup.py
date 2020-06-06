import os, shutil

source = r'C:\Users\Michael\Documents\MMEX_DB'
cloud_backup = r'C:\Users\Michael\Dropbox\Money_Manager_DB'
pendrive_backup = r'I:\MMEX_DB'

log = []
def backup (source, destination):
    files = os.listdir(source)
    try:
        shutil.copytree(source, destination)
        print(f"Directory copied to {destination}")
    except:
        print(f"Directory {destination} already exists! Instead - "
              f"the files from the {source} directory will be modified!")
        for file in files:
            file_path = os.path.join(source, file)
            shutil.copy(file_path, destination)
            log.append(file)
        print(log)

if __name__ == '__main__':
    if os.path.exists(pendrive_backup.split('\\')[0]):
        backup(source, pendrive_backup)
        print(f"Files from {source} backed up to pendrive!")
    else:
        print(f"Pendrive disconnected, couldn't backup {source} to it.")
    backup(source, cloud_backup)
    print(f"Files from {source} backed up to Dropbox!")
    print("DONE!")