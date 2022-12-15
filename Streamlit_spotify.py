from streamlit_player import st_player
import os
import streamlit as st
import streamlit as st
from audio_recorder_streamlit import audio_recorder
import streamlit.components.v1 as components
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import time
st.set_page_config(page_title="Karaoke", page_icon="🎤", layout="wide", menu_items=None)
spotify = pd.read_csv("C:/Users/luisa/Downloads/output.csv")

final_df = pd.read_csv("C:/Users/luisa/Downloads/spotify_top50.csv")
# Embed a music from SoundCloud
# st_player("https://soundcloud.com/imaginedragons/demons")


#Top geral
spotify_genre = spotify.groupby(['track_genre']).agg({'popularity': 'mean','track_id' : 'count'}).reset_index()
df_music_popularity = spotify_genre.sort_values(by=('popularity'), ascending=False).head(5)

spotify_genre_instrumentalness = spotify.groupby(['track_genre']).agg({'instrumentalness': 'mean','track_id' : 'count'}).reset_index()
df_music_i= spotify_genre_instrumentalness.sort_values(by=('instrumentalness'), ascending=False).head(5)

spotify_genre_dance = spotify.groupby(['track_genre']).agg({'danceability': 'mean','track_id' : 'count'}).reset_index()
df_music_dance = spotify_genre_dance.sort_values(by=('danceability'), ascending=False).head(5)

spotify_genre_energy = spotify.groupby(['track_genre']).agg({'energy': 'mean','track_id' : 'count'}).reset_index()
df_music_energy = spotify_genre_energy.sort_values(by=('energy'), ascending=False).tail(5)


#Top 50
order = final_df.groupby(['track_genre']).agg({'danceability': 'mean','track_id' : 'count'}).reset_index()
top50_order_dance = order.sort_values(by=('danceability'), ascending=False)
top50_df_order_dance= top50_order_dance.head(5)
top50_spotify_genre = final_df.groupby(['track_genre']).agg({'popularity': 'mean','track_id' : 'count'}).reset_index()
top50_s_g = top50_spotify_genre.sort_values(by=('popularity'), ascending=False)
top50_df_music_popularity= top50_s_g.head(5)
top50_spotify_genre_instrumentalness = final_df.groupby(['track_genre']).agg({'instrumentalness': 'mean','track_id' : 'count'}).reset_index()
top50_s_g_i = top50_spotify_genre_instrumentalness.sort_values(by=('instrumentalness'), ascending=False)
top50_df_music_i= top50_s_g_i.head(5)
top50_spotify_genre_energy = final_df.groupby(['track_genre']).agg({'energy': 'mean','track_id' : 'count'}).reset_index()
top50_s_g_e = top50_spotify_genre_energy.sort_values(by=('energy'), ascending=False)
top50_df_music_energy= top50_s_g_e.tail(5)

# Lyrics

df_lyrics = pd.read_pickle("C:/Users/luisa/OneDrive/Documentos/GitHub/Project4WebScrapStats/spotify_with_lyrics.pkl")



                 
st.markdown("<h1 style='text-align: center; color: black;'>Spotify</h1>", unsafe_allow_html=True)


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

    col1, col2 = st.columns(2)
    st.subheader('*Danceability*')
    with col1:
            with st.expander("Top"):
                    st.write("""
        This information is related to all musics in Spotify""")
            
            fig1, ax1 = plt.subplots(figsize=(15,6))
            
            # sns.barplot(x = 'track_genre', y = 'popularity', data = df_music_popularity,color= "#020202").set(title = 'Popularity')
            sns.pointplot(data=df_music_popularity, x="track_genre", y="popularity", hue="track_id", color="lightgreen")
            # ax.set_title('Amount orders not yet paid x customer')
            ax1.set_xlabel("Genre")
            ax1.set_ylabel("Popularity")
            st.pyplot(fig1)
            
            colors = sns.color_palette('pastel')[0:5]

# #create pie chart
# plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
# plt.show()
            
    with col2:
            with st.expander("Top50"):
                    st.write("""
        This information is related to the top 50 songs in Spotify.
    """)

            fig1t50, ax1t50 = plt.subplots(figsize=(15,6))
            # sns.barplot(x = 'track_genre', y = 'popularity', data = top50_df_music_popularity ,color= "#1CBA54",)
            sns.pointplot(data=top50_df_music_popularity, x="track_genre", y="popularity", hue="track_id", color="lightgreen")
            ax1t50.set_xlabel("Genre")
            ax1t50.set_ylabel("Popularity")
            st.pyplot(fig1t50)


      
    col3, col4 = st.columns(2)
    st.subheader('*Energy*')

    with col3:

            fig3, ax3 = plt.subplots(figsize=(15,6))
            # sns.barplot(x = 'track_genre', y = 'danceability', data = df_music_dance,color= "#1CBA54")
            sns.lineplot(data= df_music_dance, x="track_genre", y="danceability",color= "#1CBA54")
            ax3.set_xlabel("Genre")
            ax3.set_ylabel("Danceability")
            st.pyplot(fig3)
    with col4:

            figa, axa = plt.subplots(figsize=(15,6))
            sns.color_palette("tab10")
            # sns.barplot(x = 'track_genre', y = 'danceability', data = top50_df_order_dance, color= "#020202")
            sns.lineplot(data= top50_df_order_dance, x="track_genre", y="danceability",color= "#020202")
            axa.set_xlabel("Genre")
            axa.set_ylabel("Danceability")
            st.pyplot(figa)
        
#     col5, col6 = st.columns(2)
#     st.subheader('*Energy*')
#     with col5:
    
#             fig4, ax4 = plt.subplots(figsize=(15,4))
#             sns.barplot(x = 'track_genre', y = 'instrumentalness', data = df_music_i, color= "#020202")
#             ax4.set_xlabel("Genre")
#             ax4.set_ylabel("Instrumentalness")
#             st.pyplot(fig4)
        
#     with col6:
    
#             fig4_top50, ax4_top50 = plt.subplots(figsize=(15,4))
#             sns.barplot(x = 'track_genre', y = 'instrumentalness', data = top50_df_music_i, color= "#1CBA54")
#             ax4_top50.set_xlabel("Genre")
#             ax4_top50.set_ylabel("Instrumentalness")
#             st.pyplot(fig4_top50)
# else: 
    col7, col8 = st.columns(2)
        
    
    with col7:

    
            fig41, ax41 = plt.subplots(figsize=(15,6))
            sns.barplot(x = 'track_genre', y = 'energy', data = df_music_energy,color= "#1CBA54")
            ax41.set_xlabel("Genre")
            ax41.set_ylabel("Energy")
            plt.xticks(rotation=55, ha='right', rotation_mode='anchor')
            st.pyplot(fig41)
        
    with col8:
    
            fig4top50, ax4top50 = plt.subplots(figsize=(15,6))
            sns.barplot(x = 'track_genre', y = 'energy', data = top50_df_music_energy, color= "#020202")
            ax4top50.set_xlabel("Genre")
            ax4top50.set_ylabel("Energy")
            plt.xticks(rotation=55, ha='right', rotation_mode='anchor')
            st.pyplot(fig4top50)
            # st.text(top50_df_music_energy['energy'].std())
                    
if selected == "Musics":        
    with st.spinner('Wait for it...'):
        time.sleep(5)
        st.success('Done!')

        
    # Embed a music from SoundCloud
    band = st.text_input('Type a band and press Enter')
    st_player(f"https://soundcloud.com/{band}")
    
        # st_player("https://soundcloud.com/imaginedragons/demons")
    
     
    audio_bytes = audio_recorder()
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
        
    df_lyrics['full_name_music'] = df_lyrics['track_name']+', '+df_lyrics['artists']
    music = st.selectbox('Choose a music:', df_lyrics['full_name_music'].unique())
    
    print(music)
    L = music.split(', ')
    df_lyrics.loc[(df_lyrics['track_name']==L[0])& (df_lyrics['artists']==L[1])].lyrics.iloc[0]
    
