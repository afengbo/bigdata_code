
HADOOP_CMD="/usr/local/src/hadoop-2.6.1/bin/hadoop"
STREAM_JAR_PATH="/usr/local/src/hadoop-2.6.1/share/hadoop/tools/lib/hadoop-streaming-2.6.1.jar"

INPUT_FILE_PATH_1="/data/The_Man_of_Property.txt"
#INPUT_FILE_PATH_1="/data/1.data"
OUTPUT_PATH="/output/wc"

#$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_PATH

# Step 1.
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_PATH \
    -mapper "python map_t.py" \
    -reducer "python red_t.py" \
    -file ./map_t.py \
    -file ./red_t.py
