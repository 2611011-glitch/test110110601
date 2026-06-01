import streamlit as st

# 1. 페이지 설정 (웹 브라우저 탭에 표시될 내용)
st.set_page_config(
    page_title="홍길동의 포트폴리오",
    page_icon="👋",
    layout="centered"
)

# 2. 사이드바 구성 (연락처 및 프로필 사진 정보 등)
st.sidebar.header("Contact Info")
st.sidebar.write("📧 이메일: gildong@example.com")
st.sidebar.write("🐙 GitHub: [github.com/gildong](https://github.com)")
st.sidebar.write("📝 블로그: [gildong.tistory.com](https://tistory.com)")

# 3. 메인 화면 - 헤더 영역
st.title("👋 안녕하세요, 홍길동입니다!")
st.subheader("성장을 즐기는 3년 차 파이썬 백엔드 개발자입니다.")

# 이미지 넣기 (이미지 파일이 없다면 이 부분은 주석 처리하거나 기본 URL을 넣으세요)
# st.image("profile.jpg", width=200) 

st.write("---")

# 4. 자기소개 및 핵심 역량
st.header("📌 About Me")
st.write(
    """
    데이터를 다루고 효율적인 시스템을 구축하는 것에 흥미가 많습니다.  
    새로운 기술을 배우는 것을 두려워하지 않으며, 팀원들과의 원활한 소통을 중요하게 생각합니다.
    """
)

# 5. 기술 스택 (Tech Stacks)
st.header("🛠 Tech Stacks")

# 깔끔하게 보여주기 위해 컬럼 나누기
col1, col2 = st.columns(2)

with col1:
    st.subheader("Languages")
    st.write("- Python 🐍")
    st.write("- JavaScript 🟨")
    st.write("- SQL 🗄️")

with col2:
    st.subheader("Frameworks & Tools")
    st.write("- Django / FastAPI")
    st.write("- Git & GitHub")
    st.write("- Streamlit")

st.write("---")

# 6. 주요 프로젝트 Experience
st.header("💼 Projects")

# 첫 번째 프로젝트
with st.expander("🚀 스트림릿을 활용한 데이터 시각화 웹 앱 (2026)"):
    st.write("**주요 역할:** Full-stack 개발")
    st.write("**사용한 기술:** Python, Streamlit, Pandas")
    st.write("- 공공 데이터를 활용하여 실시간 날씨 및 미세먼지 정보를 시각화하는 대시보드 구축")
    st.write("- UI/UX 반응형 디자인 적용 및 배포 완료")

# 두 번째 프로젝트
with st.expander("🛍️ 이커머스 백엔드 시스템 고도화 (2025)"):
    st.write("**주요 역할:** 백엔드 API 설계 및 DB 최적화")
    st.write("**사용한 기술:** FastAPI, PostgreSQL, Docker")
    st.write("- 레거시 코드 리팩토링을 통해 API 응답 속도 30% 개선")
    st.write("- 동시성 문제를 해결하기 위한 DB 트랜잭션 격리 수준 조정")

st.write("---")

# 7. 방문자 방명록 (인터랙티브 기능 추가)
st.header("💌 한 줄 응원 메시지")
visitor_name = st.text_input("이름을 입력해주세요:")
message = st.text_area("응원의 한마디를 남겨주세요:")

if st.button("메시지 남기기"):
    if visitor_name and message:
        st.success(f"🎉 {visitor_name}님, 소중한 의견 감사합니다!")
        # 실제로 저장하려면 DB나 파일 저장 로직을 추가해야 합니다.
        st.info(f"[{visitor_name}]: {message}")
    else:
        st.warning("이름과 메시지를 모두 입력해주세요.")