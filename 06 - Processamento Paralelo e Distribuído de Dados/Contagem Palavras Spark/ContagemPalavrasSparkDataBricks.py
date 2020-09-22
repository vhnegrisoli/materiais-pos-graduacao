# Obs.: Esse script só rodará dentro do ambiente do DataBricks

from pyspark import SparkConf, SparkContext
from StopWords import allStopWords

print(allStopWords)

# Configurações padrões, não aplicável ao DataBricks
conf = SparkConf().set("spark.python.profile", "true")
sc = SparkContext('local', 'test', conf = conf, profiler_cls = MyCustomProfiler)

tokenized = sc.textFile('/FileStore/tables/PrideandPrejudice.txt') \
	.flatMap(lambda line: line.split(" "))

# Contar a ocorrência das palavras com alguns tratamentos
wordCounts = tokenized \
	.map(lambda x: x.replace(',', ' ').replace('.', ' ').replace('-', '').lower()) \
    .flatMap(lambda x: x.split()) \
    .filter(lambda x: x not in allStopWords) \
    .map(lambda x: (x, 1)) \
    .reduceByKey(lambda x, y: x+y) \
    .map(lambda x: (x[1], x[0])) \
    .sortByKey(False)

print(wordCounts.cache())
print(wordCounts.count())
print(wordCounts.take(10))
