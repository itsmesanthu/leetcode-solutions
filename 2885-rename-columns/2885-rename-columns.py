import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(students)
    df.columns=['student_id','first_name','last_name','age_in_years']
    return df