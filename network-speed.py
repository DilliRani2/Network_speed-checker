import speedtest

# Create Speedtest object
st = speedtest.Speedtest()

# Find best server
st.get_best_server()

# Measure download and upload speed
download_speed = st.download()
upload_speed = st.upload()

# Convert from bits/s to Megabits/s
download_speed_mbps = round(download_speed / (1024 * 1024), 2)
upload_speed_mbps = round(upload_speed / (1024 * 1024), 2)

# Display results
print("Internet Speed Test Results")
print(f"Download Speed: {download_speed_mbps} Mb/s")
print(f"Upload Speed: {upload_speed_mbps} Mb/s")
