import matplotlib.pyplot as plt #alias o sinonimo para usarla mas rapido

def bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def pie_chart(labels, values):
  fig, ax = plt.subplots() #esas variables las da la libreria fig(figura) ax(coordenadas)
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 245, 1100]
  #bar_chart(labels, values)
  pie_chart(labels, values)