import streamlit as st
import os
import subprocess

image_input = st.text_input("enter input image name ")
video_input = st.text_input("enter input video name ")
video_output = st.text_input("enter output video name ")


checkbox_result = st.checkbox("run script")


if st.button("run"):
    input_a = "/content/gdrive/MyDrive/roop/input/" + image_input
    input_b = "/content/gdrive/MyDrive/roop/input/" + video_input
    output = "/content/gdrive/MyDrive/roop/output/" + video_output
    new_directory = '/content/gdrive/MyDrive/roop'
    os.chdir(new_directory)
    normal = f'python run.py -s {input_a} -t {input_b} -o {output} --keep-frames --keep-fps --execution-provider cuda --frame-processor face_swapper face_enhancer'
    enhanced = f'python run.py -s {input_a} -t {input_b} -o {output} --keep-frames --keep-fps --execution-provider cuda --frame-processor face_swapper'
    subprocess.run(command, shell=True)

    if checkbox_result:
      subprocess.run(enhanced, shell=True)
    else:
      subprocess.run(normal, shell=True)