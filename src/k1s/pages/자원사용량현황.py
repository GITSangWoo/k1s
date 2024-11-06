import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from k1s.autoscale import wherelog

st.set_page_config(
    page_title="scale in/out 관리자 페이지 2",
    page_icon="👋",
)

st.write("도커 및 자원 사용량 현황👋")

log_path=wherelog()

df = pd.read_csv(log_path)
cdf = df[['time','CPUuses']]
Ispot = df[df['scaleIO']=="I"]
Ospot = df[df['scaleIO']=="O"]
#st.dataframe(Ispot)
#st.dataframe(Ospot)
#st.write(df.columns)

flg = plt.figure()
plt.plot(df['time'],df['CPUuses'],data=df)
plt.scatter(x=Ispot['time'], y=Ispot['CPUuses'],marker='o',color="red",label='scale in ')
plt.scatter(x=Ospot['time'], y=Ospot['CPUuses'],marker='s',color="green",label='scale out')
plt.legend(loc='lower left')

plt.xticks(rotation=45)
st.pyplot(flg)


