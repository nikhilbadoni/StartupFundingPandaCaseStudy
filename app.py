import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout= 'wide', page_title= 'Startup Analysis')

df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

def load_overall_analysis():
    st.title('Overall Analysis')

    # total invested amount
    total = round(df['amount'].sum())
    # max amount in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    # avg ticket size (amount to each startup)
    avg_funding = round(df.groupby('startup')['amount'].sum().mean())
    # total funeded startup
    num_startup = df['startup'].nunique()
    
    col1,col2,col3,col4 = st.columns(4)
    
    with col1:
        st.metric('Total',str(total)+ 'CR')
    with col2:
        st.metric('Max',str(max_funding)+ 'CR')
    with col3:
        st.metric('Avg. Funding',str(avg_funding)+ 'CR')
    with col4:
        st.metric('Startups Funded',num_startup)

    st.header('MoM Graph')
    selected_option = st.selectbox('Select Type', ['Total','Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year','month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year','month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    fig6, ax6 = plt.subplots()
    ax6.plot(temp_df['x_axis'], temp_df['amount'])

    st.pyplot(fig6)

def load_investor_details(investor):
    st.title(investor)
    # load recent 5 investments of investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1,col2 = st.columns(2)
    col3,col4 = st.columns(2)
    with col1:
        # Biggest Investments
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig1, ax1 = plt.subplots()
        ax1.bar(big_series.index,big_series.values)

        st.pyplot(fig1)
    with col2:
        # Sectorwise Investment
        vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors Invested In')
        fig2, ax2 = plt.subplots()
        ax2.pie(vertical_series, labels= vertical_series.index, autopct="%0.01f%%")

        st.pyplot(fig2)

    with col3:
        # Roundwise Investment
        round_series = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        st.subheader('Rounds Invested in')
        fig3, ax3 = plt.subplots()
        ax3.pie(round_series, labels= round_series.index, autopct="%0.01f%%")

        st.pyplot(fig3)
    
    with col4:
        # Roundwise Investment
        city_series = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
        st.subheader('Rounds Invested in')
        fig4, ax4 = plt.subplots()
        ax4.pie(city_series, labels= city_series.index, autopct="%0.01f%%")

        st.pyplot(fig4)

    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()

    st.subheader('YoY Investment')
    fig5, ax5 = plt.subplots()
    ax5.plot(year_series.index, year_series.values)

    st.pyplot(fig5)


st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One',['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    st.title('Startup Analysis')
else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)


    
    


