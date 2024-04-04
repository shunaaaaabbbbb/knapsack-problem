import streamlit as st
from page_main import page_main
from page_howto import page_howto

def main():
    st.set_page_config(layout="wide")  # ページのレイアウトをワイドに設定
    st.sidebar.title("ページ選択")
    page = st.sidebar.radio("", ["このサイトを使ってみる", "このサイトの使い方"])

    if page == "このサイトを使ってみる":
        page_main()
    elif page == "このサイトの使い方":
        page_howto()

if __name__ == "__main__":
    main()