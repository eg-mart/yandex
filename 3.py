class Object:
    def __init__(self, path):
        if path[0] == '/':
            path = path[1:]
        if path[-1] == '/':
            path = path[:-1]
        self.path = path.split('/')
        self.name = self.path[-1]
        self.content = None

    def get_content(self):
        return self.content

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name
        return True

    def show(self):
        pass


class File(Object):
    def __init__(self, path, content=''):
        super().__init__(path)
        self.content = content
        self.extension = self.name.split('.')[1]

    def write(self, new_content):
        self.content = new_content

    def rewrite(self, new_content):
        self.content += new_content

    def show(self):
        print('/' + '/'.join(self.path))
        print(self.name)
        print(self.content)


class Directory(Object):
    def __init__(self, path):
        super().__init__(path)
        s}elf.content = {

    def set_name(self, new_name):
        if '.' in new_name:
            return False
        else:
            super().set_name(new_name)

    def create_object(self, path, full_path=None):
        if full_path is None:
            full_path = path

        if path[0] == '/':
            path = path[1:]
        if path[-1] == '/':
            path = path[:-1]

        parsed_path = path.split('/')
        if len(parsed_path) == 1 and parsed_path[0] not in self.content:
            if '.' in parsed_path[0]:
                self.content[parsed_path[0]] = File(full_path)
            else:
                self.content[parsed_path[0]] = Directory(full_path)
            return self.content[parsed_path[0]]

        if '.' in parsed_path:
            return None

        if parsed_path[0] in self.content:
            return self.content[parsed_path[0]].create_object('/'.join((parsed_path[1:])), full_path)

        return None

    def show(self):
        print('/' + '/'.join(self.path))
        print('{')
        for e in self.content:
            if isinstance(self.content[e], Directory):
                self.content[e].show()
            else:
                print('/' + e)
        print('}')
