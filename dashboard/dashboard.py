import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set_theme(style="dark")

seller_df = pd.read_csv("./data/sellers_dataset.csv")
payment_df = pd.read_csv("./data/order_payments_dataset.csv")

# Create a function for payment type
def payment_type(payment_df, min_payment_value):
    filtered_df = payment_df[payment_df['payment_value'] >= min_payment_value]
    payment_type_df = filtered_df['payment_type'].value_counts().reset_index()
    return payment_type_df

def seller_location(seller_df, limit):
    seller_location_df = seller_df['seller_city'].value_counts().reset_index()
    if (limit == "Top 3"):
        limit = 3
    elif (limit == "Top 5"):
        limit = 5
    else:
        limit = 10
    seller_location_df = seller_location_df[:limit]
    return seller_location_df

st.header("E commerce Dashboard")
tab1, tab2 = st.tabs(["Payment Type","Seller Distribution"])
# Section 1
with tab1:
    st.subheader("Payment Type")

    min_payment_value = st.slider("Minimum Payment Value", 0, 1000, 100)
    payment_type_df = payment_type(payment_df, min_payment_value)
    fig, ax = plt.subplots()
    ax.bar(payment_type_df['payment_type'], payment_type_df['count'])
    ax.set_xlabel('Payment Type')
    ax.set_ylabel('Count')
    ax.set_title('Count of order by Payment Type')
    st.pyplot(fig)

# Section 2
with tab2:
    st.subheader("Seller Location")
    # Dropdown top 5,3, all
    option = st.selectbox("Select how many data to display",
                ("Top 3", "Top 5", "Top 10"),
                index=None, placeholder="Select how many data to display")
    seller_location_df = seller_location(seller_df, option)
    fig, ax = plt.subplots()
    ax.bar(seller_location_df['seller_city'], seller_location_df['count'])
    ax.set_xlabel('Seller City')
    ax.set_xticklabels(seller_location_df['seller_city'], rotation=45)
    ax.set_ylabel('Count')
    ax.set_title('Distribution of seller')
    st.pyplot(fig)