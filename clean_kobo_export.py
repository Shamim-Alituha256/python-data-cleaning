"""
Shamim - KoboToolbox Data Cleaning Script
Ex-MoH-UBOS Malaria Survey, NIRA, Electoral Commission
"""
import pandas as pd

def clean_kobo_export(input_file, output_file):
    df = pd.read_excel(input_file)
    print(f"Original rows: {len(df)}")
    
    # 1. Remove duplicates
    if '_id' in df.columns:
        df = df.drop_duplicates(subset=['_id'])
    else:
        df = df.drop_duplicates()
    
    # 2. Fix dates
    date_cols = [c for c in df.columns if 'date' in c.lower()]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    
    # 3. Trim spaces and lower case
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()
    
    print(f"Cleaned rows: {len(df)}")
    df.to_excel(output_file, index=False)
    return df

if __name__ == "__main__":
    clean_kobo_export("kobo_export_sample.xlsx", "cleaned_output.xlsx")
