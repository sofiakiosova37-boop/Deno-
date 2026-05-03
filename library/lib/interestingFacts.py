import csv
from operator import itemgetter

class Priority:
    def __init__(self):
        self.data = []
        self.priority = []
        self._counter = 0
        self.time = []

    def enqueue(self, name, info, distance):
        self._counter += 1
        fact={
            "name": name,
            "info": info,
            "distance": distance,
            "id": self._counter
        }
        self.data.append(fact)
        self.time.append(fact)
       # self.priority.append(fact)
       # self.data.sort(key=itemgetter('distance', 'id'))
    
        index = len(self.priority)
        for i in range (len(self.priority)):
            if fact['distance'] < self.priority[i]['distance']:
                index = i
                break
        self.priority.insert(index, fact)

    def streamcsv(self, file_path):
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                fact = {
                    "id": int(row['id']),
                    "name": row['name'],
                    "distance": float(row['distance']),
                    "info": row['info']
                }
                yield fact

    def process_large_data(self, file_path, max_dist=1000):
        for fact in self.streamcsv(file_path):
            if fact['distance'] <= max_dist:
                print(f"Знайдено в потоці: {fact['name']} — {fact['distance']} св. р.")

    def get_sorted_list(self, order='nearest'):
        if order == 'nearest':
            return self.priority
        elif order == 'farthest':
            return self.priority[::-1]
        elif order == 'newest':
            return sorted(self.data, key=itemgetter('id'), reverse=True)
        else:
            return self.data

    def get_nearest(self):
        if len(self.data) > 0:
            return self.data[0]    
        else:                        
            return None
    
    def get_farthest(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
         return None

    def get_oldest(self):
        if len(self.data) > 0:
            result = min(self.data, key=itemgetter('id'))
            return result
        else:
            return None
    
    def display(self):
        print(f"\n--- СПИСОК ФАКТІВ (Завантажено: {len(self.data)}) ---")
        for item in self.data:
            print(f"ID:{item['id']} | {item['name']} — {item['distance']} св. р.")

queue = Priority()
try:
    queue.process_large_data('facts.csv', max_dist=10000)
except FileNotFoundError:
    print("\n[!] Файл facts.csv не знайдено")

