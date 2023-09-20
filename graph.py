import pandas as pd
import matplotlib.pyplot as plt

file = 'data2.xlsx'
df = pd.read_excel(file, sheet_name='Лист1')
last_str = len(df)


may = df.iloc[df[df['status'] == 'Май 2021'].index[0] + 2:
               df[df['status'] == 'Июнь 2021'].index[0]]
sum_may = may[may['status'] == 'ОПЛАЧЕНО']['sum'].sum().round(2)

june = df.iloc[df[df['status'] == 'Июнь 2021'].index[0]:
               df[df['status'] == 'Июль 2021'].index[0]]
sum_june = june[june['status'] == 'ОПЛАЧЕНО']['sum'].sum().round(2)

july = df.iloc[df[df['status'] == 'Июль 2021'].index[0]:
               df[df['status'] == 'Август 2021'].index[0]]
sum_july = july[july['status'] == 'ОПЛАЧЕНО']['sum'].sum().round(2)

august = df.iloc[df[df['status'] == 'Август 2021'].index[0]:
               df[df['status'] == 'Сентябрь 2021'].index[0]]
sum_august = august[august['status'] == 'ОПЛАЧЕНО']['sum'].sum().round(2)

september = df.iloc[df[df['status'] == 'Сентябрь 2021'].index[0]:
               df[df['status'] == 'Октябрь 2021'].index[0]]
sum_september = september[september['status'] == 'ОПЛАЧЕНО']['sum'].sum().round(2)

october = df.iloc[df[df['status'] == 'Октябрь 2021'].index[0]:last_str]
sum_october = october[october['status'] == 'ОПЛАЧЕНО']['sum'].sum().round(2)

months = ['Май 2021', 'Июнь 2021', 'Июль 2021', 'Август 2021', 'Сентябрь 2021', 'Октябрь 2021']
revenues = [sum_may, sum_june, sum_july, sum_august, sum_september, sum_october]

plt.figure(figsize=(10,5))
plt.bar(months, revenues)
plt.title('Изменение выручки компании')
plt.ylabel('Выручка, руб.')

plt.show()

