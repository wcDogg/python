# CSV and Leading Zeroes

How to preserve leading zeroes in CSV files and spreadsheets. The broad solution is to convert all fields to `text`. 

## VS Code

1. Install the Excel Viewer extension. 
2. Change the extension setting `Csv-Preview Format Values` to `never`.
3. To view formatted preview, right-click a CSV file and select `Open Preview`.
4. Or open the file as usual. 

## MS Excel

1. Change file extension from `my-file.csv` to `my-file.csv.txt`.
1. Open file in Excel. The `Text Import Wizzard` launches.
1. In `Step 3 of 3` you can select the relevant columns and set their data format to `Text`.
1. A good rule of thumb is to format all columns as text. 

## Google Sheets

DO NOT go to `Drive > + New File Upload` and upload a `.csv` - this links the file to Sheets, makes assumptions about the data, and strips the leading zeros. Instead:

1. Open a new Sheet.
1. Select `File > Import` and select the `.csv` file. 
1. In the `Import File` wizard, uncheck the `Convert text to numbers, dates, and formulas` box. 

Note that this affects the entire sheet - as compared to Excel which lets you format individual columns. 

