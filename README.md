# python-data-cleaning for KoboToolbox
By Shamim Alituha |UCC Intern, Ex-UBOS-MoH, NIRA, Electoral Commission | Kampala, Uganda 

Clean messy KoboToolbox exports with Python - standardize names, fix dates, remove duplicates, create clean dataset ready  for analysis.

## What it does
My script proves you can fix real field problems automatically:
Fixes: duplicates - same '_id' submitted twice? Gone
       bad dates  - '2024/01/15', 'bad date', '2024-01-15' -> one standard date format.
       extra spaces - '"Kampala "' and '"YES "' -> '"Kampala"' and '"YES"'

## Files:
1.  clean_kobo_export.py - The python script
2.  kobo_export_sample.xlsx - Dirty data (before) - 5 rows, with duplicates and bad dates.
3.  cleaned_output.xlsx - Clean data (after) - 4 rows, no duplicates, dates fixed.

  ## Shows before/after cleaning messy field data.
  ** Before (dirty): **
| _id | district | household_size | has_mosquito_net | survey_date |
|---|---|---|---|---|
1 | "Kampala " | 5 | "YES " | 2024-01-15
2 | kampala | 5 | yes | 2024/01/15
1 |  Kampala| 5  | "YES" | 2024-01-15 (duplicate)
3 | WAKISO |   | no | bad-date

  ** After (Clean): **
| _id | district | household_size | has_mosquito_net | survey_date |

1 | Kampala | 5 | YES | 2024-01-15
2 | kampala | 5 | yes | 2024-01-15
## 1 | Kampala | 5 | YES| 2024-01-15 (duplicate removed) ##

3 | WAKISO |   | no | (blank removed invalid date)

## How to Run it: 
1. pip install pandas openpyxl - Installs the pandas
2. Put your kobo export as 'kobo_export_sample.xlsx' in the same folder
3. Run: 'python clean_kobo_export.py'
4. Get 'cleaned_output.xlsx'

   ## Ican clean your data for you
   I clean kobo / ODK / Excel SPSS exports for NGOs, health surveys, and research teams.
   Hire me on Upwork: Shamim Alituha - Software Engineer | Python $ PHP

By Shamim | Ex-UBOS MoH
