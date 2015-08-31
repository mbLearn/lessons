import os

def walk(top):
    try:
        names = os.listdir(top)
    except error, err:
        return

    dirs, nondirs = [], []
    for name in names:
        if os.path.isdir(os.path.join(top, name)):
            dirs.append(name)
        else:
            nondirs.append(name)

    yield top, dirs, nondirs

    for name in dirs:
        new_path = os.path.join(top, name)
        for x in walk(new_path):  # recursive call
            yield x

    for name in dirs:
    new_path = os.path.join(top, name)
    yield from walk(new_path)
