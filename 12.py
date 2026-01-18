import streamlit as st

# ================== CẤU HÌNH TRANG ==================
st.set_page_config(
    page_title="Vương quốc mô hình",
    page_icon="✨",
    layout="wide"
)

# ================== SIDEBAR ==================
with st.sidebar:
    st.title("Vương quốc mô hình")
    st.header("Chào mừng bạn đến Vương quốc mô hình!")
    st.image("PYDC4.13/hinh1.jpg")
    st.write("""
    Chúng tôi chuyên bán các mô hình nhân vật hoạt hình chất lượng cao.
    Luôn cập nhật và đa dạng sản phẩm.
    Cam kết sự hài lòng của khách hàng.
    """)
    st.write("🏠 Địa chỉ cửa hàng:")
    st.write("📞 Điện thoại liên hệ:")

# ================== TIÊU ĐỀ CHÍNH ==================
st.title("VƯƠNG QUỐC MÔ HÌNH")

# ================== NÚT CHỌN CHỦ ĐỀ ==================
col1, col2, col3 = st.columns(3)

with col1:
    b1 = st.button("Dragon Ball")

with col2:
    b2 = st.button("Naruto")

with col3:
    b3 = st.button("One Piece")

# ================== DRAGON BALL ==================
if b1:
    st.header("Danh sách mô hình Dragon Ball")
    col4, col5, col6 = st.columns(3)

    with col4:
        st.image("PYDC4.13/hinh2.jpg",
                 caption="Goku Ultra Instinct – Mã số: 001")

    with col5:
        st.image("PYDC4.13/hinh3.jpg",
                 caption="Vegeta Super Saiyan – Mã số: 002")

    with col6:
        st.image("PYDC4.13/hinh4.jpg",
                 caption="Piccolo – Mã số: 003")

# ================== NARUTO ==================
if b2:
    st.header("Danh sách mô hình Naruto")
    col4, col5, col6 = st.columns(3)

    with col4:
        st.image("PYDC4.13/hinh5.jpg",
                 caption="Uzumaki Naruto – Mã số: 001")

    with col5:
        st.image("PYDC4.13/hinh6.jpg",
                 caption="Uchiha Sasuke – Mã số: 002")

    with col6:
        st.image("PYDC4.13/hinh7.jpg",
                 caption="Hatake Kakashi – Mã số: 003")

# ================== ONE PIECE ==================
if b3:
    st.header("Danh sách mô hình One Piece")
    col4, col5, col6 = st.columns(3)

    with col4:
        st.image("PYDC4.13/hinh8.jpg",
                 caption="Monkey D. Luffy – Mã số: 001")

    with col5:
        st.image("PYDC4.13/hinh9.jpg",
                 caption="Roronoa Zoro – Mã số: 002")

    with col6:
        st.image("PYDC4.13/hinh10.jpg",
                 caption="Vinsmoke Sanji – Mã số: 003")

# ================== FORM ĐẶT HÀNG ==================
st.header("Đặt hàng")

with st.form("Đơn đặt hàng"):
    topics = ("Dragon Ball", "Naruto", "One Piece")
    option_topic = st.selectbox("Chủ đề mô hình", topics)

    codes = ("001", "002", "003")
    option_code = st.selectbox("Mã số mô hình", codes)

    nums = st.slider("Số lượng bạn muốn đặt:", 1, 10, 1)

    name = st.text_input("Họ và tên")
    phone = st.text_input("Số điện thoại")
    address = st.text_input("Địa chỉ giao hàng")

    submitted = st.form_submit_button("Xác nhận")

# ================== HIỂN THỊ HÓA ĐƠN ==================
if submitted:
    bill = {
        "Loại mô hình": option_topic,
        "Mã số": option_code,
        "Số lượng": nums,
        "Họ tên khách hàng": name,
        "Số điện thoại": phone,
        "Địa chỉ giao hàng": address
    }

    st.header("Bạn đã chọn:")
    for x, y in bill.items():
        st.write(x, ":", y)

# ================== IN & TẢI HÓA ĐƠN ==================
print_bill = st.checkbox("In hóa đơn")

if print_bill and submitted:
    ans = ""
    for x in bill:
        ans += str(x) + ": " + str(bill[x]) + "\n"

    st.download_button(
        "In hóa đơn",
        ans,
        file_name="hoa_don.txt"
    )
