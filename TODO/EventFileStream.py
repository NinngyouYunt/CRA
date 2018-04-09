from TODO.Event import Event
import os


# Return a list of Event
class EventFileStream:
    def __init__(self):
        self.storageRoot = os.path.dirname(__file__) + "/storage"
        self.events = []
        # read all files
        for filename in os.listdir(self.storageRoot):
            self.events = self.events + self.read_file(self, os.path.join(self.storageRoot, filename))

    @staticmethod
    def read_file(self, path):
        total_line = len(Event.contentTuple) + 1
        file_content = list(map(lambda item: item[:len(item)-1],
                                open(path, "r").readlines()))
        events = []
        for i in range(int(len(file_content) / total_line)):
            params = file_content[i * total_line:i * total_line + total_line][:total_line-1]
            # Priority
            params[2] = int(params[2])
            # Date
            params[3] = list(map(lambda x:int(x), params[3].split("/")))
            # Time
            params[4] = list(map(lambda x:int(x), params[4].split(":")))
            # isDone
            params[5] = params[5] == "True"
            # isLate
            params[6] = params[6] == "True"
            events.append(Event(*params))
            # TEST_USE
            print(params)
        return events
