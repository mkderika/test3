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

# Вопрос 4

last_str = len(df)
october = df.iloc[df[df['status'] == 'Октябрь 2021'].index[0]:last_str]

new_count = october['new/current'].value_counts()['новая']
current_count = october['new/current'].value_counts()['текущая']

print('\nВопрос 4')

if new_count > current_count:
    print('В октябре 2021 преобладает тип сделок "новая"')
elif current_count > new_count:
    print('В октябре 2021 преобладает тип сделок "текущая"')
else:
    print('В октябре 2021 преобладает равное значение типа сделок "новая" и "текущая"')

# Вопрос 5

may = df.iloc[df[df['status'] == 'Май 2021'].index[0] + 2:
               df[df['status'] == 'Июнь 2021'].index[0]]


received_in_june = may.loc[(pd.to_datetime(may['receiving_date']) >= '2021-06-01') &
                           (pd.to_datetime(may['receiving_date']) <= '2021-06-30')]
print('\nВопрос 5')
print('В июне 2021 было получено', received_in_june['document'].value_counts()['оригинал'], 'оригиналов договоров по майским сделкам')

