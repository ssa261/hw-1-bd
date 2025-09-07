import json
import os

class Base:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.data = {}
        self.next_id = 1
        self.Load()
    
    def Save(self):
        with open(self.filename, 'w') as f:
            json.dump({
                'data': self.data,
                'next_id': self.next_id
            }, f)
    
    def Load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    saved_data = json.load(f)
                    self.data = saved_data['data']
                    self.next_id = saved_data['next_id']
            except:
                self.data = {}
                self.next_id = 1
    
    def Push(self, item):
        item_id = self.next_id
        self.data[item_id] = item
        self.next_id += 1
        self.Save()
        return item_id
    
    def Get(self, item_id):
        item_id = int(item_id)
        if item_id in self.data:
            return self.data[item_id]
        return None
    
    def Update(self, item_id, new_data):
        item_id = int(item_id)
        if item_id in self.data:
            self.data[item_id] = new_data
            self.Save()
            return True
        return False
    
    def Delete(self, item_id):
        item_id = int(item_id)
        if item_id in self.data:
            del self.data[item_id]
            self.Save()
            return True
        return False
    
    def GetAll(self):
        return self.data
