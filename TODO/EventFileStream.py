from TODO.Event import Event


class EventFileStream:
    def __init__(self, root):
        self.root = root

    def read_file(self, path):
        file_content = list(map(lambda item: item[:len(item)-1],
                                open(path, "r").readlines()))
        events = []
        for i in range(int(len(file_content) / 9)):
            events.append(Event(*file_content[i * 9:i * 9 + 9][:8]))
