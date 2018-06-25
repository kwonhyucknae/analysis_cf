import pandas as pd

# pelicana
pelicana_table = pd.DataFrame.from_csv(
    '__result__/crawling/pelicana_table.csv',
    encoding='utf-8',
    index_col=1,
    header=0).fillna('')


pelicana_table = pelicana_table[pelicana_table.sido != '']
pelicana_table = pelicana_table[pelicana_table.gungu != '']

# 전체 매장수
df = pelicana_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis=1)
print(df.value_counts())

# nene


# kyochon


# goobne
