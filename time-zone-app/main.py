import streamlit as st  # Streamlit library for building the web app
from datetime import datetime  # To work with date and time
from zoneinfo import ZoneInfo  # To handle time zones

TIME_ZONES = [
    "UTC",  # Coordinated Universal Time
    "Asia/Karachi",  # Pakistan Standard Time
    "America/New_York",  # Eastern Time (US)
    "Europe/London",  # Greenwich Mean Time (UK)
    "Asia/Tokyo",  # Japan Standard Time
    "Australia/Sydney",  # Australian Eastern Time
    "Africa/Cairo",  # Eastern European Time (Egypt)
    "America/Los_Angeles",  # Pacific Time (US)
    "Asia/Dubai",  # Gulf Standard Time (UAE)
    "Europe/Paris",  # Central European Time (France)
    "Asia/Singapore",  # Singapore Standard Time
    "America/Chicago",  # Central Time (US)
    "Asia/Shanghai",  # China Standard Time
    "Europe/Berlin",  # Central European Time (Germany)
    "Asia/Seoul",  # Korea Standard Time
    "America/Toronto",  # Eastern Time (Canada)
    "America/Sao_Paulo",  # Brasília Time (Brazil)
    "Africa/Nairobi",  # East Africa Time (Kenya)
    "Asia/Bangkok",  # Indochina Time (Thailand)
    "Europe/Moscow",  # Moscow Standard Time (Russia)
    "Australia/Melbourne"  # Australian Eastern Time (Melbourne)
]

st.title("Time Zone App")  # App title

# Let users select multiple time zones with defaults
selected_timezone = st.multiselect("Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

st.subheader("Selected Timezones")  # Section heading
for tz in selected_timezone:
    # Get current time for the selected timezone
    current_time = datetime.now(ZoneInfo(tz))
    formatted_time = current_time.strftime("%Y-%m-%d %I:%M:%S %p")

    # Display the current time for the selected timezone
    st.write(f"**{tz}**: {formatted_time}")

st.subheader("Convert Time Between Timezones")  # Section heading

# Time input field with current time as default
formatted_time = st.time_input("Current Time", value=datetime.now().time())

# Dropdowns for selecting 'from' and 'to' timezones
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Button to trigger the conversion
if st.button("Convert Time"):
    # Combine date and time with the 'from' timezone
    dt = datetime.combine(datetime.today(), formatted_time, tzinfo=ZoneInfo(from_tz))

    # Convert the time to the selected 'to' timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")

    # Show the converted time
    st.success(f"Converted Time in {to_tz}: {converted_time}")

# Let me know if you want me to add anything else or tweak more! 🚀
