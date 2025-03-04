import streamlit as st
import pandas as pd
from datetime import datetime

def add_gym_log(logs, exercise, time_spent, sets, reps, weight_lifted, body_weight):
    """
    Adds a new gym log to the logs list.
    Each log is a dictionary containing:
      - exercise: The exercise performed (e.g., "Bench Press")
      - time_spent: Time spent at the gym in minutes (int)
      - sets: Number of sets (int)
      - reps: Number of reps per set (int)
      - weight_lifted: Weight lifted (float, in kg)
      - body_weight: User's body weight at time of log (float, in kg)
      - timestamp: Date and time when the log was recorded
      - volume: Computed as sets * reps * weight_lifted (float)
    Returns the updated logs list.
    """
    log_entry = {
        "exercise": exercise,
        "time_spent": int(time_spent),
        "sets": int(sets),
        "reps": int(reps),
        "weight_lifted": float(weight_lifted),
        "body_weight": float(body_weight),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "volume": int(sets) * int(reps) * float(weight_lifted)
    }
    logs.append(log_entry)
    return logs

def calculate_total_volume(logs):
    """
    Calculates the total exercise volume from all logs.
    """
    return sum(log["volume"] for log in logs)

def get_progress_summary(logs):
    """
    Returns a summary string of gym progress.
    The summary includes total number of logs, total volume, and the latest body weight.
    """
    if not logs:
        return "No logs to summarize."
    total_volume = calculate_total_volume(logs)
    latest_body_weight = logs[-1]["body_weight"]
    summary = f"Total Entries: {len(logs)} | Total Volume: {total_volume:.1f} | Latest Body Weight: {latest_body_weight:.1f} kg"
    return summary

def display_logs(logs):
    """
    Converts the logs list into a Pandas DataFrame for display.
    """
    if logs:
        df = pd.DataFrame(logs)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df.sort_values(by='timestamp', ascending=False)
    return pd.DataFrame()

def initialize_app():
    """
    Initializes (or resets) the gym log session state.
    """
    st.session_state.logs = []

def main():
    st.title("Gym Progress Tracker")
    st.write("Record your gym workouts by tracking the exercise, time spent at the gym, sets, reps, weight lifted, and your body weight.")

    # Initialize session state for logs if it doesn't exist
    if "logs" not in st.session_state:
        initialize_app()
    
    # Create three tabs for different application sections
    tab1, tab2, tab3 = st.tabs(["Log Entry", "View Logs", "Progress Graphs"])

    #---------- Tab 1: Log Entry ------------
    with tab1:
        st.header("Add a New Gym Log")
        with st.form("log_form", clear_on_submit=True):
            # Allow user to input the exercise name
            exercise = st.text_input("Exercise Name:", "")
            time_spent = st.number_input("Time Spent (minutes):", min_value=1, value=60, step=1)
            sets = st.number_input("Sets:", min_value=1, value=3, step=1)
            reps = st.number_input("Reps per Set:", min_value=1, value=10, step=1)
            weight_lifted = st.number_input("Weight Lifted (in kg):", min_value=0.0, value=20.0, step=0.5, format="%.1f")
            body_weight = st.number_input("Your Body Weight (in kg):", min_value=0.0, value=70.0, step=0.5, format="%.1f")
            submitted = st.form_submit_button("Add Log")
            if submitted:
                if exercise.strip() == "":
                    st.error("Please enter the exercise name.")
                else:
                    st.session_state.logs = add_gym_log(
                        st.session_state.logs, exercise, time_spent, sets, reps, weight_lifted, body_weight
                    )
                    st.success("Gym log added successfully!")

    #---------- Tab 2: View Logs ------------
    with tab2:
        st.header("Your Gym Logs")
        df_logs = display_logs(st.session_state.logs)
        if df_logs.empty:
            st.info("No logs recorded yet.")
        else:
            st.dataframe(df_logs)
        st.write(get_progress_summary(st.session_state.logs))

    #---------- Tab 3: Progress Graphs ------------
    with tab3:
        st.header("Progress Graphs")
        df_logs = display_logs(st.session_state.logs)
        if df_logs.empty:
            st.info("No logs to display progress.")
        else:
            df_logs = df_logs.sort_values('timestamp')
            # Plot Body Weight Over Time
            st.subheader("Body Weight Over Time")
            st.line_chart(df_logs.set_index('timestamp')['body_weight'])
            # Plot Volume Over Time
            st.subheader("Volume Over Time")
            st.line_chart(df_logs.set_index('timestamp')['volume'])
            # Plot Time Spent Over Time
            st.subheader("Time Spent at Gym Over Time")
            st.line_chart(df_logs.set_index('timestamp')['time_spent'])

if __name__ == "__main__":
    main()