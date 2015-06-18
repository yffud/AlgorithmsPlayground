#!/bin/bash

while true
do
  echo "Connecting to RTC";
  X=$(/opt/IBM/TeamConcert/scmtools/eclipse/lscm status -v -B | tac | grep '(' | grep '\$' | sed 's/^[ \t]*//' | sed 's/)//' | sed 's/(//' | awk '{print $1 }')

  for y in $(echo $X | tr " " "\n")
   do
        RTCACCEPT="";
        GITMESSAGE="";
        STATUS="";
        COMMIT="";
        PUSH="";
        echo "RTC"$y;
        RTCACCEPT=$(/opt/IBM/TeamConcert/scmtools/eclipse/lscm accept -c $y 2>&1);
        echo "RTCACCEPT"$RTCACCEPT"RTCACCEPT";
        GITMESSAGE=$(echo $RTCACCEPT);
        #GITMESSAGE=$(echo $RTCACCEPT | grep -v Repository: | grep -v Workspace: | grep -v Component:);
        echo $GITMESSAGE;
        STATUS=$(git add *);
        echo $STATUS;
        #COMMIT=$(echo $GITMESSAGE | git commit -a --author="John Washburn <jwashburn@bb-elec.com>" --file -);
        COMMIT=$(echo $GITMESSAGE | git commit -a --file -);
        echo $COMMIT;
        PUSH=$(git push);
        echo $PUSH;
        # Use break to only run a single cycle
        #break

        #echo "/opt/IBM/TeamConcert/scmtools/eclipse/lscm accept -c $y";
        #echo "git add *";
        #echo "git commit -a";
  done

  now=$(date +"%T")
  echo "$now No pending commits";

  echo "Sleeping for 60 s"
  sleep 60

done
