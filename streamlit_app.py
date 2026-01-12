import streamlit as st

st.title("🎈 숙대 Streamlit 강의")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).\n\n"
    "Streamlit 페이지를 닫은 경우에는 아래에 있는 '터미널' 옆의 '포트' 를 누른다.\n\n"
    "그리고, 전달된 주소 위에 마우스를 올리면 미리보기를 할 수 있다.\n\n"
    "역시 최고의 선생님!\n\n"
    "CodeSpaces 를 항상 새로고침하면 계속 로딩하기때문에 오래 걸린다.\n\n"
    "File Change 라는 글자가 보이면 Rerun 을 통해서 필요할 때마다 열자."
)

# 정보성 메시지 박스
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메시지입니다.")

st.write("지금 오른쪽 화면은 개인 화면 \n\n"
    "변경 사항을 반영하기 위해서는 왼쪽에 있는 파란 동그라미 아이콘 활용\n\n"
         "변경 내용 동기화 를 누르시면 git fetch 하냐고 하면 Yes 누르면 된다. \n\n"
         "이후에는 streamlit 메인 페이지에서 아이콘 눌러서 서버 올라온거 공유하면 된다. \n\n " \
         "동기화 안되면 Reboot\n\n")
