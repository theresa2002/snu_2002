def upload_file(f):
    with open("Home/static/img/"+f.name,"wb+") as des:
        for i in f.chunks():
            des.write(i)
