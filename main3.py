import streamlit as st

st.title("🔢 이모지 숫자 버튼 계산기")

for key in ["num1", "num2", "active_input"]:
    if key not in st.session_state:
        st.session_state[key] = "" if key != "active_input" else "num1"

# 숫자와 이모지 매핑
emoji_numbers = {i: f"{i}\uFE0F\u20E3" for i in range(10)}  

# 현재 입력 필드 선택
st.session_state.active_input = st.radio(
    "입력 필드를 선택하세요:", ["num1", "num2"], horizontal=True
)

# 숫자 버튼 배치 및 동작
def render_number_buttons():
    col1, col2, col3 = st.columns(3)  # 3개의 열에 버튼 배치
    for i, (num, emoji) in enumerate(emoji_numbers.items()):
        column = [col1, col2, col3][i % 3]
        if column.button(emoji, key=f"btn_{num}"):
            st.session_state[st.session_state.active_input] += str(num)

render_number_buttons()

# 사용자 입력값 및 연산자 선택
st.write(f"**첫 번째 숫자 (num1):** {st.session_state.num1}")
st.write(f"**두 번째 숫자 (num2):** {st.session_state.num2}")
operator = st.selectbox("연산자를 선택하세요 (+, -, *, /):", ["+", "-", "*", "/"])

# 결과 계산 함수
def calculate(x, y, op):
    try:
        x, y = float(x or 0), float(y or 0)
        return {"+" : x + y, "-" : x - y, "*" : x * y, "/" : "0으로 나눌 수 없습니다." if y == 0 else x / y}[op]
    except ValueError:
        return "유효한 숫자를 입력하세요."

# 계산 및 초기화 버튼
col1, col2 = st.columns(2)
if col1.button("계산하기"):
    st.success(f"결과: {calculate(st.session_state.num1, st.session_state.num2, operator)}")

if col2.button("🔄 Reset"):
    for key in ["num1", "num2"]:
        st.session_state[key] = ""
    st.success("입력값이 초기화되었습니다!")
