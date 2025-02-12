import streamlit as st
import methods

todos = methods.readonfile()

def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    todos.append(todo)
    methods.writeonfile(todos)

def del_todo(index:int):
    todos.pop(index)
    methods.writeonfile(todos)


st.title("My Todo App")
st.subheader("this is my todo App.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox_list = st.checkbox(todo, key=todo)
    if checkbox_list:
        todos.pop(index)
        methods.writeonfile(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

#st.session_state