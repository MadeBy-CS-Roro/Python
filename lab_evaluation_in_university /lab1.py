project_name = input("Enter project name: ")
number_of_files = int(input("Enter the number of files you want to create: "))
file_size = float(input("Enter the size of each file in MB: "))
total_size = number_of_files * file_size
total_gb=total_size / 1024
print("summary")
print("Name:", project_name)
print(f"Total size (MB): {total_size:.2f}")
print(f"Total size (GB): {total_gb:.2f}")
