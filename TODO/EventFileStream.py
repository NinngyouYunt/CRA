from TODO.Event import Event
import os


# Return a list of Event
class EventFileStream:
    instance = None

    def __init__(self):
        self.storageRoot = os.path.dirname(__file__) + "/storage"

    def read_all_file(self):
        events = []
        for filename in os.listdir(self.storageRoot):
            if filename.find("_") != -1:
                events = events + self.read_file(filename)
        return events

    def read_file(self, filename):
        path = os.path.join(self.storageRoot, filename)
        total_line = len(Event.contentTuple) + 1
        file_content = list(map(lambda item: item[:len(item) - 1],
                                open(path, "r").readlines()))
        events = []
        for i in range(int(len(file_content) / total_line)):
            params = file_content[i * total_line:i * total_line + total_line][:total_line - 1]
            # Priority
            params[2] = int(params[2])
            # Date
            if params[3] != "":
                params[3] = list(map(lambda x: int(x), params[3].split("/")))
            # Time
            if params[4] != "":
                params[4] = list(map(lambda x: int(x), params[4].split(":")))
            # isDone
            params[5] = params[5] == "True"
            # isLate
            params[6] = params[6] == "True"
            events.append(Event(*params))
            # TEST_USE
            print(params)
        return events

    def save_file(self, filename, events):
        path = self.get_path(filename+".temp")
        file = open(path, "w")
        for event in events:
            file.write(event.get_saving_string()+"\nEND\n")
        file.close()
        os.replace(self.get_path(filename+".temp"), self.get_path(filename))

    def get_path(self, filename):
        return os.path.join(self.storageRoot, filename)

    @staticmethod
    def get_instance():
        if EventFileStream.instance is None:
            EventFileStream.instance = EventFileStream()
        return EventFileStream.instance
