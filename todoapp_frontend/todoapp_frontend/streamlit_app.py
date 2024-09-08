import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api"

def get_tasks():
    response = requests.get(f"{API_URL}/get-all-notes")
    return response.json()

def add_task(task):
    response = requests.post(API_URL, json=task)
    return response.json()

def update_task(task_id, task):
    response = requests.put(f"{API_URL}/{task_id}", json=task)
    return response.json()

def delete_task(task_id):
    response = requests.delete(f"{API_URL}/{task_id}")
    if response.status_code == 200:
        return True
    else:
        return False

tasks = get_tasks()

st.markdown("<h1 style='text-align: center; color: black;'>To-Do List</h1>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h2 style='color: black;'>Add New Task</h2>", unsafe_allow_html=True)
new_task = st.text_input('New task:')
add_task_button = st.markdown("""
    <style>
    .stButton button {
        background-color: white;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)
if st.button('Add Task'):
    if new_task:
        new_id = max(task['id'] for task in tasks) + 1 if tasks else 1
        task = {'id': new_id, 'task': new_task, 'done': False}
        add_task(task)
        st.experimental_rerun()

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h2 style='color: black;'>Tasks</h2>", unsafe_allow_html=True)
for task in tasks:
    cols = st.columns([3, 1, 1, 1])

    with cols[0]:
        if task['done']:
            st.markdown(f"""
                <style>
                .task-done:hover {{
                    color: black;
                }}
                </style>
                <span class='task-done' style='color: darkgreen; text-decoration: line-through; text-decoration-color: gray;'>{task['task']}</span>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <style>
                .task:hover {{
                    color: black;
                }}
                </style>
                <span class='task' style='color: black;'>{task['task']}</span>
                """, unsafe_allow_html=True)

    with cols[1]:
        done = st.checkbox("Done", value=task['done'], key=f'done_{task["id"]}')
        if done != task['done']:
            task['done'] = done
            update_task(task['id'], task)
            st.experimental_rerun()

    with cols[2]:
        if st.button('Update', key=f'update_{task["id"]}'):
            st.session_state.edit_task_id = task['id']
            st.session_state.edit_task_value = task['task']
            st.experimental_rerun()

    with cols[3]:
        if st.button('Delete', key=f'delete_{task["id"]}'):
            if delete_task(task['id']):
                st.experimental_rerun()

if 'edit_task_id' in st.session_state:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: black;'>Edit Task</h2>", unsafe_allow_html=True)
    task_id = st.session_state.edit_task_id
    task_value = st.session_state.edit_task_value
    new_task_value = st.text_input('Edit task:', value=task_value, key='edit_task_input')
    if st.button('Save', key='save_task'):
        for task in tasks:
            if task['id'] == task_id:
                task['task'] = new_task_value
                update_task(task_id, task)
                break
        del st.session_state.edit_task_id
        del st.session_state.edit_task_value
        st.experimental_rerun()

st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        © 2024 Task Manager
    </div>
    """, unsafe_allow_html=True)