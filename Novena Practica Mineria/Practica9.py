import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd

#Avance de la practica, esto no es la practica final, hare modificaciones.

def entrenar_modelo_lineal(df: pd.DataFrame, x_col: str, y_col: str):
    x = sm.add_constant(df[x_col])
    model = sm.OLS(df[y_col], x).fit()
    print(model.summary())
    return model

def hacer_prediccion(model, new_data):
    new_data = sm.add_constant(new_data)
    predictions = model.predict(new_data)
    return predictions

def generar_regresion_lineal():
    data_frame = pd.read_csv("DataSet.csv")
    df_sal_min_max = data_frame[['Salary Range From', 'Salary Range To']]
    df_sal_min_max.reset_index(inplace=True)
    df_sal_min_max = df_sal_min_max.rename(columns={'Salary Range From': 'Salario Minimo', 'Salary Range To': 'Salario Maximo'})

    trained_model = entrenar_modelo_lineal(df_sal_min_max, "Salario Minimo", "Salario Maximo")

    new_data = pd.DataFrame({"Salario Minimo": [10000, 20000, 1000]})

    predictions = hacer_prediccion(trained_model, new_data)
    print(predictions)

    df_sal_min_max.plot(x="Salario Minimo", y="Salario Maximo", kind='scatter')
    plt.plot(df_sal_min_max["Salario Minimo"], trained_model.predict(sm.add_constant(df_sal_min_max["Salario Minimo"])), color='red', label='Regresión Lineal')
    plt.scatter(new_data["Salario Minimo"], predictions, color='green', label='Predicciones')
    plt.legend()
    plt.savefig(f'imagenes/RegresionLineal_Predicciones.png')
    plt.show()

generar_regresion_lineal()