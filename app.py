import streamlit as st
from pytubefix import YouTube
from pytubefix.cli import on_progress
st.title(":red[▶️] Download Youtube video for free")
url = st.text_input("Enter the url of the YouTube video", placeholder = "Paste the url")

if url:
    video_type = st.radio("Select The Type", ["only music", "only video", "music + video"], horizontal = True)
    yt = YouTube(url, on_progress_callback = on_progress)
    st.divider()
    title = yt.title
    thumnail = yt.thumbnail_url

    st.header(f":link: {title}")
    st.image(thumnail)
    st.divider()
    if yt:
        quality = st.radio("select the quality", ["low", "high"], horizontal = True) 
        if video_type == 'only music':
            if quality == 'low':
                audio = yt.streams.filter(adaptive = True, only_audio = True).order_by("abr").first()
            else:
                audio = yt.streams.filter(adaptive = True, only_audio = True).order_by("abr").desc().first()
            st.divider()
            if st.button("Download"):
                try:
                    with st.spinner(text="Downloading.....", show_time=True):
                        audio.download(filename = f"{title}_audio.mp4")
                        st.success(f"Audio track ---- {title}_audio.mp4 --- downloaded successfully")
                except Exception as e:
                    st.error(e)

        elif video_type == 'only video':
            if quality == 'low':
                video = yt.streams.filter(adaptive = True, only_video = True).order_by("resolution").first()
            else:
                video = yt.streams.filter(adaptive = True, only_video = True).order_by("resolution").desc().first()
            st.divider()
            if st.button("Download"):
                try:
                    with st.spinner(text="Downloading.....", show_time=True):
                        video.download(filename = f"{title}_video.mp4")
                        st.success(f"Video file ---- {title}_video.mp4 --- downloaded successfully")
                except Exception as e:
                    st.error(e)
        else:
            if quality == 'low':
                full_video = yt.streams.filter(progressive = True).order_by("resolution").first()
            else:
                full_video = yt.streams.filter(progressive = True).order_by("resolution").desc().first()
            st.divider()
            if st.button("Download"):
                try:
                    with st.spinner(text="Downloading.....", show_time=True):
                        full_video.download(filename = f"{title}_video.mp4")
                        st.success(f"Audio + Video ---- {title}_video.mp4 --- downloaded successfully")
                except Exception as e:
                    st.error(e)
