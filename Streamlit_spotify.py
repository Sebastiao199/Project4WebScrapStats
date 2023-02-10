from streamlit_player import st_player
import os
from audio_recorder_streamlit import audio_recorder
import streamlit.components.v1 as components
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import time
from PIL import Image
import re
import altair as alt

st.set_page_config(page_title="Karaoke", page_icon="🎤", layout="wide", menu_items=None)
spotify = pd.read_csv("MainTables/output.csv")

final_df = pd.read_csv("MainTables/spotify_top50.csv")
# Embed a music from SoundCloud
# st_player("https://soundcloud.com/imaginedragons/demons")


#Top geral

spotify_artist_popula = spotify.groupby(['artists']).agg({'popularity': 'sum','track_id' : 'count'}).reset_index()
spotify_artist_popula = spotify_artist_popula.sort_values(by=('popularity'), ascending=False).head(5)

spotify_genre_energy_toparts = spotify.groupby(['artists']).agg({'popularity': 'sum','energy' : 'mean'}).reset_index()
df_music_energy_toparts = spotify_genre_energy_toparts.sort_values(by=('popularity'), ascending=False).head(5)
df_music_energy_toparts_last = df_music_energy_toparts.sort_values(by=('energy'), ascending=False)

spotify_genre_dance_topartists = spotify.groupby(['artists']).agg({'popularity': 'sum','danceability' : 'mean'}).reset_index()
df_music_dance = spotify_genre_dance_topartists.sort_values(by=('popularity'), ascending=False).head(5)
df_music_dance_D = df_music_dance.sort_values(by=('danceability'), ascending=False)

#Top 50
final_df['artists'] = final_df['artists'].str.replace('Bad Bunny;Bomba Estéreo','Bad Bunny')
final_df['artists'] = final_df['artists'].str.replace('Bad Bunny;Chencho Corleone','Bad Bunny')


top50_spotify_artist_popula  = final_df.groupby(['artists']).agg({'popularity': 'sum','track_id' : 'count'}).reset_index()
top50_spotify_artist_popula  = top50_spotify_artist_popula.sort_values(by=('popularity'), ascending=False).head(5)


top50_spotify_genre_dance_topartists = final_df.groupby(['artists']).agg({'popularity': 'sum','danceability' : 'mean'}).reset_index()
top50_df_music_dance = top50_spotify_genre_dance_topartists.sort_values(by=('popularity'), ascending=False).head(5)
top50_df_music_dance_final = top50_df_music_dance.sort_values(by=('danceability'), ascending=False)


top50_spotify_genre_energy_toparts = final_df.groupby(['artists']).agg({'popularity': 'sum','energy' : 'mean'}).reset_index()
top50_df_music_energy_toparts = top50_spotify_genre_energy_toparts.sort_values(by=('popularity'), ascending=False).head(5)
top50_df_music_energy_toparts_final = top50_df_music_energy_toparts.sort_values(by=('energy'), ascending=False)

# Lyrics

df_1 = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project4WebScrapStats/main/Google_Playstore1.csv')
df_2 = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project4WebScrapStats/main/Google_Playstore2.csv')
df_3 = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project4WebScrapStats/main/Google_Playstore3.csv')
df_4 = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project4WebScrapStats/main/Google_Playstore4.csv')
df_5 = pd.read_csv('hhttps://raw.githubusercontent.com/Sebastiao199/Project4WebScrapStats/main/Google_Playstore5.csv')
df_6 = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project4WebScrapStats/main/Google_Playstore6.csv')
df_7 = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project4WebScrapStats/main/Google_Playstore7.csv')
df_8 = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project4WebScrapStats/main/Google_Playstore8.csv')
df_9 = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project4WebScrapStats/main/Google_Playstore9.csv')
df_10 = pd.read_csv('https://raw.githubusercontent.com/Sebastiao199/Project4WebScrapStats/main/Google_Playstore10.csv')
df_12 = pd.concat([df_1, df_2], axis=0)
df_123 = pd.concat([df_12, df_3], axis=0)
df_1234 = pd.concat([df_123, df_4], axis=0)
df_12345 = pd.concat([df_1234, df_5], axis=0)
df_123456 = pd.concat([df_12345, df_6], axis=0)
df_1234567 = pd.concat([df_123456, df_7], axis=0)
df_12345678 = pd.concat([df_1234567, df_8], axis=0)
df_123456789 = pd.concat([df_12345678, df_9], axis=0)
df_lyrics = pd.concat([df_123456789, df_10], axis=0)


# Images 

image = Image.open("Images/The beatles.jpeg")
image2 = Image.open("Images/likind park.jpeg")
image3=  Image.open("Images/bts.jpeg")
image4=  Image.open("Images/prateed kuhad.jpeg")
image5=  Image.open("Images/elvis.jpeg")

image6 = Image.open("Images/bad bunny.jpeg")
image7 = Image.open("Images/manuel turizo.jpeg")
image8=  Image.open("Images/the neighbourhood.jpeg")
image9=  Image.open("Images/ozuna.jpeg")
image10= Image.open("Images/david guetta.jpeg")
                 
st.markdown("<h1 style='text-align: center; color: black;'>Spotify</h1>", unsafe_allow_html=True)

# Code for Musics part

df_lyrics['full_name_music'] = df_lyrics['track_name']+', '+df_lyrics['artists']


selected = option_menu(None, ["Top's", "Musics"], 
    icons=['bi bi-bar-chart', 'bi bi-music-note-beamed'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#83DB9F"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#83DB9F"},
        "nav-link-selected": {"background-color": "#4ACA77"},
    }
)

if selected == "Top's":

    st.markdown("<h2 style='text-align: left; color: black;'>Tops</h2>", unsafe_allow_html=True)
    st.header('Are danceability and energy related to the popularity of songs?')
    col1, col2 = st.columns(2)

    with col1:
            with st.expander("Top"):
                st.write("""This information is related musics in Spotify two months ago""")
                       
            st.image([image, image2, image3, image4,image5], width=200)

            Artist = st.selectbox(label = 'Artists', options = ['The Beatles', 'Linkin Park', 'BTS', 'Prateek Kuhad', ' Elvis Presley'])        
            st.write('<style>.div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)         
            if Artist == 'The Beatles':
                st.subheader('*Danceability*')
                fig3, ax3 = plt.subplots(figsize=(15,6))
                sns.barplot(data = df_music_dance_D, x="artists", y="danceability", palette = ['black', 'black', 'black', 'tab:green','black'])
                ax3.set_xlabel("Artists")
                ax3.set_ylabel("Danceability")
                st.pyplot(fig3)
                st.subheader('*Energy*')
                fig41, ax41 = plt.subplots(figsize=(15,6))
                sns.barplot(data = df_music_energy_toparts_last,x = 'artists', y = 'energy', palette = ['black', 'black', 'tab:green', 'black','black'])
                ax41.set_xlabel("Artists")
                ax41.set_ylabel("Energy")
                st.pyplot(fig41)
                
            elif Artist == 'Linkin Park':
                st.subheader('*Danceability*')
                fig36, ax36 = plt.subplots(figsize=(15,6))
                sns.barplot(data = df_music_dance_D, x="artists", y="danceability", palette = ['black', 'black', 'tab:green', 'black','black'])
                ax36.set_xlabel("Artists")
                ax36.set_ylabel("Danceability")
                st.pyplot(fig36)
                st.subheader('*Energy*')
                fig415, ax415 = plt.subplots(figsize=(15,6))
                sns.barplot(data = df_music_energy_toparts_last, x = 'artists', y = 'energy', palette = ['tab:green', 'black', 'black', 'black','black'])
                ax415.set_xlabel("Artists")
                ax415.set_ylabel("Energy")
                st.pyplot(fig415)
            elif Artist == 'BTS':
                st.subheader('*Danceability*')
                fig39, ax39 = plt.subplots(figsize=(15,6))
                sns.barplot(data = df_music_dance_D, x="artists", y="danceability", palette = ['tab:green', 'black', 'black', 'black','black'])
                ax39.set_xlabel("Artists")
                ax39.set_ylabel("Danceability")
                st.pyplot(fig39)
                st.subheader('*Energy*')
                fig4156, ax4156 = plt.subplots(figsize=(15,6))
                sns.barplot(data = df_music_energy_toparts_last, x = 'artists', y = 'energy', palette = ['black', 'tab:green', 'black', 'black','black'])
                ax4156.set_xlabel("Artists")
                ax4156.set_ylabel("Energy")
                st.pyplot(fig4156)
            elif Artist == 'Prateek Kuhad':
                st.subheader('*Danceability*')
                fig30, ax30 = plt.subplots(figsize=(15,6))
                sns.barplot(data = df_music_dance_D, x="artists", y="danceability", palette = ['black', 'tab:green', 'black', 'black','black'])
                ax30.set_xlabel("Artists")
                ax30.set_ylabel("Danceability")
                st.pyplot(fig30)
                st.subheader('*Energy*')
                fig41561, ax41561 = plt.subplots(figsize=(15,6))
                sns.barplot(data = df_music_energy_toparts_last, x = 'artists', y = 'energy', palette = ['black', 'black', 'black', 'black','tab:green'])
                ax41561.set_xlabel("Artists")
                ax41561.set_ylabel("Energy")
                st.pyplot(fig41561)
            else: 
                st.subheader('*Danceability*')
                fig34, ax34 = plt.subplots(figsize=(15,6))
                sns.barplot(data = df_music_dance_D, x="artists", y="danceability", palette = ['black', 'black', 'black', 'black','tab:green'])
                ax34.set_xlabel("Artists")
                ax34.set_ylabel("Danceability")
                st.pyplot(fig34)
                st.subheader('*Energy*')
                fig415616, ax415616 = plt.subplots(figsize=(15,6))
                sns.barplot(data = df_music_energy_toparts_last, x = 'artists', y = 'energy', palette = ['black', 'black', 'black', 'tab:green','black'])
                ax415616.set_xlabel("Artists")
                ax415616.set_ylabel("Energy")
                st.pyplot(fig415616)
    with col2:
            with st.expander("Top50"):
                st.write("""This information is related to the top 50 songs in Spotify.""")
            

            st.image([image6, image7, image8, image9,image10], width=195)
             
            Artist50 = st.selectbox(label = 'Artists', options = ['Bad Bunny', 'Manuel Turizo', 'The Neighbourhood', 'Ozuna', ' David Guetta'])        
            st.write('<style>.div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)         
            if Artist50 == 'Bad Bunny':
                st.subheader('*Danceability*')
                fig31, ax31 = plt.subplots(figsize=(15,6))
                sns.barplot(data = top50_df_music_dance_final, x="artists", y="danceability", palette = ['black', 'black', 'tab:green', 'black','black'])
                ax31.set_xlabel("Artists")
                ax31.set_ylabel("Danceability")
                st.pyplot(fig31)
                
                st.subheader('*Energy*')
                fig411, ax411 = plt.subplots(figsize=(15,6))
                sns.barplot(data =top50_df_music_energy_toparts_final ,x = 'artists', y = 'energy', palette = ['black', 'black', 'black', 'tab:green','black'])
                ax411.set_xlabel("Artists")
                ax411.set_ylabel("Energy")
                st.pyplot(fig411)
                
            elif Artist50 == 'Manuel Turizo':
                st.subheader('*Danceability*')
                fig361, ax361 = plt.subplots(figsize=(15,6))
                sns.barplot(data = top50_df_music_dance_final, x="artists", y="danceability", palette = ['black', 'tab:green', 'black', 'black','black'])
                ax361.set_xlabel("Artists")
                ax361.set_ylabel("Danceability")
                st.pyplot(fig361)
                
                st.subheader('*Energy*')
                fig4155, ax4155 = plt.subplots(figsize=(15,6))
                sns.barplot(data = top50_df_music_energy_toparts_final, x = 'artists', y = 'energy', palette = ['black', 'black', 'tab:green', 'black','black'])
                ax4155.set_xlabel("Artists")
                ax4155.set_ylabel("Energy")
                st.pyplot(fig4155)
                
            elif Artist50 == 'The Neighbourhood':
                st.subheader('*Danceability*')
                fig3978, ax3978 = plt.subplots(figsize=(15,6))
                sns.barplot(data = top50_df_music_dance_final, x="artists", y="danceability", palette = ['black', 'black', 'black', 'tab:green','black'])
                ax3978.set_xlabel("Artists")
                ax3978.set_ylabel("Danceability")
                st.pyplot(fig3978)
                
                st.subheader('*Energy*')
                fig415633, ax415633 = plt.subplots(figsize=(15,6))
                sns.barplot(data = top50_df_music_energy_toparts_final, x = 'artists', y = 'energy', palette = ['black', 'tab:green', 'black', 'black','black'])
                ax415633.set_xlabel("Artists")
                ax415633.set_ylabel("Energy")
                st.pyplot(fig415633)
                
            elif Artist50 == 'Ozuna':
                st.subheader('*Danceability*')
                fig3067, ax3067 = plt.subplots(figsize=(15,6))
                sns.barplot(data = top50_df_music_dance_final, x="artists", y="danceability", palette = ['tab:green', 'black', 'black', 'black','black'])
                ax3067.set_xlabel("Artists")
                ax3067.set_ylabel("Danceability")
                st.pyplot(fig3067)
                
                st.subheader('*Energy*')
                fig4159, ax4159 = plt.subplots(figsize=(15,6))
                sns.barplot(data = top50_df_music_energy_toparts_final, x = 'artists', y = 'energy', palette = ['black', 'black', 'black', 'black','tab:green'])
                ax4159.set_xlabel("Artists")
                ax4159.set_ylabel("Energy")
                st.pyplot(fig4159)
            else: 
                st.subheader('*Danceability*')
                fig347, ax347 = plt.subplots(figsize=(15,6))
                sns.barplot(data = top50_df_music_dance_final, x="artists", y="danceability", palette = ['black', 'black', 'black', 'black','tab:green'])
                ax347.set_xlabel("Artists")
                ax347.set_ylabel("Danceability")
                st.pyplot(fig347)
                
                st.subheader('*Energy*')
                fig4150, ax4150 = plt.subplots(figsize=(15,6))
                sns.barplot(data = top50_df_music_energy_toparts_final, x = 'artists', y = 'energy', palette = ['tab:green', 'black', 'black', 'black', 'black'])
                ax4150.set_xlabel("Artists")
                ax4150.set_ylabel("Energy")
                st.pyplot(fig4150)


      
                    
if selected == "Musics":        
    with st.spinner('Wait for it...'):
        time.sleep(1)
        st.success('Done!')

        
    # Embed a music from SoundCloud
    band = st.text_input('Type a band and press Enter')
    st_player(f"https://soundcloud.com/{band}")    
    
    music = st.selectbox('Choose a music:', df_lyrics['full_name_music'].unique())
    
    #print(music)
    L = music.split(', ')
    lyrics = df_lyrics.loc[(df_lyrics['track_name']==L[0])& (df_lyrics['artists']==L[1])].lyrics.iloc[0]
    my_list = re.findall('[A-HJ-Z][^A-HJ-Z]*', lyrics)
    str1 = "\n".join(my_list)
    for i in my_list:
        st.markdown(i)
    # st.markdown(my_list)

    # my_list = re.findall('[a-zA-Z][^A-Z]*', lyrics).str.split('\n')
    # str1 = "\n".join(my_list)
    
    audio_bytes = audio_recorder()
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
        
