from pytube import Playlist
import pandas as pd
import os

doDL = True

if __name__ == "__main__":
    playlistDic = {}
    playlistList = [
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_F2wzyb_WDIgJEdzl6w8F6G'), #Code Geass
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HerBoNty1XAYD4g26xjwnm'), #Naruto
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GZdEx8UjvAQ4l1Fmdofp6D'), #Naruto Shippuden
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GUVTMmFj0abv7NeeeCAycR'), #Bleach
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Fh_XLX8Ly8U6DWepv4iipS'), #Angel Beats
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GYxXvn72A4ovXBxIaZfbSj'), #Black Lagoon
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_FP_OUsjHkF529ljZjQWKdx'), #Ao no Exorcist
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GdAf2FxhLNLRAUzNd679GP'), #Boku no Hero
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EXCwI8yLNCRLLZzUlS-q4j'), #Bungou Stray Dogs
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_E-06egHQ_0Vy4V0G4w0T5N'), #Captain Tsubasa
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EHdT-1jB0_nVumE1nuY49v'), #Mysterieuse Cite Dor
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_F96QkibwX23Rpogx30EkV0'), #City Hunter
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Ef7BZRNL6gy4jA0i9l_P6N'), #Code Lyoko
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_FqgjHAItydbXI-qRj9vUAE'), #Cowboy Bebop
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GKqh8AeISX4b3lL1l8Qk6f'), #Deadman Wonderland
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EfAwYWbk92hKA04Y4zR1o7'), #Death Note
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_FwyAbE964rYzmO_xGwSHz7'), #Detective Conan
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GMfKOR0EdeYwxlag_84BOt'), #Dragon Ball & co
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_H4jxa8ol3wkXaIkjTHa9Bt'), #Koutetsujou no Kabaneri
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_FtalwCzmzqllwfN6mQVhrx'), #Durarara
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EVWDYFgbdxcNHl8qjRYjXo'), #Erased
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_F4eX9Wyn9k3RRTo3OHT2GB'), #Evangelion
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_F-c14oBifnPVXbgrBBndg-'), #Eyeshield 21
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Hb_eYufrtZ4_64eXioHl9C'), #Fate & co
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HPeiXfHKd819hqbt4yfhyX'), #One Punch Man
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GTyaiQFqiF_f7Y3dF_OAdS'), #Full Metal Alchemist
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HohkEJSj2TEzh8l7cvvC0g'), #GTO
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Flfwst2z_QTqCkPjtcVNe1'), #Kimetsu no Yaiba
    ]

    for playList in playlistList:
        playlistDic[playList.title] = playList

    if True:
        paramDic = {}
        paramDic['output_path'] = 'D:\Videos\Anime\\'
        paramDic['extDL'] = '.mp4'

        videoDLDic = {}
        videoDLDic['videoTitle'] = []
        videoDLDic['videoURL'] = []
        videoDLDic['videoView'] = []

    #---------------------------------------- Download video for each playlist and each video ---------------------------------------------------------------
    for playlistName, playlist in playlistDic.items():#Loop through the different youtube playlist
        print("Downloading :", playlistName)
        outputPathAnime = paramDic['output_path'] + playlistName

        if not os.path.exists(outputPathAnime): #If the anime folder does not exist => create one, else pass
            os.mkdir(outputPathAnime)

        for video in playlist.videos:#for each video in the playlist
            videoName = video.title
            videoUrl = video.watch_url
            videoViews = video.views

            videoDLDic['videoTitle'].append(videoName)
            videoDLDic['videoURL'].append(videoUrl)
            videoDLDic['videoView'].append(videoViews)

            st = video.streams.get_highest_resolution()
            if doDL:
                st.download(output_path = outputPathAnime)
            #video.streams.first().download()

    #Create a dictionnary and store DL songs into an Excel
    pd.DataFrame(videoDLDic).to_csv(r'D:\Project\TwitchBot\ytDL\alreadyDLSong.csv', index = False)