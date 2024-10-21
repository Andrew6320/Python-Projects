Here is a README and brief project description based on the files and project instructions provided.
# Fitness Studio Global & National Workout Interest Analysis

This project explores the global and national interest in various workout types using search trends data from 2018 to 2023. It helps a fitness studio assess interest in home workouts, gym workouts, and related activities, both globally and in specific countries. The analysis addresses peak search trends for workouts, the most popular workout-related keywords during the COVID-19 pandemic, current keyword popularity, and the countries with the highest interest in workouts.

## Project Overview

The project answers the following key questions:
1. **Global Workout Search Peak**: Identifies when global searches for "workout" were at their highest.
2. **Keyword Popularity**: Determines the most popular workout-related keywords during the COVID-19 pandemic and in the present day.
3. **Country Comparison**: Compares workout interest in the United States, Australia, and Japan to find which country has the highest interest.
4. **Expansion to New Markets**: Compares the interest in home workouts between the Philippines and Malaysia to determine the best country for potential expansion.

## Datasets

The project uses the following datasets:

1. **workout.csv**: Monthly global search interest for the term "workout" from 2018 to 2023.
   - Columns: `month`, `workout_worldwide`

2. **workout_geo.csv**: Search interest for "workout" by country from 2018 to 2023.
   - Columns: `country`, `workout_2018_2023`

3. **three_keywords.csv**: Global search interest for three workout-related keywords (home workouts, gym workouts, and home gyms) over the same period.
   - Columns: `home_workout`, `gym_workout`, `home_gym`

4. **three_keywords_geo.csv**: Country-specific search interest for the same three workout-related keywords.
   - Columns: `Country`, `home_workout_2018_2023`, `gym_workout_2018_2023`, `home_gym_2018_2023`

## Key Results

- **Global Peak Year**: The global search for "workout" peaked in the year '2020'.
- **Most Popular Keywords**:
   - During the COVID-19 pandemic, 'home' was the most popular.
   - 2023, 'gym' is the most popular keyword.
- **Top Country for Workout Interest**: Among the United States, Australia, and Japan,'United States' has the highest search interest in workouts.
- **Home Workout Expansion**: Between the Philippines and Malaysia, 'Philippines' has the highest interest in home workouts, making it the ideal market for expansion.

## Variables

- `year_str`: String representing the year of peak global interest in the format "yyyy".
- `peak_covid`: The most popular keyword during the COVID-19 pandemic.
- `current`: The most popular keyword currently.
- `top_country`: The country with the highest workout interest (United States, Australia, or Japan).
- `home_workout_geo`: The country with the highest interest in home workouts between the Philippines and Malaysia.

## Installation & Usage

1. Clone the repository:
  
2. Ensure you have Python installed and the necessary libraries:
   ```bash
   pip install pandas
   ```
3. Run the analysis using the provided scripts to view results.

