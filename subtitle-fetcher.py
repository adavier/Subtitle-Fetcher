import tvdbsimple as tvdb

def setup():
    auth_file = open("auth.txt")
    auth = auth_file.readlines()
    auth_file.close()
    auth = [x.rstrip() for x in auth]
    print(auth)
    tvdb.KEYS.API_KEY = auth[2]
    return tvdb