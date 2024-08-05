import random
import json

class Schemas:
    def __init__(self, filename):
        self.names = []
        self.used_schemas = []
        self.num_calls = 0
        self.filename = filename
        self.load_used_names()

    def add_schemas(self, *names):
        self.names.extend(names)

    def get_random_name(self):
        if self.num_calls == len(self.names) * 2:
            # all names have been used twice, reset the lists
            self.used_schemas = []
            self.names = []
            self.num_calls = 0
        if not self.names:
            # all names have been used and the list is empty
            return "No more schemas"
        if not self.used_schemas:
            # first call, initialize used_names list
            self.used_schemas = []
        unused_schemas = [name for name in self.names if name not in self.used_schemas]
        if not unused_schemas:
            # all names have been used, reset the used_names list
            self.used_schemas = []
            unused_schemas = self.names
        name = random.choice(unused_schemas)
        self.used_schemas.append(name)
        self.num_calls += 1
        self.save_used_schemas()
        return name
    
    def load_used_names(self):
        try:
            with open(self.filename) as f:
                self.used_schemas = json.load(f)
        except FileNotFoundError:
            pass
        
    def save_used_schemas(self):
        with open(self.filename, 'w') as f:
            json.dump(self.used_schemas, f)

    def schema_list(self):


        return schemas.get_random_name()

schemas = Schemas('used_names.json')
