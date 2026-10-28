
import streamlit as st

st.set_page_config(page_title="Конвертер величин", page_icon="🔄")

tab1, tab2, tab3 = st.tabs([
    "🏠 Головна",
    "🔄 Конвертер",
    "🔗 Корисні посилання"
])

with tab1:
    st.title("🏠 Мій додаток")
    st.write("Ласкаво просимо до інтерактивного конвертера величин!")

with tab2:
    st.title("🔄 Конвертер величин")

    mode = st.selectbox(
        "Оберіть конвертер",
        ["Метри в кілометри", "Цельсій у Фаренгейт"]
    )

    value = st.number_input("Введіть значення", value=0.0)

    if st.button("Конвертувати"):
        if mode == "Метри в кілометри":
            st.success(f"Результат: {value / 1000} км")
        else:
            result = value * 9 / 5 + 32
            st.success(f"Результат: {result} °F")

with tab3:
    st.title("🔗 Корисні посилання")
    st.write("Навчальні сайти та ігри")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📚 Навчання")
        st.markdown("[📖 W3Schools](https://www.w3schools.com/)")
        st.markdown("[💻 GitHub](https://github.com/)")
        st.markdown("[🎓 Khan Academy](https://www.khanacademy.org/)")

    with col2:
        st.subheader("🎮 Ігри")
        st.markdown("[🎮 Poki](https://poki.com/)")
        st.markdown("[🕹️ CrazyGames](https://www.crazygames.com/)")
        st.markdown("[♟️ Chess.com](https://www.chess.com/)")
