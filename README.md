
# Gym Progress Tracker
#### Video Demo: https://youtu.be/YourVideoDemoURL
#### Creator: Diego Diaz
#### GitHub Usernames: diegodiaz25
#### Hult Section: CM3
#### Date Recorded: 03/03/2023

## Description:
Gym Progress Tracker is a robust and interactive Python web application designed to help users record, monitor, and analyze their gym workouts over time. This project allows you to log essential workout details such as the exercise performed, the time spent at the gym (in minutes), the number of sets and repetitions per set, the weight lifted, and your body weight at the time of the workout. The application then computes your workout “volume” (calculated as sets * reps * weight lifted) and provides progressive insights through interactive graphs and detailed logs.

The primary aim of Gym Progress Tracker is to empower gym enthusiasts to see their progress through clear data visualization. Whether you are looking to track improvements in strength, monitor your body weight changes, or simply keep a record of your workouts, this application consolidates all key metrics into one convenient interface. In addition to logging workouts, the application offers a visual representation of trends over time, making it easier to adjust your training regimen and optimize your fitness routines.

The project was implemented in Python using the Streamlit framework for the user interface, Pandas for data manipulation, and pytest to ensure correctness and maintainability. All core functionalities reside in the file `project.py`, which includes a main function along with several helper functions (such as add_gym_log, calculate_total_volume, get_progress_summary, and display_logs) that work together to create a cohesive experience. The corresponding tests for these helper functions are provided in the file `test_project.py`, ensuring that changes to the codebase do not break the core functionality.

Gym Progress Tracker is organized into three main sections accessed via tabs:
- **Log Entry:** This section allows users to record new gym workouts. Here you input the exercise name, time spent at the gym, the number of sets, reps per set, weight lifted, and your current body weight. Each log entry is timestamped automatically, and the workout volume is calculated immediately.
- **View Logs:** In this tab, users can view a table of all their logged workouts. The logs are sorted by date and include all details recorded, as well as an overall summary that shows total entries, cumulative volume, and the latest recorded body weight.
- **Progress Graphs:** This section converts your logged workout data into interactive visual graphs. You can view trends over time in your body weight, workout volume, and even the time spent at the gym. These graphs offer valuable insights, allowing users to easily track their fitness improvements and adjust their training accordingly.

## File Structure and Contents:
```
GYM_PROGRESS_TRACKER/
├── project.py           # Main application file containing the main() function and helper functions.
├── test_project.py      # Pytest test cases for validating the helper functions in project.py.
├── requirements.txt     # Lists all pip-installable dependencies (streamlit, pytest, pandas).
└── README.md            # This detailed project documentation file.
```

- **project.py:**  
  This is the entry point of the application and contains the main function along with functions for adding logs, calculating total workout volume, generating progress summaries, and converting logs to a format suitable for display and graphing.

- **test_project.py:**  
  This file includes tests for each of the major helper functions. Test functions are prefixed with `test_` (e.g., test_add_gym_log, test_calculate_total_volume, test_get_progress_summary) to ensure that each component of the project works as intended.

- **requirements.txt:**  
  This file includes a list of all the necessary dependencies required to run the application. It ensures that any user cloning the project can simply install all libraries using the command `pip install -r requirements.txt`.

- **README.md:**  
  This document explains the project in detail, including its purpose, file structure, usage instructions, design decisions, and possible future improvements.

## Features:
- **Interactive Log Entry:**  
  Users can easily record their gym workouts by entering detailed information such as the exercise, gym duration, sets, reps, weight lifted, and body weight. Each entry is stored along with an automatic timestamp.
  
- **Comprehensive Log Viewing:**  
  Workout logs are displayed in a table format with sorting by timestamp and an overall summary of progress, making it simple to review past performance.

- **Detailed Progress Graphs:**  
  The application generates interactive graphs to illustrate trends in body weight, workout volume, and time spent at the gym. This visual feedback is ideal for identifying improvements or adjusting training plans.

- **Modular and Testable Code:**  
  All core functionalities are separated into clearly defined functions that can be tested independently using pytest. This modular approach makes the project maintainable and extensible.

## Getting Started:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/gym-progress-tracker.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd gym-progress-tracker
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Web Application:**
   ```bash
   streamlit run project.py
   ```
5. **Run Tests:**
   ```bash
   pytest test_project.py
   ```

## Design Decisions and Future Improvements:
### Design Choices:
- **Separation of Concerns:**  
  The application is organized into distinct tabs (Log Entry, View Logs, and Progress Graphs) to isolate data input, review, and visualization. This improves usability and simplifies future enhancements.
  
- **Interactive Data Visualization:**  
  Leveraging Streamlit’s charting features and Pandas DataFrames, the application provides clear, dynamic graphs that help users monitor trends in their training metrics.

- **Modular Code Structure:**  
  By isolating core functionalities into separate helper functions and maintaining a clear file structure, the code is easier to read, test, and extend over time.

### Challenges Encountered:
- **State Management:**  
  Managing user session data with Streamlit’s session state was critical to delivering a seamless user experience across different tabs.
  
- **Data Visualization:**  
  Converting log data into intuitive graphs required thoughtful use of Pandas, but ultimately allowed for dynamic and interactive progress charts.

### Future Improvements:
- **Persistent Data Storage:**  
  Future versions might integrate a database or file-based storage to allow users to retain their logs between sessions.
  
- **Enhanced Analytics:**  
  Additional analytics such as exercise-specific trends, performance forecasting, and personalized recommendations could provide deeper insights.
  
- **User Accounts and Authentication:**  
  Implementing user authentication and personalized dashboards would allow individual users to maintain long-term workout records and progress history.
  
- **Mobile Optimization:**  
  Adapting the interface for mobile devices could help users log workouts on the go.

## Conclusion:
Gym Progress Tracker merges robust functionality with an intuitive user interface to create a comprehensive tool for monitoring gym workouts. Its organized design, interactive graphs, and detailed logs empower users to understand their progress and make informed training decisions. With a modular codebase that is thoroughly tested and a user-friendly layout, this application serves as both a practical fitness tracker and an example of high-quality Python software design.

**Credits:**  
Developed by Diego Diaz  
*(CHATGPT was used as a helper tool to resolve certain design challenges and amplify aspects of this assignment)*
