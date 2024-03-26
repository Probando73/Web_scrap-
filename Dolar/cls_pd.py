import pandas as pd


class Frame():
    """
    Clase para leer diferentes tipos de archivos
    """

    def __init__(self, data) -> None:
        """
        Metodo constructor que inicia la clase.
        """

        self.data = data

    def read_csv_file(self,):
        """
        Metodo para leer archivos csv.
        """

        return pd.read_csv(self.data)

    def read_excel_file(self, sheet_name_):
        """
        Metodo para leer archivos xlsx.
        """

        return pd.read_excel(self.data, sheet_name=sheet_name_)

    def order_index(self, data, order=True):
        """
        Metodo para ordenar el indice de una serie o dataframe.
        """

        return data.sort_index(ascending=order)

    def drop_nan(self, data):
        """
        Metodo para eliminar los registros NaN y None.
        """

        return data.dropna()


#################################################################


class Series(Frame):
    """
    Clase para crear y manipular series.
    """

    def __init__(self, data) -> None:
        """
        Metodo constructor que inicia la clase.
        """

        super().__init__(data)

    def create_serie(self):
        """
        Metodo para crear una serie.
        """
        return pd.Series(self.data)

    def order_values_serie(self, data, order=True):
        """
        Metodo para ordenar los valores de una serie
        """

        return data.sort_values(order)

#################################################################


class DataFrame(Series):
    """
    Clase para crear DataFrames.
    """

    def __init__(self, data) -> None:
        """
        Metodo constructor que inicia la clase.
        """

        super().__init__(data)

    def create_DataFrame(self, index_=None, columns_=None):
        """
        Metodo para crear un DataFrame.
        """
        return pd.DataFrame(self.data, index=index_, columns=columns_)

    def columns_name(self, data):
        """
        Metodo que devuelve una lista con los nombres de las columnas del dataframe.
        """

        return data.columns

    def order_values_df(self, data, column_name, order=True):
        """
        Metodo para ordenar los valores de una columna del dataframe, TRUE es creciente  
        y FALSE es decreciente.
        """

        return data.sort_values(column_name, ascending=order)

    def add_column(self, data, new_key, new_values):
        """
        Metodo para agregar una columna a un dataframe, pasando como argumento una serie
        """
        new_column = data[new_key] = new_values
        return new_column

    def delete_df(self, data, column_name):
        """Metodo para eliminar una columna del dataframe"""

        # return data.del[column_name]

    def pop_df(self, data, column_name):
        """
        Metodo para que elimina una columna del dataframe
        y la devuelve como una serie.
        """

        return data.pop(column_name)

    def export_csv(self,):
        """
        Metodo para exportar un DataFrame a un formato CSV.
        """
        pass

    def export_excel(self,):
        """
        Metodo para exportar un DataFrame a un formato xlxs.
        """

        pass


#################################################################
