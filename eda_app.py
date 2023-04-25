# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import utils

def run_eda_app():
    st.subheader("탐색적 자료 분석")

    iris = pd.read_csv("data/iris.csv")
    st.markdown("## IRIS DATA")
    st.write(iris)

    # 메뉴 지정
    submenu = st.sidebar.selectbox("하위메뉴", ["기술통계량", "그래프분석", "통계분석"])
    if submenu == "기술통계량":
        st.dataframe(iris)
        with st.expander("데이터타입"):
            st.write(iris.dtypes)
        with st.expander("기술통계량"):
            st.write(iris.describe())
        with st.expander("타겟 빈도 수 확인"):
            st.write(iris["species"].value_counts())
    elif submenu == "그래프분석":
        st.title("그래프분석")
        with st.expander("산점도"):
            fig1 = px.scatter(iris, x = "sepal_width", y = "sepal_length", color = "species", size = "petal_width", hover_data = ["petal_length"])
            st.plotly_chart(fig1)

        # layouts
        col1, col2 = st.columns(2)
        with col1:
            st.title("Seaborn")
            fig2, ax = plt.subplots()
            sns.scatterplot(iris, x="sepal_width", y="sepal_length", hue="species", ax=ax)
            st.pyplot(fig2)

        with col2:
            st.title("Matplotlib")
            fig3, ax = plt.subplots()
            colors = {"Iris-setosa":"red", "Iris-versicolor":"green", "Iris-virginica":"blue"}
            ax.scatter(x=iris["sepal_width"], y=iris["sepal_length"], color=iris["species"].map(colors))
            st.pyplot(fig3)

        # Tabs
        tab1, tab2, tab3 =st.tabs(["탭1", "탭2", "탭3"])
        with tab1:
            st.write("탭1")
            choice_species = st.selectbox("iris_species", iris["species"].unique())
            st.title(choice_species)
            fig4 = px.scatter(data_frame=iris[iris["species"] == choice_species].reset_index(drop=True),
                             x="sepal_width", y="sepal_length")
            st.plotly_chart(fig4)

        with tab2:
            st.write("탭2")
            student = pd.read_csv("data/학생.csv")
            student = student.drop(student[student["group"].isin(["all", "middleschool", "highschool"])].index, axis=0).reset_index(drop=True)

            plt.rc("font", family="Malgun Gothic")
            fig5, ax = plt.subplots(nrows=6, ncols=8, figsize=(40, 40))
            i = 0; j = 0
            for col in student.columns[3:]:
                ax[i, j].boxplot([student[student["gender"]=="male"][col], student[student["gender"]=="female"][col]])
                ax[i, j].set_title(col)
                ax[i, j].set_xticklabels(["male", "female"])
                j += 1
                if j > 7:
                    i += 1
                    j = 0
            st.pyplot(fig5)

        with tab3:
            st.write("탭3")
            choice_col = st.selectbox("column", student.columns[3:])
            st.title(choice_col)

            plt.rc("font", family="Malgun Gothic")
            fig6, ax = plt.subplots()
            ax.boxplot([student[student["gender"]=="male"][choice_col], student[student["gender"]=="female"][choice_col]])
            ax.set_title(choice_col)
            ax.set_xticklabels(["male", "female"])
            st.pyplot(fig6)

    elif submenu == "통계분석":
        pass
    else:
        st.warning("warning")