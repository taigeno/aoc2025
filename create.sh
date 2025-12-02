DAY=$1
DIRNAME="Day$DAY"

mkdir $DIRNAME
cp template.py $DIRNAME/day$DAY.py
touch $DIRNAME/test.txt
touch $DIRNAME/input.txt