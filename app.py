import streamlit as st
import os
import subprocess
import time

current_path = os.getcwd()

tab1, tab2 = st.tabs(["DeepFake", "Logs"])
log_file_path = f"{current_path}/roop/logs.txt"
log_text_key = "log"

if not os.path.exists(os.path.join(current_path, "roop", "input")):
    os.makedirs(os.path.join(current_path, "roop", "input"))

def save_uploaded_file(uploaded_file):
    # Save the file to the "uploads" folder
    with open(os.path.join(current_path, "roop", "input", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

def get_uploaded_filenames():
    # Get the list of files in the "uploads" folder
    files = os.listdir(os.path.join(current_path, "roop", "input"))
    return files

with tab1:
    uploaded_files = st.file_uploader("Choose files to upload", accept_multiple_files=True)
    if uploaded_files:
        st.write("### Uploaded Files:")
        for file in uploaded_files:
            file_details = {"filename": file.name, "filetype": file.type, "filesize": file.size}
            st.write(file_details)

            # Save the file to a folder
            save_uploaded_file(file)

    image_input = st.selectbox("Choose a file", get_uploaded_filenames(), key="input_image")
    video_input = st.selectbox("Choose a file", get_uploaded_filenames(), key="input_video")
    video_output = st.text_input("enter output video name ")


    checkbox_result = st.checkbox("run script")


    if st.button("run"):
        input_a = f"{current_path}/roop/input/{image_input}"
        input_b = f"{current_path}/roop/input/{video_input}"
        output = f"{current_path}/roop/output/{video_output}"
        new_directory = f'{current_path}/roop'
        os.chdir(new_directory)
        normal = f'python run.py -s {input_a} -t {input_b} -o {output} --keep-frames --keep-fps --execution-provider cuda --frame-processor face_swapper face_enhancer'
        enhanced = f'python run.py -s {input_a} -t {input_b} -o {output} --keep-frames --keep-fps --execution-provider cuda --frame-processor face_swapper'

        if checkbox_result:
          subprocess.run(enhanced, shell=True)
        else:
          subprocess.run(normal, shell=True)
with tab2:
    
    def read_log_file():
        with open(log_file_path, 'r') as file:
            content = file.read()
        return content
    
    st.title("Real-Time Log Viewer")
    
    while True:
        try:
            # Read and display the content of the log file
            log_content = read_log_file()

            # Use st.text_area with a single key for the text area
            dynamic_key = f"{log_text_key}_{int(time.time())}"
            st.text_area("Log Content", log_content, height=200, key=dynamic_key)
            
            # Sleep for a short interval (e.g., 1 second) before updating again
            time.sleep(1)
        except FileNotFoundError:
            st.error(f"File not found: {log_file_path}")
            break
