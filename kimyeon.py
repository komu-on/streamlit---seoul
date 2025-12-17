import streamlit as st 
import time

questions = [
    {
        "question": "시간이 나면 뭐 하지?",
        "options": {"🎬 동영상을 본다.": 13, "📚 책을 읽는다.": 0}
    },
    {
        "question": "나의 겨울철 잠옷 스타일은?",
        "options": {"👕 가볍게 입고 난방 28도": 68, "🧤 두껍게 껴입고 난방 26도": 50}
    },
    {
        "question": "걸으면 20분 거리.. 나의 선택은?",
        "options": {"🚶‍♀️ 운동할 겸 걸어다닌다.": 0, "🚗 어른들께 차로 데려다 달라고 한다.": 4}
    },
    {
        "question": "스마트폰이 새로 나왔다고?",
        "options": {"📱 최대한 빨리 바꾼다.": 90, "👍 그래도 2년은 써야지": 45}
    },
    {
        "question": "배가 출출해서 간식을 먹으려고 한다.",
        "options": {"🍊 오렌지": 16, "🍊 감귤": 1}
    },
    {
        "question": "나의 샤워 스타일은 어떨까?",
        "options": {"🚿 후다다닥 15분 안에 끝": 21, "🛀 꼼꼼하게 따뜻하게 30분": 43}
    },
    {
        "question": "부산에 가족여행 가려고 하는데",
        "options": {"🚂 분위기 있는 기차": 6, "✈️ 빠른게 최고 비행기": 53}
    },
    {
        "question": "명절에 받은 용돈으로 옷을 산다면?",
        "options": {"🛍️ 저렴한 옷 3벌": 30, "💎 좋은 옷 1벌": 10}
    },
    {
        "question": "작년에 산 청바지가 있지만, 올해는 다른 디자인이 유행인걸",
        "options": {"👖 유행은 못 참지~ 새로산다.": 33, "🙅‍♀️ 뭘 또 사~ 참는다.": 0}
    },
    {
        "question": "내가 자주 먹는 반찬은?",
        "options": {"🐮 소고기": 115, "🐷 삼겹살": 31, "🐟 고등어구이": 5}
    },
    {
        "question": "밥 먹고 깨끗하게 밥상 닦으라고 하셨다.",
        "options": {"🧼 행주로 닦기": 1, "🧻 물티슈로 닦기": 5}
    },
    {
        "question": "나는 밥 먹을 때",
        "options": {"😋 남김없이 먹는다.": 0, "🍚 한 숟가락씩 남긴다.": 3}
    },
    {
        "question": "가족들과 공원 나들이~ 우리 가족은?",
        "options": {"👨‍👩‍👧‍👦 부모님 차로 이동한다.": 70, "🚌 대중교통을 이용한다.": 33}
    },
    {
        "question": "새로운 음식이 먹고 싶을 때 우리 가족은?",
        "options": {"🍽️ 음식점 가서 외식": 1, "🛵 집에서 편하게 배달": 20}
    },
    {
        "question": "두 메뉴 중 하나만 먹어야 한다면?",
        "options": {"🍗 치킨": 30, "🥗 나물 비빔밥": 11}
    },
    {
        "question": "나는 평소 물을 마실 때?",
        "options": {"💧 페트병": 18, "🥤 텀블러": 1}
    }
]

st.title("🌍기후 위기 밸런스 게임🌍")

# session_state 초기화
if 'carbon_score' not in st.session_state:
    st.session_state.carbon_score = 0
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'show_loading' not in st.session_state:
    st.session_state.show_loading = False
if 'show_reference' not in st.session_state:
    st.session_state.show_reference = False

# 시작 화면
if not st.session_state.game_started:
    st.write("전 지구인이 당신처럼 산다면 지구 평균 기온은 몇 도나 올라가나요?")
    st.caption("주의! 정답일 것 같은 것을 누르지 말고 진짜 내 평소 모습 반영하기")
    if st.button("시작하기"):
        st.session_state.game_started = True
        st.rerun()

# 게임이 진행 중일 경우
elif not st.session_state.game_over:
    # 현재 질문 정보 가져오기
    current_q = questions[st.session_state.question_index]
    st.subheader(f"질문 {st.session_state.question_index + 1}")
    st.write(current_q["question"])

    # 답변 버튼 생성
    cols = st.columns(len(current_q["options"]))
    for i, (option, score) in enumerate(current_q["options"].items()):
        with cols[i]:
            if st.button(option, key=f"opt_{i}"):
                st.session_state.carbon_score += score
                st.session_state.question_index += 1
                if st.session_state.question_index >= len(questions):
                    st.session_state.game_over = True
                    st.session_state.show_loading = True
                st.rerun()
    
    st.progress((st.session_state.question_index) / len(questions))
    st.write(f"현재까지의 탄소 점수: {st.session_state.carbon_score}")

# 모든 질문에 답했을 경우 (게임 종료)
else:
    if st.session_state.show_loading:
        with st.spinner('결과를 확인해봅시다...'):
            time.sleep(3)
        st.session_state.show_loading = False
        st.rerun()

    score = st.session_state.carbon_score

    # 결과 데이터를 구조화하여 관리
    result_data = [
        {"range": (0, 184), "temp": 1, "effect": st.balloons, "img_url": "https://img.icons8.com/fluency/480/thermometer.png", "message": """
        그 결과, 북극의 얼음이 녹는 속도가 빨라져 북극곰이 멸종 위기에 놓입니다.
        폭염, 산불, 홍수 등의 이상기후가 발생합니다.🌱
        """},
        {"range": (185, 260), "temp": 2, "effect": st.snow, "img_url": "https://img.icons8.com/fluency/480/sea-waves.png", "message": """
        그 결과, 그린란드 전체가 녹아 저지대의 주요 도시가 바다에 잠기고 열사병으로 사망하는 환자들이 수십만 명이 됩니다.
        식량 부족 현상으로 인간은 물론 동물 사료 공급도 위기입니다.😥
        """},
        {"range": (261, 340), "temp": 3, "effect": st.snow, "img_url": "https://img.icons8.com/fluency/480/desert.png", "message": """
        그 결과, 죽음의 문턱. 극도로 위험한 살인적인 폭염과 습도로 인해
        지구의 폐, 아마존이 사라집니다.
        전세계적 식량 부족으로 분쟁이 발생하고 문명이 붕괴됩니다.😨
        """},
        {"range": (341, 500), "temp": 4, "effect": st.snow, "img_url": "https://img.icons8.com/fluency/480/tsunami.png", "message": """
        그 결과, 남극의 빙하가 붕괴되어 아프리카, 호주, 미국이 물에 잠깁니다.😱😱
        """},
        {"range": (501, float('inf')), "temp": 5, "effect": st.snow, "img_url": "https://img.icons8.com/fluency/480/skull.png", "message": """
        그 결과, 지구상 생명체의 종말에 가까워집니다.
        극지방이 녹아내리고 인간 사회가 알고 있던 지구의 모습은 거의 없는 비인간적이고 폭력적인 세계가 됩니다.☠️☠️
        """}
    ]

    temperature_rise = 0
    result_message = ""
    result_effect = None
    result_img_url = "https://img.icons8.com/fluency/480/thermometer.png"

    for data in result_data:
        min_score, max_score = data["range"]
        if min_score <= score <= max_score:
            temperature_rise = data["temp"]
            result_message = data["message"]
            result_effect = data["effect"]
            result_img_url = data["img_url"]
            break

    st.success("🎉 모든 질문에 답변했습니다. 결과 확인하기 🎉")
    st.subheader(f"최종 탄소 점수: {score}점")
    st.write(f"전 세계 모든 사람이 당신처럼 생활한다면, 지구의 평균 기온은 약 **{temperature_rise}도** 상승할 것으로 예상됩니다!")
    
    # 결과 이미지 보여주기
    st.image(result_img_url, width=300)

    if result_effect:
        result_effect()
    st.write(result_message)
    
    if st.button("다른 결과 확인하기"):
        st.session_state.show_reference = not st.session_state.show_reference

    if st.session_state.show_reference:
        st.divider()
        st.subheader("🌡️ 지구 온도 상승별 변화")
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image("https://cdn-icons-png.flaticon.com/512/808/808602.png", caption="지구 온도계")
        with col2:
            st.markdown("""
            * **1도 (0~184점)**: 집중호우, 한파 등 기상 현상 증가
            * **2도 (185~260점)**: 적도지방 주요 도시 거주 불가능
            * **3도 (261~340점)**: 아마존 열대우림 파괴, 남부유럽 가뭄
            * **4도 (341~500점)**: 남극의 빙하붕괴, 아프리카, 호주, 미국 침수
            * **5도 (501~620점)**: 대부분 생물체 대멸종
            """)

    if st.button("다시 시작하기"):
        # 게임 상태를 초기값으로 재설정
        st.session_state.carbon_score = 0
        st.session_state.question_index = 0
        st.session_state.game_over = False
        st.session_state.game_started = False
        st.session_state.show_reference = False
        st.rerun()
