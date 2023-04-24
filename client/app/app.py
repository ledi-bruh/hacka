import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from datetime import datetime
from json import loads, dumps
import requests
with open('info.md', 'r',encoding="utf-8") as f:
    markdown_string = f.read()

st.sidebar.title("Ведение базы данных для временного персонала")
st.sidebar.info("Cсылка на "
                "[github](https://github.com/ledi-bruh/hacka)")

with st.sidebar: 
    selected2 = option_menu(None, ["Информация", "Загрузка Данных", 'Формирование выборок'], 
        icons=['info', 'bi bi-arrow-down-square-fill', "bi bi-menu-button-wide-fill"], 
        menu_icon="cast", default_index=0)
    

if selected2 == "Загрузка Данных":
    uploaded_file = st.file_uploader("Выберети файл")
    if uploaded_file is not None:
        upladdata = pd.read_csv(uploaded_file,sep=";",encoding='utf-8')
        upladdata.columns = ["department_id","fio","post_name","attraction_year","observation_name","work_status_code","worker_address","worker_email","worker_phone_number","work_exp_name","work_status_status"]
        data = upladdata.to_json(orient="records")
        response = requests.post('https://httpbin.org/post', data={'records':data})

    df = pd.DataFrame(
    [
       {"Отдел, ответственный за проведение выборочного наблюдения ": "", "ФИО привлеченного работника": "", "Должность": "", "Год привлечения":"","Наименование выборочного наблюдения":"","Место проведения работ":"","Адрес проживания":"","Электронный адрес":"","Контактный номер телефона":"","Опыт работы в Омскстате":"", "Оценка качества работы":""},
    
     ]
    )
    edited_df = st.experimental_data_editor(df, num_rows="dynamic",use_container_width=False,width = 1000)

    if st.button('Отправить'):
       st.write("Добавлено")
if selected2 == "Формирование выборок":
    options = st.sidebar.multiselect(
    'Место проведения работ',
    ['Село Алексеевка', 'Омск', 'Тара', 'Борьшеречье'])
    options2 = st.sidebar.multiselect(
    'Адрес проживания',
    ['Село Алексеевка', 'Омск', 'Тара', 'Борьшеречье'])
    number = st.sidebar.number_input('Введите год',step = 1,max_value=datetime.now().year,min_value=1991)
    name_abs = st.sidebar.text_input('Наименование выборочного наблюдения', placeholder= 'Введите наименование')
    status = st.sidebar.text_input('Оценка качества работы', placeholder= 'Введите оценку')