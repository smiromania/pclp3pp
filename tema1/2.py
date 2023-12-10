import pandas as pd
import matplotlib.pyplot as plt


file_path = 'data.csv'  

data = pd.read_csv(file_path)

data.plot(title='Toate Valorile')
plt.show()

X = 6
data.head(X).plot(title=f'Primele {X} Valori')
plt.show()

Y = 11
data[['Durata', 'Puls']].tail(Y).plot(title=f'Ultimele {Y} Valori pentru Durata și Puls')
plt.show()
