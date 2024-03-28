song_length = 471
beat_total = 400
measure_total = int(beat_total/4)
song_ms  = 0

for x in range(song_length):
    print("(" + str(measure_total) + ", " + str(beat_total) + ", " + str(x + 1) + ", (0, 0, 0, 0, 0), False),")