import serpapi
from serpapi import GoogleSearch






import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
def compare(med_name):
    params = {
        "engine": "google_shopping",
        "q": med_name,
        "gl":"in",
        "location":"india",
        "api_key": "1062f568e9afa2c000cddf53bb15e5a35acdcd901cf294a21590a5c62ff2b531"

    }
    search = GoogleSearch(params)
    results = search.get_dict()
    shopping_result = results["shopping_results"]
    return shopping_result

col1,col2 = st.columns(2)
col1.image("e_pharmacy.png",width = 200)
col2.header("E_Pharmacy price Comparision system")
st.sidebar.title("Enter Name Of Medicine : ")
st.sidebar.markdown(" ")
st.sidebar.markdown(" ")
med_name = st.sidebar.text_input("Enter the name here 👇:")
number = st.sidebar.text_input("Enter number of option here 👇:")
medicine_comp = []
medicine_price = []

if med_name is not None:
    if st.sidebar.button("Price compare"):
        shopping_results = compare(med_name)
        lowest_price = float((shopping_results[0].get("price"))[1:])
        lowest_price_index = 0
        st.sidebar.image(shopping_results[1].get("thumbnail"))
        for i in range(int(number)):
            current_price = float((shopping_results[i].get("price"))[1:])
            medicine_price.append (float((shopping_results[i].get("price"))[1:]))
            medicine_comp.append(shopping_results[i].get("source"))

            st.title(f"option{i+1}")
            col1,col2 = st.columns(2)
            col1.write("Company")
            col2.write(shopping_results[i].get("source"))

            col1.write("Title")
            col2.write(shopping_results[i].get("title"))

            col1.write("Price")
            col2.write(shopping_results[i].get("price"))


            url = shopping_results[i].get("product_link")
            col1.write("Buy link")
            col2.write("[Link](%s)"%url)
            """------------------------------------------------------"""
            if (current_price < lowest_price):
                lowest_price = current_price
                lowest_price_index = i


        st.title("Best Option")
        col1, col2 = st.columns(2)
        col1.write("Company")
        col2.write(shopping_results[lowest_price_index].get("source"))

        col1.write("Title")
        col2.write(shopping_results[lowest_price_index].get("title"))

        col1.write("Price")
        col2.write(shopping_results[lowest_price_index].get("price"))

        url = shopping_results[lowest_price_index].get("product_link")
        col1.write("Buy link")
        col2.write("[Link](%s)" % url)

        df = pd.DataFrame(medicine_price,medicine_comp)
        st.title("chart Comparision")
        st.bar_chart(df)

        fig,ax = plt.subplots()
        ax.pie(medicine_price,labels = medicine_comp,shadow = True)
        ax.axis("equal")
        st.pyplot(fig)






