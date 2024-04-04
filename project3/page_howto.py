import streamlit as st
from PIL import Image

def page_howto():
    img = Image.open("project3/input_hand.png")
    st.image(img)
    
    st.title("このサイトの使い方")
    st.header("1.手入力verの使い方")
    st.subheader("下図のように各数値を入力して「計算実行」ボタンを押してください。")
    #st.image("image/input_hand.png")
    st.title("\u2193")
    st.subheader("「計算実行」ボタンを押すと下図のように結果が得られます。")
    st.image("image/result_hand.png")
    st.subheader("左側が選ばれたアイテム、右側が最適値と選ばれたアイテムのコストの合計を表しています。")
    st.header("")
    st.markdown('<hr style="border-top: 1px dashed #555;">', unsafe_allow_html=True)
    st.header("")
    st.header("2.csvファイルverの使い方")
    st.subheader("「テンプレートをダウンロードする」ボタンを押してテンプレートファイルをダウンロードします。")
    st.image("image/download.png")
    st.title("\u2193")
    st.subheader("ダウンロードしたファイルは下図のようになっています。")
    st.image("image/csv.png")
    st.title("\u2193")
    st.subheader("1列目にアイテム名、2列目にアイテムのコスト、3列目にアイテムの価値を入力してください。")
    st.image("image/input_csv.png")
    st.title("\u2193")
    st.subheader("ナップサックの容量を入力して、作成したcsvファイルをアップロードし。「計算実行」ボタンを押してください。")
    st.image("image/upload_csv.png")
    st.title("\u2193")
    st.subheader("左側が選ばれたアイテム、右側が最適値と選ばれたアイテムのコストの合計を表しています。")
    st.image("image/result_csv.png")

