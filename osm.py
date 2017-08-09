from pythonopensubtitles.opensubtitles import OpenSubtitles
from io import BytesIO
import urllib3
import gzip
multithreading = True
if multithreading:
    # Multithreaded downloads
    import threading
    import time

class subtitleFinder :

    def __init__(self,username="",password="", token=""):
        self.subs = OpenSubtitles()
        if token:
            self.subs.token = token  # Set token to that provided -- untested
        else:
            self.subs.login(username, password)

    #  result = [{'MatchedBy': 'imdbid', 'IDSubMovieFile': '0', 'MovieHash': '0', 'MovieByteSize': '0', 'MovieTimeMS': '0', 'IDSubtitleFile': '1952931532', 'SubFileName': 'Person.of.Interest.S01E01.HDTV.en.srt', 'SubActualCD': '1', 'SubSize': '51140', 'SubHash': '1e591e0dcfa8197e70d05ab3a68c958d', 'SubLastTS': '00:43:38', 'SubTSGroup': '2', 'IDSubtitle': '4242217', 'UserID': '419677', 'SubLanguageID': 'eng', 'SubFormat': 'srt', 'SubSumCD': '1', 'SubAuthorComment': '', 'SubAddDate': '2011-09-23 15:40:55', 'SubBad': '0', 'SubRating': '0.0', 'SubDownloadsCnt': '166380', 'MovieReleaseName': 'S01E01.HDTV.XviD-ASAP / 720p-IMMERSE', 'MovieFPS': '23.976', 'IDMovie': '83999', 'IDMovieImdb': '1941917', 'MovieName': '"Person of Interest" Pilot', 'MovieNameEng': '', 'MovieYear': '2011', 'MovieImdbRating': '8.5', 'SubFeatured': '0', 'UserNickName': 'gutoresquin', 'SubTranslator': '', 'ISO639': 'en', 'LanguageName': 'English', 'SubComments': '0', 'SubHearingImpaired': '0', 'UserRank': 'administrator', 'SeriesSeason': '1', 'SeriesEpisode': '1', 'MovieKind': 'episode', 'SubHD': '1', 'SeriesIMDBParent': '1839578', 'SubEncoding': 'UTF-8', 'SubAutoTranslation': '0', 'SubForeignPartsOnly': '0', 'SubFromTrusted': '1', 'QueryCached': 1, 'SubTSGroupHash': '17b1cfb76c2c9188e3772b16eb3b18be', 'SubDownloadLink': 'http://dl.opensubtitles.org/en/download/src-api/vrf-19b40c51/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/filead/1952931532.gz', 'ZipDownloadLink': 'http://dl.opensubtitles.org/en/download/src-api/vrf-f51c0baf/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/subad/4242217', 'SubtitlesLink': 'http://www.opensubtitles.org/en/subtitles/4242217/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/person-of-interest-pilot-en', 'QueryNumber': '0', 'QueryParameters': {'imdbid': '1941917', 'sublanguageid': 'eng'}, 'Score': 34.6638}, {'MatchedBy': 'imdbid', 'IDSubMovieFile': '0', 'MovieHash': '0', 'MovieByteSize': '0', 'MovieTimeMS': '0', 'IDSubtitleFile': '1953205010', 'SubFileName': 'person.of.interest.s01e01.dvdrip.xvid-reward.srt', 'SubActualCD': '1', 'SubSize': '43805', 'SubHash': '12ba13bf716e293c52b3fa174b3c8f1b', 'SubLastTS': '00:42:27', 'SubTSGroup': '8', 'IDSubtitle': '4657669', 'UserID': '0', 'SubLanguageID': 'eng', 'SubFormat': 'srt', 'SubSumCD': '1', 'SubAuthorComment': '', 'SubAddDate': '2012-09-09 11:22:04', 'SubBad': '0', 'SubRating': '0.0', 'SubDownloadsCnt': '10630', 'MovieReleaseName': ' person.of.interest.s01e01.dvdrip.xvid-reward', 'MovieFPS': '23.976', 'IDMovie': '83999', 'IDMovieImdb': '1941917', 'MovieName': '"Person of Interest" Pilot', 'MovieNameEng': '', 'MovieYear': '2011', 'MovieImdbRating': '8.5', 'SubFeatured': '0', 'UserNickName': '', 'SubTranslator': '', 'ISO639': 'en', 'LanguageName': 'English', 'SubComments': '0', 'SubHearingImpaired': '0', 'UserRank': '', 'SeriesSeason': '1', 'SeriesEpisode': '1', 'MovieKind': 'episode', 'SubHD': '0', 'SeriesIMDBParent': '1839578', 'SubEncoding': 'ASCII', 'SubAutoTranslation': '0', 'SubForeignPartsOnly': '0', 'SubFromTrusted': '0', 'QueryCached': 1, 'SubTSGroupHash': '80ff21163490f8d5e7d2817a6db92ceb', 'SubDownloadLink': 'http://dl.opensubtitles.org/en/download/src-api/vrf-197d0c43/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/filead/1953205010.gz', 'ZipDownloadLink': 'http://dl.opensubtitles.org/en/download/src-api/vrf-f5650bc4/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/subad/4657669', 'SubtitlesLink': 'http://www.opensubtitles.org/en/subtitles/4657669/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/person-of-interest-pilot-en', 'QueryNumber': '0', 'QueryParameters': {'imdbid': '1941917', 'sublanguageid': 'eng'}, 'Score': 10.1063}, {'MatchedBy': 'imdbid', 'IDSubMovieFile': '0', 'MovieHash': '0', 'MovieByteSize': '0', 'MovieTimeMS': '0', 'IDSubtitleFile': '1953205011', 'SubFileName': 'person.of.interest.s01e01.extended.pilot.dvdrip.xvid-reward.srt', 'SubActualCD': '1', 'SubSize': '56390', 'SubHash': '478a88c9b3e48f1b1683ec70a86d060f', 'SubLastTS': '00:54:05', 'SubTSGroup': '1', 'IDSubtitle': '4657670', 'UserID': '0', 'SubLanguageID': 'eng', 'SubFormat': 'srt', 'SubSumCD': '1', 'SubAuthorComment': '', 'SubAddDate': '2012-09-09 11:22:04', 'SubBad': '0', 'SubRating': '0.0', 'SubDownloadsCnt': '23690', 'MovieReleaseName': ' person.of.interest.s01e01.extended.pilot.dvdrip.xvid-reward', 'MovieFPS': '23.976', 'IDMovie': '83999', 'IDMovieImdb': '1941917', 'MovieName': '"Person of Interest" Pilot', 'MovieNameEng': '', 'MovieYear': '2011', 'MovieImdbRating': '8.5', 'SubFeatured': '0', 'UserNickName': '', 'SubTranslator': '', 'ISO639': 'en', 'LanguageName': 'English', 'SubComments': '0', 'SubHearingImpaired': '0', 'UserRank': '', 'SeriesSeason': '1', 'SeriesEpisode': '1', 'MovieKind': 'episode', 'SubHD': '0', 'SeriesIMDBParent': '1839578', 'SubEncoding': 'ASCII', 'SubAutoTranslation': '0', 'SubForeignPartsOnly': '0', 'SubFromTrusted': '0', 'QueryCached': 1, 'SubTSGroupHash': 'd322313b0ee4ef22a36e7020b5e7ec95', 'SubDownloadLink': 'http://dl.opensubtitles.org/en/download/src-api/vrf-197e0c44/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/filead/1953205011.gz', 'ZipDownloadLink': 'http://dl.opensubtitles.org/en/download/src-api/vrf-f55e0bbc/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/subad/4657670', 'SubtitlesLink': 'http://www.opensubtitles.org/en/subtitles/4657670/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/person-of-interest-pilot-en', 'QueryNumber': '0', 'QueryParameters': {'imdbid': '1941917', 'sublanguageid': 'eng'}, 'Score': 10.2369}, {'MatchedBy': 'imdbid', 'IDSubMovieFile': '0', 'MovieHash': '0', 'MovieByteSize': '0', 'MovieTimeMS': '0', 'IDSubtitleFile': '1953652407', 'SubFileName': 'Person of Interest  Ep 1 Pilot.srt', 'SubActualCD': '1', 'SubSize': '54011', 'SubHash': '34831fe210538fd18e8d0b1dd7b81ade', 'SubLastTS': '00:43:38', 'SubTSGroup': '2', 'IDSubtitle': '5110515', 'UserID': '0', 'SubLanguageID': 'eng', 'SubFormat': 'srt', 'SubSumCD': '1', 'SubAuthorComment': '', 'SubAddDate': '2013-07-29 13:23:14', 'SubBad': '0', 'SubRating': '0.0', 'SubDownloadsCnt': '9827', 'MovieReleaseName': ' Person of Interest  Ep 1 Pilot', 'MovieFPS': '0.000', 'IDMovie': '83999', 'IDMovieImdb': '1941917', 'MovieName': '"Person of Interest" Pilot', 'MovieNameEng': '', 'MovieYear': '2011', 'MovieImdbRating': '8.5', 'SubFeatured': '0', 'UserNickName': '', 'SubTranslator': '', 'ISO639': 'en', 'LanguageName': 'English', 'SubComments': '0', 'SubHearingImpaired': '0', 'UserRank': '', 'SeriesSeason': '1', 'SeriesEpisode': '1', 'MovieKind': 'episode', 'SubHD': '0', 'SeriesIMDBParent': '1839578', 'SubEncoding': 'UTF-8', 'SubAutoTranslation': '0', 'SubForeignPartsOnly': '0', 'SubFromTrusted': '0', 'QueryCached': 1, 'SubTSGroupHash': '17b1cfb76c2c9188e3772b16eb3b18be', 'SubDownloadLink': 'http://dl.opensubtitles.org/en/download/src-api/vrf-19b30c53/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/filead/1953652407.gz', 'ZipDownloadLink': 'http://dl.opensubtitles.org/en/download/src-api/vrf-f50d0bab/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/subad/5110515', 'SubtitlesLink': 'http://www.opensubtitles.org/en/subtitles/5110515/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/person-of-interest-pilot-en', 'QueryNumber': '0', 'QueryParameters': {'imdbid': '1941917', 'sublanguageid': 'eng'}, 'Score': 10.09827}, {'MatchedBy': 'imdbid', 'IDSubMovieFile': '0', 'MovieHash': '0', 'MovieByteSize': '0', 'MovieTimeMS': '0', 'IDSubtitleFile': '1953655535', 'SubFileName': 'Person of Interest 1x01 - Pilot.srt', 'SubActualCD': '1', 'SubSize': '59830', 'SubHash': '29281fa9d767fe24abd56bf5289995a9', 'SubLastTS': '00:55:44', 'SubTSGroup': '1', 'IDSubtitle': '5113606', 'UserID': '1683613', 'SubLanguageID': 'eng', 'SubFormat': 'srt', 'SubSumCD': '1', 'SubAuthorComment': '', 'SubAddDate': '2013-07-31 13:05:24', 'SubBad': '0', 'SubRating': '0.0', 'SubDownloadsCnt': '21434', 'MovieReleaseName': 'Person of Interest 1x01 - Pilot', 'MovieFPS': '25.000', 'IDMovie': '83999', 'IDMovieImdb': '1941917', 'MovieName': '"Person of Interest" Pilot', 'MovieNameEng': '', 'MovieYear': '2011', 'MovieImdbRating': '8.5', 'SubFeatured': '0', 'UserNickName': 'james66', 'SubTranslator': '', 'ISO639': 'en', 'LanguageName': 'English', 'SubComments': '0', 'SubHearingImpaired': '1', 'UserRank': 'sub leecher', 'SeriesSeason': '1', 'SeriesEpisode': '1', 'MovieKind': 'episode', 'SubHD': '0', 'SeriesIMDBParent': '1839578', 'SubEncoding': 'ASCII', 'SubAutoTranslation': '0', 'SubForeignPartsOnly': '0', 'SubFromTrusted': '0', 'QueryCached': 1, 'SubTSGroupHash': 'd322313b0ee4ef22a36e7020b5e7ec95', 'SubDownloadLink': 'http://dl.opensubtitles.org/en/download/src-api/vrf-19c60c58/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/filead/1953655535.gz', 'ZipDownloadLink': 'http://dl.opensubtitles.org/en/download/src-api/vrf-f51b0baf/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/subad/5113606', 'SubtitlesLink': 'http://www.opensubtitles.org/en/subtitles/5113606/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/person-of-interest-pilot-en', 'QueryNumber': '0', 'QueryParameters': {'imdbid': '1941917', 'sublanguageid': 'eng'}, 'Score': 11.21434}, {'MatchedBy': 'imdbid', 'IDSubMovieFile': '0', 'MovieHash': '0', 'MovieByteSize': '0', 'MovieTimeMS': '0', 'IDSubtitleFile': '1954390918', 'SubFileName': 'Person of Interest - 01x01 - Pilot.Web-DL.English.C.updated.Addic7ed.com.srt', 'SubActualCD': '1', 'SubSize': '47522', 'SubHash': '8ad5288e042ffdbdfdf7b7daf514b7b7', 'SubLastTS': '00:43:00', 'SubTSGroup': '8', 'IDSubtitle': '5812638', 'UserID': '0', 'SubLanguageID': 'eng', 'SubFormat': 'srt', 'SubSumCD': '1', 'SubAuthorComment': '', 'SubAddDate': '2014-09-05 00:10:54', 'SubBad': '0', 'SubRating': '0.0', 'SubDownloadsCnt': '5324', 'MovieReleaseName': ' Person of Interest - 01x01 - Pilot.Web-DL.English.C.updated.Addic7ed.com', 'MovieFPS': '0.000', 'IDMovie': '83999', 'IDMovieImdb': '1941917', 'MovieName': '"Person of Interest" Pilot', 'MovieNameEng': '', 'MovieYear': '2011', 'MovieImdbRating': '8.5', 'SubFeatured': '0', 'UserNickName': '', 'SubTranslator': '', 'ISO639': 'en', 'LanguageName': 'English', 'SubComments': '0', 'SubHearingImpaired': '0', 'UserRank': '', 'SeriesSeason': '1', 'SeriesEpisode': '1', 'MovieKind': 'episode', 'SubHD': '0', 'SeriesIMDBParent': '1839578', 'SubEncoding': 'ASCII', 'SubAutoTranslation': '0', 'SubForeignPartsOnly': '0', 'SubFromTrusted': '0', 'QueryCached': 1, 'SubTSGroupHash': '80ff21163490f8d5e7d2817a6db92ceb', 'SubDownloadLink': 'http://dl.opensubtitles.org/en/download/src-api/vrf-19c60c5a/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/filead/1954390918.gz', 'ZipDownloadLink': 'http://dl.opensubtitles.org/en/download/src-api/vrf-f5490bba/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/subad/5812638', 'SubtitlesLink': 'http://www.opensubtitles.org/en/subtitles/5812638/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/person-of-interest-pilot-en', 'QueryNumber': '0', 'QueryParameters': {'imdbid': '1941917', 'sublanguageid': 'eng'}, 'Score': 10.05324}, {'MatchedBy': 'imdbid', 'IDSubMovieFile': '0', 'MovieHash': '0', 'MovieByteSize': '0', 'MovieTimeMS': '0', 'IDSubtitleFile': '1955349491', 'SubFileName': 'Person.of.Interest.S01E01.720p.HDTV.ReEnc-Max.srt', 'SubActualCD': '1', 'SubSize': '46822', 'SubHash': '72ac04035e444e22927b2020f930b9fc', 'SubLastTS': '00:42:32', 'SubTSGroup': '2', 'IDSubtitle': '6769377', 'UserID': '4332442', 'SubLanguageID': 'eng', 'SubFormat': 'srt', 'SubSumCD': '1', 'SubAuthorComment': '', 'SubAddDate': '2016-10-20 15:17:38', 'SubBad': '0', 'SubRating': '0.0', 'SubDownloadsCnt': '1471', 'MovieReleaseName': ' Person.of.Interest.S01E01.720p.HDTV.ReEnc-Max', 'MovieFPS': '23.976', 'IDMovie': '83999', 'IDMovieImdb': '1941917', 'MovieName': '"Person of Interest" Pilot', 'MovieNameEng': '', 'MovieYear': '2011', 'MovieImdbRating': '8.5', 'SubFeatured': '0', 'UserNickName': 'red1jhon', 'SubTranslator': '', 'ISO639': 'en', 'LanguageName': 'English', 'SubComments': '0', 'SubHearingImpaired': '0', 'UserRank': 'bronze member', 'SeriesSeason': '1', 'SeriesEpisode': '1', 'MovieKind': 'episode', 'SubHD': '1', 'SeriesIMDBParent': '1839578', 'SubEncoding': 'ASCII', 'SubAutoTranslation': '0', 'SubForeignPartsOnly': '0', 'SubFromTrusted': '0', 'QueryCached': 1, 'SubTSGroupHash': '17b1cfb76c2c9188e3772b16eb3b18be', 'SubDownloadLink': 'http://dl.opensubtitles.org/en/download/src-api/vrf-19d20c5b/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/filead/1955349491.gz', 'ZipDownloadLink': 'http://dl.opensubtitles.org/en/download/src-api/vrf-f57d0bc6/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/subad/6769377', 'SubtitlesLink': 'http://www.opensubtitles.org/en/subtitles/6769377/sid-wOog0I4sWDjuitBOr-UG5SbNRZ8/person-of-interest-pilot-en', 'QueryNumber': '0', 'QueryParameters': {'imdbid': '1941917', 'sublanguageid': 'eng'}, 'Score': 16.01471}]

    def _search(self,imdb_id, language="eng"):
        return self.subs.search_subtitles([{"sublanguageid": language, "imdbid": imdb_id}])

    def _search_multiple(self,imdb_ids, language="eng"):
        request = []
        for imdb_id in imdb_ids:
            request.append({"sublanguageid": language, "imdbid": imdb_id})
        return self.subs.search_subtitles(request)

    def get_sub_link(self, imdb_id, language="eng"):
        result = self._search(imdb_id, language)
        sorted1 = sortby(result,"SubDownloadsCnt")
        return sorted1[0]["SubDownloadLink"]

    def get_sub_links(self,imdb_ids, language="eng"):
        results = self._search_multiple(imdb_ids, language)
        separated = self._separate_episodes(imdb_ids, results)
        for key in separated:
            sorted1 = sortby(separated[key],"SubDownloadsCnt")
            #[print(x["SubFileName"],x["SubDownloadsCnt"]) for x in sorted1]
            #print(sorted1[0]["SubFileName"],sorted1[0]["SubDownloadLink"])
            separated[key] = sorted1[0]["SubDownloadLink"]
        return separated


    def _separate_episodes(self,imdb_ids,array):
        separated = {}
        for sub in array:
            try:
                separated[sub["IDMovieImdb"]].append(sub)
            except KeyError:
                separated[sub["IDMovieImdb"]] = [sub]
        return separated

class Downloader:
    def __init__(self):
        self.http = urllib3.PoolManager()
        self.threads = []


    def download_gz(self,url,filepath,finishcmd=None):
        data = BytesIO()
        request = self.http.request("GET",url)
        data.write(request.data)
        #if not filename:
        #    filename = str(request.info()["Content-Disposition"]).strip('"')
        #    filename = filename[((filename.find("filename="))+10):-3]
        #print(filename)
        data.seek(0)
        if request.status != 200:
            raise Exception("404 on file, downlaod limit possibly reached.")
        unzip = gzip.GzipFile(fileobj=data)
        with open(filepath,"wb") as outfile:
            outfile.write(unzip.read())
        if finishcmd:
            finishcmd()

    def download_multiple(self,links,threads):

        def thread_helper(url,filepath,finishcmd):
            print("Starting download")
            self.download_gz(url,filepath,finishcmd=finishcmd)

        def thread_finish():
            print("Finished download")

        assert type(links) == list
        for index, link in enumerate(links):
            thread = threading.Thread(target=thread_helper, args=(link[0], link[1], thread_finish))
            self.threads.append(thread)
            thread.run()
            if (index+1)%threads == 0:
                print("Waiting")
                while len(self.threads) >= threads:
                    self.threads = [t for t in self.threads if t.isAlive()]
                    time.sleep(0.2)










def sortby(array,attr):
    new_array = []
    new_array.append(array[0])
    array.pop(0)
    for index, sub in enumerate(array):
        x = 0
        while x < len(new_array) and int(sub[attr]) < int(new_array[x][attr]):
            x += 1
        else:
            new_array.insert(x,sub)
    return new_array


# downloader = Downloader()
# downloader.download_multiple([['http://dl.opensubtitles.org/en/download/src-api/vrf-19b20c58/sid-fCUvRAveBXYAxxEIska,ZiWKKUb/filead/1954134875.gz',"C:\\Users\\Philip\\Documents\\Programming\\Subtitle-Fetcher\\Subtitles/Rick and Morty-tt2861424/Rick and Morty - 1x1.srt"],
# ['http://dl.opensubtitles.org/en/download/src-api/vrf-19bb0c57/sid-fCUvRAveBXYAxxEIska,ZiWKKUb/filead/1954209970.gz',"C:\\Users\\Philip\\Documents\\Programming\\Subtitle-Fetcher\\Subtitles/Rick and Morty-tt2861424/Rick and Morty - 1x2.srt"]
# ],2)
# #print(downloader.get_sub_link("1941917"))
#print(downloader.get_sub_links([1941917,2007219]))

#down = Downloader()
#down.download_gz("https://www.opensubtitles.org/en/download/src-api/vrf-19b40c51/sid-3Se2mF8OPUWXWGbk6reGVJr6pP8/filead/1952931532.gz")
