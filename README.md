# AI Preparedness Index (AIPI) Analysis

This project anlayses the relationship between countries' economic status and AI preparedness. The analysis assesses the impact 4 macro-structural indicators: digital infrastructure, human capital and labor market policies, innovation and economic integration, and regulation and ethics have on AI preparedness. The AIPI Index score is the sum of these 4 key macro-structural indicators. The analysis also examines whether certain indicators are more influential on specific economic statuses and which indicator is most influential on high AIPI scores.

## Motivation

AI has taken the world by a storm over recent decades and advancements in AI are happening quickly and becoming evermore present in our lives, such as voice assistants, image recognition, and Chat GPT. Only a few years ago Chat GPT was a basic chatbot, but today is significantly more advanced. It can analyse text and images, solve mathematical problems and generate a wide range of text outputs.

This analysis aims to provide data-driven insights into how prepared countries are to adopt AI depending on their economic status. 
It highlights the impact of factors such as access to internet, use of mobile-phones for online transactions, education and digital skills and flexibility of wage determination. These factors all fall under a macro-structural indicator on AI preparedness which offers valuable information for policymakers and businesses looking to boost AI adoption.


## Dataset

The datset includes the AIPI index score and the four AIPI indicator scores of 174 countries. It also categories countries by the economic status. The 3 categories are a such: Advanced economies (AE), Emerging market economies (EM) and Low-income countries (LIC).

## Analysis Methods

- Visualisations using Python libraraies: Matplotlib, Pandas and NumPY
- Statistical analysis to explore relationships between AIPI and economoic status

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/orelafifo/AI-ANALYSIS.git
   ```
2. Navigate to the project folder:
   ```bash
   cd AI-ANALYSIS
   ```
3. Install the required dependencies:
   ```bash
   pip install --user -r requirements.txt
   ```
4. Run the main analysis script:
   ```bash
   python main_analysis.py
   ```


## Results

- Advanced economies are the most prepared for AI adoption.
- The distribution of AIPI scores is the least skewed and least dispersed for low-income countries.
- Religon and ethics is the most influential AIPI while Innovation and economic integration is the least.

## Testing

A test suite has been created using Python's pytest library. Continuous integration is set up with CirlceCI to ensure that the code is reproduceable and is of a high qulaity.

### Running the Tests
1. Ensure the virtual environment is activated.
2. Run the tests using pytest:
   ```bash
   pytest

    