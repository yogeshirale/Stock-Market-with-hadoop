		VISUALIZATION OF STOCK MARKET STRUCTURE USING HADOOP

1.In the project, we are visualiziing the cluster of the company with the same interest. We downloaded the dataset from the Yahoo! Finance. Dataset contains open and close values of stock market.

2. The project runs in three parts. THe first part contains storing the dataset from the server onto the data.csv file. This is done by using the part1.py python program.

3. The second part is the mapper.py and reducer.py program. It is implemented on hadoop.
>>> hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streamiheng*.jar -file mapper.py -mapper 'python mapper.py' -file reducer.py   -reducer 'python reducer.py' -input /user/input/data.csv -output /user/output 

4. The third part contains plotting of the Graph using the output file part-00000 generated using hadoop framework.
