# run a simple hadoop streaming task
- local data test: cat demodata | python mapper.py | python reduce.py
- run online with hdfs data: nohup sh run.sh & 
