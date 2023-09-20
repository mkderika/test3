import pandas as pd

file = 'data.xlsx'
df = pd.read_excel(file, sheet_name='Лист1')
last_str = len(df)

# делаем срез по договорам, заключенным до 1 июля
period = df.iloc[df[df['status'] == 'Май 2021'].index[0] + 2:
               df[df['status'] == 'Июль 2021'].index[0]]

# берем только те записи, оригиналы по которым пришли после 1 июля, и которые не имеют статус ПРОСРОЧЕНО
july_remains = period.loc[(pd.to_datetime(period['receiving_date']) >= '2021-07-01')]\
                .loc[period['status'] != 'ПРОСРОЧЕНО']\
                .loc[period['document'] == 'оригинал']

# делаем датафрейм с данными по бонусам менеджерам за договора со статусом "новый"
new_deals = july_remains.loc[july_remains['new/current'] == 'новая'].loc[july_remains['status'] == 'ОПЛАЧЕНО']
new_deals.insert(len(new_deals.columns), 'bonus', new_deals['sum'] / 100 * 7)
new_deals_manager = new_deals.groupby(['sale'])['bonus'].sum().round(2).reset_index()

# делаем датафрейм с данными по бонусам менеджерам за договора со статусом "текущий"
current_deals = july_remains.loc[july_remains['new/current'] == 'текущая']

# делаем датафрейм с данными по бонусам менеджерам за договора со статусом "текущий" c договорами больше 10к
more_ten_k = current_deals.loc[current_deals['sum'] >= 10000]
more_ten_k.insert(len(current_deals.columns), 'bonus', current_deals['sum'] / 100 * 5 )
more_ten_k_manager = more_ten_k.groupby(['sale'])['bonus'].sum().round(2).reset_index()

# делаем датафрейм с данными по бонусам менеджерам за договора со статусом "текущий" c договорами меньше 10к
less_ten_k = current_deals.loc[current_deals['sum'] < 10000]
less_ten_k.insert(len(current_deals.columns), 'bonus', current_deals['sum'] / 100 * 3 )
less_ten_k_manager = less_ten_k.groupby(['sale'])['bonus'].sum().round(2).reset_index()

# объединяем ранее полученные датафреймы и группируем по менеджеру
frames = [new_deals_manager, more_ten_k_manager, less_ten_k_manager]
final_bonuses = pd.concat(frames).groupby(['sale'])['bonus'].sum().round(2).reset_index()

print(final_bonuses)