import streamlit as st
import os
import subprocess
import time

tab1, tab2 = st.tabs(["DeepFake", "Logs"])
log_file_path = "/content/logs.txt"

with tab1:
    image_input = st.text_input("enter input image name ")
    video_input = st.text_input("enter input video name ")
    video_output = st.text_input("enter output video name ")


    checkbox_result = st.checkbox("run script")


    if st.button("run"):
        input_a = "/content/roop/input/" + image_input
        input_b = "/content/roop/input/" + video_input
        output = "/content/roop/output/" + video_output
        new_directory = '/content/roop'
        os.chdir(new_directory)
        normal = f'python run.py -s {input_a} -t {input_b} -o {output} --keep-frames --keep-fps --execution-provider cuda --frame-processor face_swapper face_enhancer'
        enhanced = f'python run.py -s {input_a} -t {input_b} -o {output} --keep-frames --keep-fps --execution-provider cuda --frame-processor face_swapper'
        subprocess.run(command, shell=True)

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

            # Use st.text_area with a unique key
            st.text_area(f"Log Content: {log_text_key}", log_content, key=log_text_key)
            
            # Sleep for a short interval (e.g., 1 second) before updating again
            time.sleep(1)
        except FileNotFoundError:
            st.error(f"File not found: {log_file_path}")
            break
