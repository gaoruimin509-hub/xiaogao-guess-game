import streamlit as st
import random

# 页面标题（改成你想要的）
st.title("是小高的猜·数·游·戏·喔")

st.write("电脑随机生成一个 **4位数字**（0~9，可重复，首位可为0）")
st.write("你来猜，每次只告诉你 **几A**（数字和位置都正确）")
st.write("猜中4A就算赢！没有B提示哦～ 开始吧！")

# 初始化游戏状态
if 'answer' not in st.session_state:
    st.session_state.answer = ''.join(random.choice('0123456789') for _ in range(4))
    st.session_state.guess_count = 0
    st.session_state.history = []

answer = st.session_state.answer

# 输入框（固定 key）
guess = st.text_input(
    f"第 {st.session_state.guess_count + 1} 次猜测（请输入4位数字，可重复）：",
    value="",
    max_chars=4,
    key="current_guess"
)

if st.button("提交猜测！"):
    if not guess:
        st.warning("请输入4位数字再提交哦～")
    elif len(guess) != 4 or not guess.isdigit():
        st.error("请输入正好 **4位** 的数字！（0-9，可重复）")
    else:
        st.session_state.guess_count += 1
        a = sum(1 for i in range(4) if guess[i] == answer[i])
        result = f"{a}A"
        st.session_state.history.append((guess, result))
        
        if a == 4:
            st.success(f"恭喜！！！ 猜对了～ 答案就是 **{answer}**")
            st.balloons()
            st.write(f"你一共用了 **{st.session_state.guess_count} 次**！")
            
            if st.button("再玩一局"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
        else:
            st.info(f"→ {result}")

# 历史猜测显示移到这里（提交逻辑之后）
if st.session_state.history:
    st.write("历史猜测：")
    for g, result in st.session_state.history:
        st.write(f"- {g} → {result}")

# 侧边栏小提示（可选）
st.sidebar.write("规则：只显示A（位置+数字正确）")
st.sidebar.write("答案可重复，输入也可重复")
st.sidebar.write("提交后输入框保留上次猜测，可直接修改～")
