#!/bin/python3

import imdb, osm
import os

rootfolder ="C:\\Users\\Philip\\Documents\\Programming\\Subtitle-Fetcher\\Subtitles"

def find():
    imdbx = imdb.imdb_api()
    subfind = osm.subtitleFinder()
    result = imdbx.search(input("Name of show:")) #
    if len(result) > 1: #TV show
        episode_list = {
            #[id,series#,episode#]
        }
        episode_ids = []
        for episode in result[1]:
            episode_list[int(episode.imdb_id[2:])] = [episode.season,episode.episode]
            episode_ids.append(episode.imdb_id[2:])
        sublinks = {}
        chunk_size = 25
        episode_ids_chunk = [episode_ids[i:i + chunk_size] for i in range(0, len(episode_ids), chunk_size)]
        print("Fetching download links for episodes (in blocks of {0})".format(chunk_size))
        for x in episode_ids_chunk:
            sublinks.update(subfind.get_sub_links(x))
        print(sublinks)

        folder = rootfolder+"/"+result[0].title+"-"+result[0].imdb_id
        try:
            os.mkdir(folder)
        except FileExistsError:
            print("Folder already present")
        Down = osm.Downloader()
        for key in sublinks:
            filepath = folder+"/"+result[0].title+" - "+str(episode_list[int(key)][0])+"x"+str(episode_list[int(key)][1])+".srt"
            if not os.path.exists(filepath):
                print("Saving to:",  filepath)
                Down.download_gz(sublinks[key], filepath)
            else:
                print("Skipping ",filepath)


find()