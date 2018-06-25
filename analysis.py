import pandas as pd

# pelicana
pelicana_table = pd.DataFrame.from_csv(
    '__result__/crawling/pelicana_table.csv',
    encoding='utf-8',
    index_col=0,
    header=0).fillna('')


pelicana_table = pelicana_table[pelicana_table.sido != '']
pelicana_table = pelicana_table[pelicana_table.gungu != '']

# 전체 매장수

#sido gundo 별 매장수

pelicana=pelicana_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis=1).value_counts()
print(pelicana)
#s2=pelicana.value_counts()
#print(s2)


# nene
nene_table = pd.DataFrame.from_csv(
    '__result__/crawling/nene_table.csv',
    encoding='utf-8',
    index_col=0,
    header=0).fillna('')

nene_table = nene_table[nene_table.sido != '']
nene_table = nene_table[nene_table.gungu != '']
nene = nene_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis=1).value_counts() # 'SIDO GUNGU' 별 매장수
# print(nene)

# kyochon
kyochon_table = pd.DataFrame.from_csv(
    '__result__/crawling/kyochon_table.csv',
    encoding='utf-8',
    index_col=0,
    header=0).fillna('')

kyochon_table = kyochon_table[kyochon_table.sido != '']
kyochon_table = kyochon_table[kyochon_table.gungu != '']
kyochon = kyochon_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis=1).value_counts() # 'SIDO GUNGU' 별 매장수
# print(kyochon)

# goobne
goobne_table = pd.DataFrame.from_csv(
    '__result__/crawling/goobne_table.csv',
    encoding='utf-8',
    index_col=0,
    header=0).fillna('')

goobne_table = goobne_table[goobne_table.sido != '']
goobne_table = goobne_table[goobne_table.gungu != '']
goobne = goobne_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis=1).value_counts() # 'SIDO GUNGU' 별 매장수
#print(goobne)


merge_dict={'pelicana':pelicana,'nene':nene,'kyochon':kyochon,'goobne':goobne}
pd.DataFrame(merge_dict)



