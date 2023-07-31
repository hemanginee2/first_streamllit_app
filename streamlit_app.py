import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title( 'My  Parents New Healthy Diner' ) 
streamlit.header( 'Breakfast Menu' )
streamlit.text( 'Omega 3 & Blueberry Oatmill' )
streamlit.text( 'Kale Spinach & Rocket Smoothie' )
streamlit.text( 'Hard-Boiled Free Range Egg' )
streamlit.header( ' 🥣Breakfast Favorites' )
streamlit.text( '   🥗Omega 3 & Blueberry Oatmill' )
streamlit.text( '   🐔Kale Spinach & Rocket Smoothie' )
streamlit.text( '   🥑🍞Hard-Boiled Free Range Egg' )
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index( 'Fruit' )
streamlit.dataframe(my_fruit_list)


# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page
streamlit.dataframe( my_fruit_list )

# Let's put a pick list here so they can pick the fruit they want to include 


# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page
streamlit.dataframe( fruits_to_show )

# streamlit.header("Fruityvice Fruit Advice!")
# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)
streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?)
    # if not fruit_choice:
    #       streamlit.error("Please select a fruit to 
    if not fruit_choice:
                streamlit.error('Please select a fruit to get information.')
        else:
                back_from_function = get_fruityvice data(fruit_choice)
                streamlit.dataframe(back_from_function)

    
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# streamlit.text(fruityvice_response)
# streamlit.text(fruityvice_response.json())
# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
# import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT *from fruit_load_list")
# my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(" The Fruit Load List Contais:")
streamlit.header(" The Fruit Load List Contais:")
# streamlit.text(my_data_row)
# streamlit.dataframe(my_data_row)
streamlit.dataframe(my_data_rows)
streamlit.stop()
# fruit_choice = streamlit.text_input('What fruit would you like to add?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)







