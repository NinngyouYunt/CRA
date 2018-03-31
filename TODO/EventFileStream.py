from TODO.Event import Event
import os


class EventFileStream:
    def __init__(self):
        self.storageRoot = os.path.dirname(__file__) + "/storage"
        self.events = []
        for filename in os.listdir(self.storageRoot):
            self.events = self.events + self.read_file(self, os.path.join(self.storageRoot, filename))

        for event in self.events:
            print(str(event))

    @staticmethod
    def read_file(self, path):
        file_content = list(map(lambda item: item[:len(item)-1],
                                open(path, "r").readlines()))
        events = []
        for i in range(int(len(file_content) / 9)):
            events.append(Event(*file_content[i * 9:i * 9 + 9][:8]))
        return events
