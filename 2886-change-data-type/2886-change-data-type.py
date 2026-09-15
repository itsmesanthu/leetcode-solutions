import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(students)
    df=df.astype({'grade':int})
    return df