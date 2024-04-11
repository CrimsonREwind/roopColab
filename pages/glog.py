import streamlit as st
import time

st.title("Real-Time Log Viewer")

log_file_path = "/kaggle/working/roop/logs.txt"
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
