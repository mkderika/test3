import pandas as pd

file = 'data.xlsx'
df = pd.read_excel(file, sheet_name='Лист1')

# Вопрос 1

july = df.iloc[df[df['status'] == 'Июль 2021'].index[0]:
               df[df['status'] == 'Август 2021'].index[0]]

total_rev_july = july[july['status'] == 'ОПЛАЧЕНО']['sum'].sum()

print('Вопрос 1')
print('Общая выручка за июль 2021 года по тем сделкам, приход денежных средств которых не просрочен:', round(total_rev_july, 2))

# Вопрос 3

best_manager_september = (df.iloc[df[df['status'] == 'Сентябрь 2021'].index[0]:
            df[df['status'] == 'Октябрь 2021'].index[0]].groupby(['sale'])['sum'].sum().reset_index().
            sort_values(by='sum', ascending=False))

print('\nВопрос 3')
print('Менеджер, который привлек больше всего денежных средств в сентябре 2021 -', best_manager_september.loc[0, 'sale'])
