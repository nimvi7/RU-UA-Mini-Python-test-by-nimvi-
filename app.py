import streamlit as st 
st.set_page_config(page_title="Мини тест от Nimvi", page_icon="🎲", layout="wide")
st.title("Привет!, Рад тебя видет на моем мини/-тесте")
st.header("Что бы прости на тест тебе надо перейти в раздел *Мини-тест*")
tab1, tab2=st.tabs(["Про тест", "Мини-тест"])
col1, col2= st.columns([1,2])



with tab1:
    st.header("Про-мой мини-тест")
    st.subheader("Я создал мини-тест про знание языка Python,")
    st.subheader("В моем мини-тесте будет только 3 вопроса")
    st.subheader("В этом мини-тесте только легкие вопросы по языку Pathon")


with tab2:
     st.progress(0/3)
score = 0


with tab2: 
        
        q1 = st.radio("Что такое python?",["Зебра","Язык програмирования","JavaScript"])
        if st.button("Проверить", key=246567):
            if q1 is None:
                 st.warning("Выбери ответ")
            else:
                 score = 1 if q1 == "Язык програмирования" else 0 
                 st.subheader(f"Результат: {score} из 1 ")
                 if score == 1:
                     st.success("Правельно!!")
                     st.progress(1/3)
                     score = 1
                 else:
                     st.error("Не правельно!!")









with tab2:
      q2 = st.radio("Что делает Print?",["Пичает()","Майнкрафт-мод","Читает файл"])
      if st.button("Проверить", key=24656):
        if q2 is None:
             st.warning("Выбери ответ")
        else:
             score = 2 if q2 == "Пичает()" else 1 
             st.subheader(f"Результат: {score} из 2 ")
             if score == 2:
                  st.success("Правельно!!")
                  st.progress(2/3)
                  score = 2  
             else:
                  st.error("Не правельно!!")








with tab2:
      q3 = st.radio("print(5 + 3)?",["8","print(5 + 3)","print(8)"])
      if st.button("Проверить", key=24655736):
        if q3 is None:
             st.warning("Выбери ответ")
        else:
             score = 3 if q3 == "8" else 2 
             st.subheader(f"Результат: {score} из 3 ")
             if score == 3:
                  st.success("Правельно!!")
                  st.progress(3/3)
                  st.balloons()
             else:
                  st.error("Не правельно!!")






