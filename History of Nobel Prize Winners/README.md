# Nobel Prize Data Analysis

## Project Overview

This project is a data analysis of Nobel Prize winners aimed at uncovering significant patterns and trends. Using a dataset of Nobel laureates, the analysis focuses on demographics such as gender and nationality, time trends, and the identification of individuals or organizations that have won the prize multiple times. The code answers key questions by calculating proportions, identifying standout winners, and recognizing time periods with notable achievements.

### Key Objectives
- Determine the most commonly awarded gender and birth country.
- Identify the decade with the highest ratio of U.S.-born Nobel laureates.
- Find the decade and category with the highest proportion of female laureates.
- Discover the first woman Nobel laureate and her category.
- Compile a list of individuals or organizations that have won more than one Nobel Prize.

## Files
- **notebook.ipynb**: The Jupyter notebook contains the full analysis and code that answers the aforementioned questions based on the Nobel Prize dataset.
- **Questions.docx**: A document outlining the specific questions answered by the analysis.
- **nobel.csv**: The dataset containing information about Nobel laureates.

## Questions Addressed

1. **Most Common Gender and Birth Country**: 
   - The analysis identifies the predominant gender and birth country among Nobel Prize winners.

2. **Decade with Highest U.S. Ratio**: 
   - The project computes the decade that had the highest proportion of U.S.-born laureates in relation to total winners across all categories.

3. **Highest Proportion of Female Laureates**: 
   - A decade-category pair is pinpointed where the proportion of female winners was the highest, showing progress in gender representation.

4. **First Woman Laureate**: 
   - The analysis identifies the first woman to win a Nobel Prize, along with the category she won in.

5. **Repeat Laureates**: 
   - A list of individuals and organizations who have won the prize more than once is generated.

## How to Run

1. Clone the repository:
   
2. Install dependencies:
   Make sure you have Python and the necessary libraries installed. You can use the following to install them:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook to view the analysis:
   ```bash
   jupyter notebook notebook.ipynb
   ```

## Requirements

- Python 3.x
- Pandas
- Jupyter Notebook

## Results

Through the analysis, the following questions were answered:
- Most Common Gender: Male
- Most Common Birth Country: United States of America
- Highest U.S. Ratio Decade: 2000
- Highest Female Representation: {2020: 'Literature'}
- First Female Laureate: Marie Curie, née Sklodowska | Physics
- Repeat Laureates: 
['Comité international de la Croix Rouge (International Committee of the Red Cross)',
 'Frederick Sanger',
 'John Bardeen',
 'Linus Carl Pauling',
 'Marie Curie, née Sklodowska',
 'Office of the United Nations High Commissioner for Refugees (UNHCR)']