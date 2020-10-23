while true
do
    if [ "$(date +"%s")" == "$(date --date="04:20" +"%s")" ]
    then
        python3 ./venv/updateUSA.py
    fi
    if [ "$(date +"%s")" == "$(date --date="16:20" +"%s")" ]
    then	    
        python3 ./venv/updateHK.py
    fi
sleep 1
done
~      
