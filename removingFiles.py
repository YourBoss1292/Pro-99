import shutil
import os
import time

def main():
	deleted_folders_count = 0
	deleted_files_count = 0

	path = /path_to_delete

	days = 30

	seconds = time*time() - (days * 24* 60* 60)

	if os.path.exists(path):

		for root_folder, folders, files in os.walk(path):

		if seconds >= get_file_or_folder_age(root_folder):
			remove_folder(root_folder)

			deleted_folders_count =+ 1

			break

		else:

			for folder in folders:

				folder_path = os.path.join(root_folders,folder)

				if seconds >= get_file_or_folder_age(folder_path):
					remove_folder(folder_path)
					deleted_folders_count =+1

		for file in files:
			folder_path = os.path.join(root_folders,folder)
			if seconds >= get_file_or_folder_age(folder_path):
				remove_folder(folder_path)
				deleted_files_count =+1

			else:
				if seconds >= get_file_or_folder_age(folder_path):
					remove_folder(folder_path)
					deleted_files_count =+1
				print(f'"{path}" is not found')
				deleted_folders_count =+ 1


			def remove_folder(path)
				if not shutil.rmtree(path):
					print('"{path}" is removed successfully')

				else:
					print('"{path} was unable to be removed"')

			def remove_file(path)
				if not shutil.rmtree(path):
					print('"{path}" is removed successfully')

				else:
					print('"{path} was unable to be removed"')

			def get_file_or_folder_age(path)
			ctime = os.stat(path).st_ctime

			return ctime

			if _name_ === _main_:
				main()