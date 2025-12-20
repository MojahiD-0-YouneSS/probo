
class Base5Collector:
    def __init__(self):
        self.classes = []

    def __getattr__(self, key):
        # Parse key like container_xxl → container-xxl
        dash = key.replace("_", "-")
        self.classes.append(dash)
        return self

    def __str__(self):
        return " ".join(self.classes)

    
