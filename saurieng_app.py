import streamlit as st

st.set_page_config(page_title="Tính tiền sầu riêng", page_icon="🥭")

st.title("💥 Tính tiền sầu riêng")

gia_thai = 50000
gia_ri6 = 30000

so_kg_thai = st.number_input("Nhập số kg sầu riêng Thái", min_value=0.0, step=0.5)
so_kg_ri6 = st.number_input("Nhập số kg sầu riêng Ri6", min_value=0.0, step=0.5)

tien_thai = so_kg_thai * gia_thai
tien_ri6 = so_kg_ri6 * gia_ri6
tong_tien = tien_thai + tien_ri6

st.write(f"Sầu riêng Thái: {so_kg_thai} kg × {gia_thai:,} đ = {tien_thai:,.0f} đ")
st.write(f"Sầu riêng Ri6: {so_kg_ri6} kg × {gia_ri6:,} đ = {tien_ri6:,.0f} đ")
st.success(f"💰 Tổng cộng: {tong_tien:,.0f} đ")
