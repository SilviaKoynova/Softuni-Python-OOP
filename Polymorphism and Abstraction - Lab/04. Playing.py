def start_playing(obj):
    return obj.play()


class Children:
    def play(self):
        return "Children are playing"


class Guitar:
    def play(self):
        return "Playing the guitar"


# guitar = Guitar()
# start_playing(guitar)
piano = Children()
start_playing(piano)

