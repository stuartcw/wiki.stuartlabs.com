BACKUP_FILE_DATE=`date -r quotes.csv "+%m-%d-%Y_%H_%M_%S"`
mv quotes.csv quotes_$BACKUP_FILE_DATE."csv"
curl https://gist.githubusercontent.com/JakubPetriska/060958fd744ca34f099e947cd080b540/raw/963b5a9355f04741239407320ac973a6096cd7b6/quotes.csv -o quotes.csv
rm quotes.json
