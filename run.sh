#!/bin/sh

source ./common.sh

begin_date=`date -d "20 days ago" +%Y%m%d`
end_date=`date -d today +%Y%m%d`
# run 20 days
while [ $begin_date != $end_date ]
do
	date=$begin_date
	INPUT=/app/input_path_$date
	OUTPUT=/app/output_path_$date
	hadoop fs -rmr ${OUTPUT}

	hadoop streaming \
		-jobconf mapred.job.name="lengdong_yuetu_$date" \
		-jobconf mapred.map.tasks=1000  \
		-jobconf mapred.reduce.tasks=1 \
		-jobconf mapred.job.map.capacity=1000 \
		-jobconf mapred.job.reduce.capacity=1 \
		-jobconf mapred.job.priority=${PRIORITY}   \
		-jobconf stream.num.map.output.key.fields=1 \
		-jobconf num.key.fields.for.partition=2  \
		-partitioner  org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner  \
		-input ${INPUT} \
		-output  ${OUTPUT}\
		-mapper "python mapper.py" \
		-reducer "python reduce.py" \
		-file mapper.py \
		-file reduce.py 

	hadoop fs -getmerge ${OUTPUT} data/$date.txt
	begin_date=`date -d "+1 day $begin_date" +%Y%m%d`
done
