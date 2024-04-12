import streamlit as st
import os
import subprocess
import time

script_dir = os.path.dirname(os.path.realpath(__file__))

tab1, tab2 = st.tabs(["DeepFake", "Logs"])
log_file_path = f"{script_dir}/logs.txt"
log_text_key = "log"

if not os.path.exists(os.path.join(script_dir, "input")):
    os.makedirs(os.path.join(script_dir, "input"))
def save_uploaded_file(uploaded_file):
    # Save the file to the "uploads" folder
    with open(os.path.join(script_dir, "input", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
def get_uploaded_filenames():
    # Get the list of files in the "uploads" folder
    files = os.listdir(os.path.join(script_dir, "input"))
    return files
def videoplay():
    video_file = open(f"{script_dir}/output/{video_output}", 'rb')
    video_bytes = video_file.read()
    if os.path.exists(os.path.join(script_dir, "output", video_output)):
        st.video(video_bytes)

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



    genre = st.radio(
        "Select processing type",
        ["Normal", "Enhanced"],
        captions=["Normal deepfake", "Enhanced deepfake"])

    if st.button("run"):
        input_a = f"{script_dir}/input/{image_input}"
        input_b = f"{script_dir}/input/{video_input}"
        output = f"{script_dir}/output/{video_output}"
        new_directory = f'{script_dir}'
        os.chdir(new_directory)
        normal = f'python run.py -s {input_a} -t {input_b} -o {output} --keep-frames --keep-fps --execution-provider cuda --frame-processor face_swapper face_enhancer'
        enhanced = f'python run.py -s {input_a} -t {input_b} -o {output} --keep-frames --keep-fps --execution-provider cuda --frame-processor face_swapper'
        if genre == 'Normal':
            subprocess.run(normal, shell=True)
        if genre == 'Enhanced':
            subprocess.run(enhanced, shell=True)
        videoplay()




with tab2:
    
    st.title("Real-Time Log Viewer")

    def tail_log_file(log_file_path):
        # Open the file in read mode
        with open(log_file_path, "r") as log_file:
            # Read the initial lines, if any
            lines = log_file.readlines()
            for line in lines:
                st.text(line.strip())

            # Continuously read new lines
            while True:
                where = log_file.tell()  # Get current file position
                line = log_file.readline()
                if not line:
                    time.sleep(1)  # Wait for new data
                    log_file.seek(where)  # Go back to the file's current position
                else:
                    st.text(line.strip())


    tail_log_file(log_file_path)
