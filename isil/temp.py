  "date": row["eventDate"],
            "artist": (row["artist"])["name"],
            "venue": (row["venue"])["name"],
            "city": ((row["venue"])["city"])["name"],
            "state": ((row["venue"])["city"])["stateCode"]




        milestones = []

        mile = 0
        elapsedTime = 0
        # For each mile, add (pace * mile #) to calculate elapsed time
        for i in range(27):
            elapsedTime = mile*pace
            milestones.append(elapsedTime)
            mile += 1
        
        pointTwo = pace * .2188
        elapsedTime += int(pointTwo)
        milestones.append(elapsedTime)

        print(milestones)

        for mile in milestones:
            duration = elapsedTime + startTimeSec


        for y in milestones:
            duration = str(datetime.timedelta(duration))

        print(duration)
        print(milestones)
