import collection.crawler as cw

result = cw.crawling(
    url='http://movie.naver.com/movie/sdb/rank/rmovie.nhn',
    encoding='cp949')

print(result)

