
def number_of_files(file_size, file_unit, drive_size_gb):

    if file_unit == "B":
        return int((1000**3) / file_size *drive_size_gb)
    
    if file_unit == "KB":
        return int((1000**2) / file_size *drive_size_gb)
    
    if file_unit == "MB":
        return int((1000) / file_size *drive_size_gb)


print(number_of_files(50000, "B", 1))
print(number_of_files(4096, "B", 1.5))
print(number_of_files(4.5, "MB", 750))
