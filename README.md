# F1_Driver Analytics
🏎️ F1 Driver Analytics Dashboard

An interactive Formula 1 Driver Analytics Dashboard built using Python, Pandas, Plotly, and Streamlit.

The dashboard allows users to explore and compare Formula 1 drivers based on career statistics such as championships, race wins, podiums, pole positions, fastest laps, points, and performance rates.

---

📊 Project Overview

Formula 1 generates a large amount of historical driver performance data. This project transforms driver statistics into an interactive dashboard that makes it easier to analyze career performance and compare drivers across different eras.

Users can interact with the dashboard using filters, charts, driver comparisons, and individual driver profiles.

---

✨ Features

📌 Dashboard Overview

- Total number of drivers
- Total championships
- Total race wins
- Total podiums
- Total points
- Interactive visualizations

🏆 Driver Rankings

- Top 10 drivers by championships
- Top 10 drivers by race wins
- Driver performance rankings
- Points-based analysis

⚔️ Driver Comparison

Compare any two drivers based on:

- Championships
- Race entries
- Race starts
- Pole positions
- Race wins
- Podiums
- Fastest laps
- Points
- Win rate
- Podium rate

👤 Driver Profile

Select an individual driver to view:

- Nationality
- Seasons
- Years active
- Championships
- Race wins
- Podiums
- Points
- Pole positions
- Fastest laps
- Career performance chart

🌍 Historical Analysis

Explore:

- Drivers by nationality
- Drivers by decade
- Active vs retired drivers
- Champions vs non-champions

🔎 Interactive Filters

Filter the dashboard by:

- Nationality
- Decade
- Driver status
- Championship status

---

🛠️ Technologies Used

Technology| Purpose
Python| Programming language
Pandas| Data processing and analysis
Plotly| Interactive charts
Streamlit| Web dashboard
NumPy| Numerical operations
Jupyter Notebook| Data exploration and analysis

---

📁 Project Structure

F1_Driver_Analytics/
│
├── app.py
├── F1Drivers_Dataset.csv
├── README.md
└── requirements.txt

---

📋 Dataset

The dataset contains aggregated Formula 1 driver career statistics.

Important columns

Driver
Nationality
Seasons
Championships
Race_Entries
Race_Starts
Pole_Positions
Race_Wins
Podiums
Fastest_Laps
Points
Active
Decade
Pole_Rate
Win_Rate
Podium_Rate
Points_per_Entry
Years_Active
Champion

---

🚀 Installation

1. Clone the repository

git clone https://github.com/yourusername/f1-driver-analytics.git

2. Navigate to the project directory

cd f1-driver-analytics

3. Install the required libraries

pip install -r requirements.txt

If you don't have a "requirements.txt" file, install them manually:

pip install streamlit pandas plotly numpy

---

▶️ Run the Dashboard Locally

Run the following command:

streamlit run app.py

The dashboard will open in your browser at:

https://f1drivers-dabczzsj82qyf87urqdjrf.streamlit.app/

---

📈 Dashboard Visualizations

The dashboard includes interactive Plotly visualizations such as:

- 🏆 Top Drivers by Championships
- 🥇 Top Drivers by Race Wins
- 📈 Race Wins vs Career Points
- 📅 Drivers by Decade
- 🌍 Drivers by Nationality
- 👤 Individual Driver Performance
- ⚔️ Driver-to-Driver Comparison

All charts support interactive features such as hovering, zooming, filtering, and selecting data points.

---

💡 Key Questions Explored

This dashboard can help answer questions such as:

1. Who has won the most F1 World Championships?
2. Who has the most race victories?
3. Which drivers have the highest podium counts?
4. How are race wins related to career points?
5. Which nationalities have produced the most F1 drivers?
6. How has the number of drivers changed across decades?
7. How does one driver compare with another?
8. Which drivers have the highest win or podium rates?
9. How do active drivers compare with retired drivers?
10. Which drivers have had the longest careers?

---

🎯 Project Objectives

The main objectives of this project are:

- Analyze historical Formula 1 driver data
- Perform exploratory data analysis
- Create meaningful visualizations
- Build an interactive dashboard
- Enable driver-to-driver comparisons
- Present statistical insights in an easy-to-understand format
- Deploy the dashboard as a web application

---

☁️ Deployment

The application can be deployed using Streamlit Community Cloud.

Deployment Steps

1. Push the project to GitHub.
2. Make sure "app.py", the dataset, and "requirements.txt" are included.
3. Connect the GitHub repository to Streamlit Community Cloud.
4. Select "app.py" as the main application file.
5. Deploy the application.

Once deployed, the dashboard can be accessed through a public web URL.

---

📦 Requirements

Create a "requirements.txt" file containing:

streamlit
pandas
numpy
plotly

---

🔮 Future Improvements

Possible future enhancements include:

- 🏁 Race-by-race performance analysis
- 🗺️ Interactive map of driver nationalities
- 📅 Season-wise driver performance
- 🏎️ Constructor/team analysis
- 🏆 Championship progression
- 📊 Advanced driver performance scoring
- 🔥 Driver era comparison
- 📈 Career progression charts
- 🏁 Circuit-specific analysis
- 🌐 Live Formula 1 data integration
- 📱 Improved mobile responsiveness

---

👨‍💻 Author

Your Name

Data Analytics & Visualization Project

---

⭐ Acknowledgements

This project was created as a data analytics and visualization project using Python and Streamlit.

Special thanks to the open-source Python ecosystem for providing tools such as Pandas, Plotly, NumPy, and Streamlit.

---

📜 License

This project is intended for educational and analytical purposes.

Feel free to use, modify, and improve the project for learning and personal projects.
