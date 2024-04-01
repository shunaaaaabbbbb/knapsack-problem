import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pulp import *


def knapsack_solver(capacity, costs, values):
    # ナップサック問題を解くアルゴリズムを実装
    items = [i for i in range(len(costs))]
    prob = pulp.LpProblem(sense = LpMaximize)
    x = LpVariable.dicts("x", (items), cat="Binary")
    prob += lpSum(values[i] * x[i] for i in items)
    prob += lpSum(costs[i] * x[i] for i in items) <= capacity
    result = prob.solve() 
    selected_items = [i for i in items if x[i].value() == 1]
    opt_value = prob.objective.value()
    opt_cost = 0
    for i in items:
        if x[i].value() == 1:
            opt_cost += costs[i]
    return selected_items, opt_value, opt_cost
    


def display_result(selected_items, opt_value, opt_cost, names_csv=None):
    col1, col2 = st.columns(2)
    col1.header("選ばれたアイテム：")
    if names_csv is not None and not names_csv.empty:
        for item_number in selected_items:
            col1.subheader(names_csv[item_number])
    else:
        for item_name in selected_items:
            col1.subheader(item_name+1)
    col2.header(f"最適値：{opt_value}")
    col2.header(f"コスト合計：{opt_cost}")


def main():

    st.set_page_config(layout="wide")  # ページのレイアウトをワイドに設定
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

    
if __name__ == '__main__':
    main()



def display_result(selected_items, opt_value, opt_cost):
    col1, col2 = st.columns(2)
    col1.header("選ばれたアイテム：")
    for item_name in selected_items:
        col1.subheader(item_name)
    col2.header(f"最適値：{opt_value}")
    col2.header(f"コスト合計：{opt_cost}")   

def display_result_csv(selected_items, opt_value, opt_cost,names_csv):
    col1, col2 = st.columns(2)
    col1.header("選ばれたアイテム：")
    for item_number in selected_items:
        col1.subheader(names_csv[item_number])
    col2.header(f"最適値：{opt_value}")
    col2.header(f"コスト合計：{opt_cost}")   