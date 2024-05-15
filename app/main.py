import utils
import read_csv
import charts

'''def run():
  data = read_csv.read_csv('./app/data.csv')
  country = input('Escribe el pais: ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.bar_chart(labels, values)
  
  print(result) '''

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America', data))
  
  countries = list(map(lambda x: x['Country/Territory'], data))
  porcentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.pie_chart(countries,porcentages)

  country = input('Escribe el pais: ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.bar_chart(country['Country/Territory'], labels, values)

if __name__ == '__main__':
  run()

'''ese if dice al archivo main.py qie si es ejecutado desde la terminal, ejecute el metodo run(),
si main.py es ejecutado desde otro archaivo por ejemplo example.py, ese run() no se va a ejecutar'''

'''lo anterior es apra poder llamar main.py desde la terminal y desde example.py, desde ambos, llamado dualidad'''