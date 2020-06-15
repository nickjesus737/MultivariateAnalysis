from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo
import pandas as pd 
import numpy as np
import io
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib
from .models import Estudio
import base64


class AnalisisFactorialServicio:

    def ejecutar(self, estudio_id):
        estudio = Estudio.objects.get(id=estudio_id)

        n_componentes = estudio.numero_componenentes
        calcular_n_componentes = False if n_componentes else True
        rotacion = estudio.rotacion
        data = estudio.archivo_datos
        df = pd.read_csv(io.StringIO(data.read().decode('utf-8')), delimiter=',')
        resultados = {}

        # Remove missing values
        df.dropna(inplace=True)

        # Calculating Bartlett’s Test
        chi_square_value, p_value = calculate_bartlett_sphericity(df)

        # Kaiser-Meyer-Olkin (KMO) Test, < 0.5 the results of the factor analysis probably won’t be very useful.
        kmo_all, kmo_model = calculate_kmo(df)

        # Initalize FactorAnalyzer object
        if calcular_n_componentes:
            analisis_dummy = FactorAnalyzer(df.shape[1], rotacion)
            analisis_dummy.fit(df)
            eigenvalues, _ = analisis_dummy.get_eigenvalues()
            n_componentes = len(list(filter(lambda x: x >= 1, eigenvalues)))
            analisis = FactorAnalyzer(n_componentes, rotacion)
        else:
            analisis = FactorAnalyzer(n_componentes, rotacion)


        # Ejecutar analisis
        analisis.fit(df)

        # Get Matriz de correlacion
        matriz_correlacion = analisis.corr_

        # Get cargas
        cargas = analisis.loadings_

        # Get eigen values
        eigenvalues, _ = analisis.get_eigenvalues()
        
        # Get communalities
        communalities = analisis.get_communalities()

        # Get Factor covariance
        factor_covariance = analisis.get_factor_variance()

        matplotlib.rcParams['figure.figsize'] = (10.0, 6.0)

        style.use('ggplot')

        # Eigenvalues grafica
        plt.scatter(range(1, df.shape[1]+1), eigenvalues)
        plt.plot(range(1, df.shape[1]+1), eigenvalues)
        plt.title('Scree Plot')
        plt.xlabel('Factors')
        plt.ylabel('Eigenvalue')
        plt.axhline(y=1, c='k')
        # Saving images in memory
        grafica_1 = io.BytesIO()
        plt.savefig(grafica_1, format='png')
        grafica_1.seek(0)
        # Encode PNG image to base64 string
        grafica_1B64String = "data:image/png;base64,"
        grafica_1B64String += base64.b64encode(grafica_1.getvalue()).decode('utf8')


        Z = np.abs(analisis.loadings_)
        fig, ax = plt.subplots()
        c = ax.pcolor(Z)
        fig.colorbar(c, ax=ax)
        ax.set_yticks(np.arange(analisis.loadings_.shape[0])+0.5, minor=False)
        ax.set_xticks(np.arange(analisis.loadings_.shape[1])+0.5, minor=False)
        ax.set_yticklabels(df.columns)
        #ax.set_xticklabels(analisis.loadings_.columns.values)
        
        grafica_2 = io.BytesIO()
        plt.savefig(grafica_2, format='png')
        grafica_2.seek(0)
        # Encode PNG image to base64 string
        grafica_2B64String = "data:image/png;base64,"
        grafica_2B64String += base64.b64encode(grafica_2.getvalue()).decode('utf8')


        return {
            'chi_square_value': chi_square_value,
            'kmo_all': kmo_all,
            'kmo_model': kmo_model,
            'matriz_correlacion': matriz_correlacion,
            'cargas': cargas,
            'eigenvalues': eigenvalues,
            'communalities': communalities,
            'factor_covariance': factor_covariance,
            'eigenvalues_graph': grafica_1B64String,
            'cargas_graph': grafica_2B64String
        }

        


        


