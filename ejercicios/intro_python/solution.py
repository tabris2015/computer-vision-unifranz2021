estudiantes = [
    {
        'nombre': 'juan',
        'apellido': 'perez',
        'notas': {
            'MAT': 30,
            'QMC': 30,
            'FIS': 30,
            'LAB': 30
        },
        'extras': [2, 3, 1, 1, 1],
        'asistencia': 90
    },
    {
        'nombre': 'ANA',
        'apellido': 'rivera',
        'notas': {
            'MAT': 98,
            'QMC': 98,
            'FIS': 98,
            'LAB': 98
        },
        'extras': [1, 2, 3],
        'asistencia': 100
    }
]


class Evaluador:
    """Esta clase implementa diversas funciones para calcular promedios
    de una lista de estudiantes y obtener otros datos adicionales, ademas,
    tambien implementa una funcion para escribir un reporte de notas"""
    def __init__(self, lista_estudiantes, min_asistencia, max_extras):
        self.lista_estudiantes = lista_estudiantes
        self.min_asistencia = min_asistencia
        self.max_extras = max_extras

    def calcular_promedios(self):
        lista_notas = []
        for estudiante in self.lista_estudiantes:
            estudiante_dic = {
                'nombre completo': f'{estudiante["nombre"].capitalize()} {estudiante["apellido"].capitalize()}'
            }

            if estudiante.get('notas') is None or estudiante['notas'] == {} or estudiante['asistencia'] < self.min_asistencia:
                estudiante_dic['promedio'] = 0
                lista_notas.append(estudiante_dic)
                continue
            
            promedio_materias = sum([nota for nota in estudiante['notas'].values()]) / len(estudiante['notas'])
            promedio_materias += sum(estudiante['extras']) if sum(estudiante['extras']) <= self.max_extras else self.max_extras
            if promedio_materias > 100:
                promedio_materias = 100

            estudiante_dic['promedio'] = promedio_materias
            lista_notas.append(estudiante_dic)
        return lista_notas

    def obtener_mejor_estudiante(self):
        return max(self.calcular_promedios(), key=lambda estudiante: estudiante['promedio'])

    def salvar_datos(self, nombre_archivo):
        print('salvando datos')
        with open(nombre_archivo, 'w') as archivo:
            # cabecera
            data_str = 'Nombre Completo,Asistencia,MAT,FIS,QMC,LAB,Total Extras,Promedio Final,Observacion\n'
            for est_data, est_final in zip(self.lista_estudiantes, self.calcular_promedios()):
                if est_data.get('notas') is None or est_data['notas'] == {}:
                    continue
                est_str = f'{est_final["nombre completo"]},{est_data["asistencia"]},'
                est_str += f'{est_data["notas"]["MAT"]},{est_data["notas"]["FIS"]},{est_data["notas"]["QMC"]},{est_data["notas"]["LAB"]},'
                est_str += f'{sum(est_data["extras"]) if sum(est_data["extras"]) <= self.max_extras else self.max_extras},{est_final["promedio"]},'
                est_str += f'{"APROBADO" if est_final["promedio"] > 50 else "REPROBADO"}\n'

                data_str += est_str

            archivo.write(data_str)
        print(f'datos guardados en {nombre_archivo}')


if __name__ == '__main__':
    evaluador = Evaluador(lista_estudiantes=estudiantes, min_asistencia=80, max_extras=5)
    notas = evaluador.calcular_promedios()
    print(f'Notas: {notas}')
    mejor = evaluador.obtener_mejor_estudiante()
    print(f'Mejor estudiante: {mejor}')
    evaluador.salvar_datos('ejemplo_notas.csv')
