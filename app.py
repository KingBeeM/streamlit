# - *- conding:UTF-8 -*-
import streamlit as st
import pandas as pd
from utils import p_lans

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

if __name__ == "__main__":
    main()