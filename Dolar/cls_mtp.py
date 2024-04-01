#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np


class Graphics():
    """
    Clase para crear diferentes tipos de graficos. 
    """

    def __init__(self,):
        """
        Metodo constructor que inicia la clase.
        """

        fig, self.ax = plt.subplots()
        # self.data = data

    def scatter(self, data_x, data_y, line_color='black', marker_type=None, title="Sin titulo", alignment='center', axis_x_title=None, axis_y_title=None, label_name='Sin asignar', legend='upper right'):
        """
        Metodo para crear graficos de dispersion.
        """

        scatter = self.ax.scatter(
            x=data_x, y=data_y, color=line_color, marker=marker_type, label=label_name)
        self.texts(title, alignment, axis_x_title, axis_y_title, legend)
        return scatter

    def plot(self, data_x, data_y, line_color='black', marker_type=None, line_type='solid', title='Sin titulo', alignment='center', axis_x_title=None, axis_y_title=None, label_name='Sin asignar', legend=None):
        """
        Metodo para crear graficos de lineas.
        """

        plot = self.ax.plot(data_x, data_y, color=line_color,
                            marker=marker_type, linestyle=line_type, label=label_name)
        self.texts(title, alignment, axis_x_title, axis_y_title, legend)
        return plot

    def fill_between(self, data_x, data_y, line_color='black', title="Sin titulo", alignment='center', axis_x_title=None, axis_y_title=None, label_name='Sin asignar', legend='upper right'):
        """
        Metodo para crear graficos de area.
        """

        between = self.ax.fill_between(
            data_x, data_y, color=line_color, label=label_name)
        self.texts(title, alignment, axis_x_title, axis_y_title, legend)
        return between

    def bar_v(self, data_x, data_y, line_color='black', title="Sin titulo", alignment='center', axis_x_title=None, axis_y_title=None, label_name='Sin asignar', legend='upper right'):
        """
        Metodo para crear graficos de barras verticales.
        """

        bar = self.ax.bar(data_x, data_y, color=line_color, label=label_name)
        self.texts(title, alignment, axis_x_title, axis_y_title, legend)
        return bar

    def bar_h(self, data_x, data_y, line_color='black', title="Sin titulo", alignment='center', axis_x_title=None, axis_y_title=None, label_name='Sin asignar', legend='upper right'):
        """
        Metodo para crear graficos de barras horizontales.
        """

        bar_h = self.ax.barh(
            data_x, data_y, color=line_color, label=label_name)
        self.texts(title, alignment, axis_x_title, axis_y_title, legend)
        return bar_h

    def hist(self, data_x, data_y, line_color='black', title="Sin titulo", alignment='center', axis_x_title=None, axis_y_title=None, label_name='Sin asignar', legend='upper right'):
        """
        Metodo para crear histogramas.
        """

        hist = self.ax.hist(data_x, data_y, color=line_color, label=label_name)
        self.texts(title, alignment, axis_x_title, axis_y_title, legend)
        return hist

    def pie(self, data_x, labels_names):
        """
        Metodo para crear graficos de torta.
        """

        pie = self.ax.pie(data_x, labels=labels_names, counterclock=False)
        return pie

    def boxplot(self, data_x):
        """
        Metodo para crear diagrama de cajas y bigotes.
        """

        boxplot = self.ax.boxplot(data_x)
        return boxplot

    def imshow(self,):
        # Investigar
        """
        Metodo para crear mapas de color.
        """

        data = np.random.random((6, 8))

        imshow = self.ax.imshow(data)
        return imshow

  ###########################################################

    def texts(self, title, alignment, axis_x_title, axis_y_title, legend):
        """
        Metodo para personalizar: Titulos,Ejes y leyenda.
        """

        self.ax.set_title(title, loc=alignment)
        self.ax.set_xlabel(axis_x_title)
        self.ax.set_ylabel(axis_y_title)
        self.ax.legend(loc=legend)

    def savefig(self, name_figure):
        """
        Metodo para guardar el grafico en formato PNG.
        """

        return plt.savefig(f'{name_figure}.png')

    def show(self,):
        """
        Metodo para mostrar los graficos.
        """

        return plt.show()
