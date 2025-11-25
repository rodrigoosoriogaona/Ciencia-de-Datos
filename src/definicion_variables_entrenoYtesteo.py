import pandas as pd
from sklearn.model_selection import train_test_split
import os
import pandas as pd

#Funciones para definir las rutas tanto para este .py (utilizado en los modelos)
#Como para el excel (utilizado tanto en este .py como en los modelos)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(BASE_DIR, "data", "train_limpio.xlsx")

df = pd.read_excel(excel_path)

X = df.drop(columns=['SalePrice','Id'])
y = df['SalePrice']

X_codificado = pd.get_dummies(X,drop_first=True)

X_entreno, X_test, y_entreno, y_test = train_test_split(
    X_codificado, y, test_size=0.2, random_state=42
)


