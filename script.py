money = int(input("Enter sum:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for value in per_cent.values():
   result = int(money / 100 * value)
   deposit.append(money*per_cent['ТКБ']/100)
   deposit.append(money*per_cent['СКБ']/100)
   deposit.append(money*per_cent['ВТБ']/100)
   deposit.append(money*per_cent['СБЕР']/100)
print("Максимальная сумма, которую вы сможете заработать:")
print(max(deposit))
