import streamlit as st
from functions import get_todos, save_todo

todos = get_todos()

def add_todo(): #gets one todo at a time from the session
    new_todo = st.session_state["new_todo"] #using the key below
    new_todo = new_todo + '\n'
    todos.append(new_todo)
    save_todo(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to improve your productivity") #For simple text

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    # print(checkbox)
    if checkbox == True:
        todos.remove(todo) #The todos list is automatically updated
        save_todo(todos) #we are allowed to save the list here, not at the end of the for lood
        del st.session_state[todo]
        st.experimental_rerun() #To rerun or refresh the page again
 

new_todo = st.text_input("", placeholder="Add new todo....", on_change=add_todo, key='new_todo')

# st.session_state
