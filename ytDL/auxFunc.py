from numpy import isin
import pandas as pd

def checkVideoInPlaylist(playlist, videoUrlList)#check if videoUrlList is in playlist, return what is not in the intersection
    videoAlreadyDOne = playlist.video_urls
    videoToDL = videoUrlList
    
    return list(set(videoAlreadyDOne) ^ set(videoToDL))

def updateSongDL(df):
    extEnd = '.csv'
    xlSongCheckPath = 'D:\Project\TwitchBot\ytDL\\'
    xlSongCheckFile = 'alreadyDLSong'
    xlSongCheckMain = xlSongCheckPath + xlSongCheckFile +extEnd