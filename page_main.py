import streamlit as st
import pandas as pd
from knapsack_solver import knapsack_solver
from display_result import display_result

def page_main():

    
    st.title('ナップサック問題を解いてみよう！')
    st.subheader("このサイトはナップサックの容量、アイテム数、各アイテムのコストと価値を入力したら、ナップサック問題を解いてくれるサイトです。")
    st.write("")
    capacity = st.number_input('ナップサックの容量', min_value=1, key = "capacity")
    num_items = st.number_input('アイテム数（最大10個）', min_value=1,max_value=10, step=1)
    costs = []
    values = []
    
    # 入力されたアイテム数に応じて適切な数のカラムを生成
    columns = []
    for i in range(2):
        columns.append(st.columns(num_items))  # 2つのカラムを作成
    
    # 各アイテムの重さと価値を入力
    for i in range(num_items):
        with columns[0][i]:  # 重さのカラム
            costs.append(st.number_input(f'コスト（アイテム {i+1}） ', min_value=1))
        with columns[1][i]:  # 価値のカラム
            values.append(st.number_input(f'価値（アイテム {i+1}） ', min_value=1))

    if st.button('計算実行', key = "button"):
        selected_items, opt_value, opt_cost = knapsack_solver(capacity, costs, values)
        display_result(selected_items, opt_value, opt_cost)

    st.write("")
    st.write("")
    st.subheader("csvファイルをアップロードしても計算してくれます。")
    df_base = pd.DataFrame({"Names of items":[],"Costs of items":[],"Values of items":[]})
    csv_base = df_base.to_csv(index=False,encoding="shift-jis")
    st.write("")
    st.write("下のボタンを押すとテンプレートのcsvファイルをダウンロードできます")
    st.download_button("テンプレートをダウンロードする",csv_base,file_name="ナップサック問題_テンプレート.csv")
    capacity_csv = st.number_input("ナップサックの容量", min_value=1, key = "capacity_csv")
    data_csv = st.file_uploader("csvファイルをアップロードする", type = "csv", accept_multiple_files=False)
    if data_csv is not None:
        df = pd.read_csv(data_csv, encoding="shift_jis")
        st.write(df)
        names_csv = df["Names of items"]
        costs_csv = df["Costs of items"]
        values_csv = df["Values of items"]
    if st.button('計算実行', key = "button_csv"):
        if data_csv is not None:
            selected_items_csv, opt_value_csv, opt_cost_csv = knapsack_solver(capacity_csv, costs_csv, values_csv)
            display_result(selected_items_csv, opt_value_csv, opt_cost_csv,names_csv)
        else:
            st.write("ファイルをアップロードしてください")

