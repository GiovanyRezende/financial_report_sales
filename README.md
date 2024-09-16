# Power BI Report in Financial Sales
*This is a challenge of Data Engineering NTT DATA Bootcamp in [DIO](https://web.dio.me/).* It consists in creating a report for Data Analysis in Power BI with two pages, using [the same dataset from previous project](https://github.com/GiovanyRezende/sales_report/).

## Data Cleaning
The Data Cleaning was made in Python with Pandas:

```
import pandas as pd

df = pd.read_excel('/content/Financial Sample.xlsx')

df['Segment'] = df.Segment.str.upper()
df['Product'] = df.Product.str.upper()
df['Month Name'] = df['Month Name'].str.upper()
df['Units Sold'] = round(df['Units Sold']).astype('int64')
df = df.fillna('None')
df = df.drop(columns=['Month Name','Month Number','Year'])
df.to_excel('financial_sample_transformed.xlsx')
```
*Note: it's needed to declare the correct path for files. This code was made in Google Colab.*

## Interactive Buttons
This report has interactive buttons. The actions envolve change the page and charts, and segment data.

## News Charts
The report has:
- Radar Chart;
- Hierarchical Tree Chart;
- Area Line Chart;
- Map Chart;
- Tremap Chart
