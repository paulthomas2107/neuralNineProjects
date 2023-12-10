import shutil


def ignore_specific_files(directory, files):
    return [f for f in files if f == 'miss.txt']


# shutil.copy('source_dir/first.txt', 'source_dir/second.txt')
# shutil.copytree('source_dir', 'destination_dir')
# shutil.copytree('source_dir', 'destination_dir_002', ignore=ignore_specific_files)
# shutil.move('first.txt', 'third.txt')
# shutil.move('third.txt', 'source_dir/third.txt')
# total, used, free = shutil.disk_usage('/')
# print(total, used, free)
# shutil.copystat('hello.txt', 'hello2.txt')
# print(shutil.which('python3'))
# shutil.make_archive('myarchive', 'zip', '.')
# shutil.unpack_archive('myarchive.zip', 'unpack_dir')
print(shutil.get_archive_formats())
print(shutil.get_unpack_formats())