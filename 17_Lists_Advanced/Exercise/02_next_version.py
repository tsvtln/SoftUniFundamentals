def next_version(version):
    version = ''.join(version)
    version = int(version) + 1
    version_list = [str(char) for char in str(version)]
    version = '.'.join(version_list)
    return version


entry_version = input().split('.')
print(next_version(entry_version))
