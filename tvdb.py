import tvdbsimple as tvdb
import textwrap

def setup():
    auth_file = open("auth.txt")
    auth = auth_file.readlines()
    auth_file.close()
    auth = [x.rstrip() for x in auth]
    print(auth)
    tvdb.KEYS.API_KEY = auth[1]


def prettyprint_series(series,wrap):
    print(series["id"])
    print("\t", series["seriesName"], ",", series["firstAired"], ",", series["network"], "\tStatus:", series["status"])
    try:
        print(wrap.fill(series["overview"]))
    except AttributeError:
        pass


def getShow():
    search = tvdb.Search()
    response = search.series(input("Series: "))
    show_id = 0
    wrap2 = textwrap.TextWrapper(initial_indent="\t\t", subsequent_indent="\t\t")
    if len(response) > 1:
        print("Multiple responses, please pick one")
        for index, val in enumerate(response):
            print("[{0}]".format(str(index+1)), end=" ")
            prettyprint_series(val, wrap2)

        show_id = response[int(input("Number:"))-1]["id"]
    else:
        prettyprint_series(response[0], wrap2)
        if input("Is this correct? (Y/N)").lower() == "y":
            show_id = response[0]["id"]

    return show_id



#setup()
#getShow()

