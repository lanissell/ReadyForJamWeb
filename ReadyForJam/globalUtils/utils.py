def HandleUploadedFile(f, staticPath, name):
    path = staticPath + name
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return path
