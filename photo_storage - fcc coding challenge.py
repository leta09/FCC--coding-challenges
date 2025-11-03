
def number_of_photos(photo_size_mb, drive_size_gb):

    return int(drive_size_gb*1000/ photo_size_mb)


print(number_of_photos(4, 256))
print(number_of_photos(3.5, 750))

