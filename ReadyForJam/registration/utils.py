def handle_uploaded_file(f, name):
    path = 'static/img/' + name
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return path
