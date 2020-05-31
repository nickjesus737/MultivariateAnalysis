from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo
import pandas as pd 
import numpy as np
import io


class AnalisisFactorialServicio:

    def ejecutar(self, estudio):
        
        n_componentes = estudio.numero_componenentes
        calcular_n_componentes = False if n_componentes else True
        rotacion = estudio.rotacion
        data = estudio.archivo_datos
        df = pd.read_csv(io.StringIO(data.read().decode('utf-8')), delimiter=',')

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



        


        


