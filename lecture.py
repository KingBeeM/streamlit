# - *- conding:UTF-8 -*-
import streamlit as st
import pandas as pd
from PIL import Image
from utils import p_lans

# Data VIZ
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # title
    st.title("Hellow World")

    # text
    st.text("This is so {}".format("good"))

    # Header
    st.header("This is Header")

    # Subheader
    st.subheader("This is subHeader")

    # Markdown
    st.markdown("## This is Markdown")

    # 색상이 들어간 텍스트 feature
    st.success("성공")
    st.warning("경고")
    st.info("정보와 관련된 탭")
    st.error("에러 메시지")
    st.exception("예외처리")

    # st.write()
    st.write("일반 텍스트")
    st.write(1+2)
    st.write(dir(str))

    st.title(":sunglasses:")

    # Help
    st.help(range)
    st.help(st.title)

    # 데이터 불러오기
    st.title("IRIS 데이터")
    iris = pd.read_csv("data/iris.csv")

    st.title("st.dataframe()")
    st.dataframe(iris, 200, 100) # Height, Width

    st.title("st.table()")
    st.table(iris)

    st.title("st.write()")
    st.write(iris)

    myCode = """
    def hellow():
        print("hi")
    """
    st.code(myCode, language="Python")

    # 위젯, button 기능 활용
    name = "kingbee"
    if st.button("Submit"):
        st.write(f"name: {name.upper()}")

    # RadioButton
    s_state = st.radio("status", ("활성화", "비활성화"))
    if s_state == "활성화":
        st.success("활성화 상태")
    else:
        st.error("비활성화 상태")

    # Check Box
    if st.checkbox("show/hide"):
        st.text("show")

    # Select Box
    choice = st.selectbox("프로그래밍 언어", p_lans) # utils.py 에서 불러오기
    st.write(f"{choice} 언어를 선택함")

    # multitple selection
    lans = ("영어", "일본어", "중국어", "독일어")
    myChoice = st.multiselect("언어 선택", lans, default="중국어")
    st.write("선택", myChoice)

    # slider
    age = st.slider("나이", 1, 120)
    st.write(age)

    # Image 가져오기
    img1 = Image.open("data/image_01.jpg")
    st.image(img1)
    img2 = Image.open("data/image_02.jpg")
    st.image(img2)
    img3 = Image.open("data/image_03.jpg")
    st.image(img3)

    url = "https://thumb.mt.co.kr/06/2023/01/2023010306193413103_1.jpg"
    st.image(url)

    # Video 출력
    with open("data/secret_of_success.mp4", "rb") as rb:
        video_file = rb.read()
        st.video(video_file, start_time=1)

    # Audio 출력
    with open("data/song.mp3", "rb") as rb:
        audio_file = rb.read()
        st.audio(audio_file, format="audio/mp3")

    # 화면 분할
    iris = pd.read_csv("data/iris.csv")

    choice = st.selectbox("iris_species", iris["species"].unique())
    st.title(choice)

    result = iris[iris["species"] == choice].reset_index(drop=True)
    st.dataframe(result)

    fig = px.scatter(data_frame=result, x='sepal_length', y='sepal_width')
    st.plotly_chart(fig)

    col1, col2 = st.columns([0.5, 0.5], gap="large")
    with col1:
        fig1, ax = plt.subplots()
        sns.scatterplot(result, x="petal_length", y="sepal_width")
        st.pyplot(fig1)

    with col2:
        fig2, ax = plt.subplots()
        ax.scatter(x=result["sepal_length"], y=result["sepal_width"])
        st.pyplot(fig2)

if __name__ == "__main__":
    main()