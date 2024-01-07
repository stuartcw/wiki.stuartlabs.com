# Keybase Chat API 

Some code which listens to all the messages that you receive and if they contain a certain string, repeats back the message. Each message that is heard is logged as JSON.

```bash
#!/bin/bash

CHAT_NAME="test"
TEAM_NAME="your_team_name"

keybase chat api-listen | while read L; do
{
    OUTPUT_FILENAME=`date '+%Y-%m-%d %H:%M:%S.json'`
    echo $OUTPUT_FILENAME
    echo $L | jq . > "$OUTPUT_FILENAME"
    OUT=$(jq --raw-output 'select(.type == "chat")|select(.msg.content.text.body|startswith("!stubot "))| .msg.content.text.body | "*" + ltrimstr("!arnie ") + "*"' <<< "$L")
    if [ "${OUT}" != "" ]; then
    {
        echo "OUT is ${OUT}"
        OUT=`echo ${OUT} | sed 's/!stubot//g'`
        OUT="You said: ${OUT}"
        JSON='{ "method": "send", "params":  {"options": {"channel": {"name": "'${TEAM_NAME}'", "members_type": "team", "topic_type": "chat", "topic_name": "'${CHAT_NAME}'" } , "message": {"body":"'${OUT}'"} } } }'
        echo $JSON > json.txt
        echo $JSON | keybase chat api
    }; fi
}; done
```
