AICTE Internship Project - Climate Risk and Disaster Management
This repository contains my AICTE Internship project on Climate Risk and Disaster Management using the Forest Fire Dataset (derived from NASA’s EONET API via Kaggle). The project focuses on analyzing natural disasters such as wildfires, forestfire and there impact.

---

## Week 1 Project
In Week 1, the goal was to reach the Data Understanding stage:

Imported necessary Python libraries (pandas, numpy)
Loaded the dataset (Data.csv)
Explored dataset using:

.info() → structure of data

.describe() → summary statistics

.isnull().sum() → missing values check

Previewed disaster categories and their counts

This forms the foundation for deeper analysis and visualization in upcoming weeks.

📂 Files in Repository

Foresfire.ipynb → Notebook for Week 1

Forestfires.csv → Forest Fire Dataset

README.md → Project description


⚙️ How to Run
Clone the repository
git clone https://github.com/your-username/AICTE-ClimateRisk-Project.git


---

## Week 2 Project 

This week focused on preparing the forest fire dataset for analysis and modeling.

* **Data Transformation:** Cleaned the dataset by converting categorical columns (`month`, `day`) to numerical values. Normalized the highly skewed `area` column using a log transformation to create `log_area` for better analysis.
* **Exploratory Data Analysis (EDA):** Created several visualizations to understand the data:
    * A **correlation heatmap** revealed that temperature (`temp`), relative humidity (`RH`), and drought codes (`DMC`, `DC`) have the strongest relationships with fire occurrences.
    * **Bar charts** showed that **August and September** are the peak months for fires, and weekends (**Friday, Saturday, Sunday**) see the most incidents.
    * An interactive **geographical map** (`forest_fire_map.html`) was generated to visualize the location and size of the fires.
 

 ⚙️ How to Run

1.  Ensure you have `pandas`, `numpy`, `seaborn`, `matplotlib`, and `folium` installed.
2.  Open the Jupyter Notebook (`Forestfire Week2.ipynb`) and run the cells.

