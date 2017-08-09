from imdbpie import Imdb
import textwrap

class imdb_api:
    def __init__(self, anonymize=False):
        self.imdb = Imdb(anonymize=anonymize)

    def search(self,title,imdb_id=""):
        if not imdb_id:
            print("Searching")
            results = self.imdb.search_for_title(title)
            chosen = self.search_select(results)
            title_id = results[chosen]["imdb_id"]
        else:
            title_id = imdb_id
        print("Looking up series")
        title = self.imdb.get_title_by_id(title_id)
        if title.type == "tv_series":
            print("Detected TV series, downloading episode list")
            episodes = self.imdb.get_episodes(title_id)
            print(episodes)
            return [title, episodes]
        else:
            return [title]

    def search_select(self,results):
        def get_input(allow_0=True):
            print("Which show do you want? type 0 to see more")
            out = 0
            while out == 0:
                inp = input("> ")
                if inp == "0" and allow_0:
                    return out
                else:
                    try:
                        out = int(inp)
                    except ValueError:
                        print("Not a number")
            return out

        if len(results) > 1:
            chosen = 0
            for index, show in enumerate(results):
                print("[{0}] ({3})\t{1}\t{2}".format(str(index + 1),show["title"],show["year"],show["imdb_id"]))
                if ((index+1) % 10) == 0:
                    chosen = get_input()
                    if chosen != 0:
                        break
            if chosen == 0:
                print("No more")
                chosen = get_input(allow_0=False)
            return chosen - 1



#imdb = imdb_api()
#x = imdb.search("Person of Interest")
#print(x)