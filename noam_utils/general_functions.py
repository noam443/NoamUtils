import os


def create_folder(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def get_filename(path, with_extension=True):
    filename = os.path.basename(path)
    if not with_extension:
        return filename.rsplit('.', 1)[0]
    return filename


def get_filename_extension(path):
    extension = path.rsplit('.', 1)[1] if len(path.rsplit('.', 1)) > 1 else ''
    return extension
