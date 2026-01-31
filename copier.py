import shutil
import os
import time

USB_DRIVE = "F:/"      # Change to your USB letter
BACKUP_FOLDER = "C:/USB_Backup/"  # Folder on your PC

def copy_files():
    if not os.path.exists(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)

    for root, dirs, files in os.walk(USB_DRIVE):
        for file in files:
            source = os.path.join(root, file)
            relative_path = os.path.relpath(source, USB_DRIVE)
            destination = os.path.join(BACKUP_FOLDER, relative_path)

            dest_dir = os.path.dirname(destination)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            shutil.copy2(source, destination)
            print(f"Copied: {source} -> {destination}")

def wait_for_usb():
    print("Waiting for your USB drive...")

    while True:
        if os.path.exists(USB_DRIVE):
            print("USB detected! Copying files...")
            copy_files()
            print("Backup complete!")
            break
        time.sleep(1)

wait_for_usb()
