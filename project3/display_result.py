import streamlit as st

def display_result(selected_items, opt_value, opt_cost, names_csv=None):
    col1, col2 = st.columns(2)
    col1.header("選ばれたアイテム：")
    if names_csv is not None and not names_csv.empty:
        for item_number in selected_items:
            col1.subheader(names_csv[item_number])
    else:
        for item_name in selected_items:
            col1.subheader(f"アイテム{item_name+1}")
    col2.header(f"最適値：{opt_value}")
    col2.header(f"コスト合計：{opt_cost}")