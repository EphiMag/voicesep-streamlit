# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:55:25 2022

@author: magla
"""
import streamlit as st
from pydub import AudioSegment
import os

uploaded_file = st.file_uploader("Importez une musique",type=['wav','mp3'])

if uploaded_file is not None:
    #st.write(uploaded_file.name)
    if uploaded_file.name.endswith('wav'):
        audio = AudioSegment.from_wav(uploaded_file)
        file_type = 'wav'
    elif uploaded_file.name.endswith('mp3'):
        audio = AudioSegment.from_mp3(uploaded_file)
        file_type = 'mp3'
        
    audio.export(uploaded_file.name, format=file_type)
    os.system("demucs -n mdx_extra_q --two-stems=vocals uploaded_file.name")
    st.audio('separated/mdx_extra_q/mix/vocals.wav', format='audio/wav')