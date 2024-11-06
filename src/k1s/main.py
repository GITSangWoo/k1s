import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from k1s.autoscale import checkAll,main,stopApp,startApp,scalein,scaleout,wherelog

st.set_page_config(
    page_title="scale in/out 관리자 메인 페이지 ",
    page_icon="👋",
)

st.write("스케일 인/아웃 관리 페이지👋")

wherelog()
result0,result1,result2 = checkAll()

with st.form(key='my_form'):
    st.write("시간:",result0,"총 도커수:",result1, "CPU 총 사용량:",result2)

    col1, col2, col3 = st.columns(3)
    with col1:
        start_button = st.form_submit_button(label='Auto scale Start')
    with col2:
        stop_button = st.form_submit_button(label='Auto scale Stop')
    with col3:
        rerun_button = st.form_submit_button(label='View Current Dockers')
    if start_button:
        startApp()
        st.write("Auto scale has started.")
    if stop_button:
        stopApp()
        st.write("Auto scale has stopped.")
    if rerun_button:
        st.write("Review Current Dockers")
        #result0,result1,result2 = checkAll()
        st.rerun()

with st.form(key="docker"):
    cnt = st.text_input("스케일 인/아웃할 도커의 개수")
    
    col1,col2 =st.columns(2)
    with col1:
        scale_out = st.form_submit_button(label='manual scale out')
    with col2:
        scale_in = st.form_submit_button(label='manual scale in')
    if scale_out:
        scaleout(cnt)
        result0,result1,result2 = checkAll()
        st.write(cnt,"개","scale out 되었습니다.","총 도커수:",result1,"개 입니다.")
    if scale_in:
        scalein(cnt)
        result0,result1,result2 = checkAll()
        st.write(cnt,"개","scale out 되었습니다.","총 도커수:",result1,"개 입니다.")
  
