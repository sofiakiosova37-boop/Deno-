from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

class Facts:
    def __init__(self, name, discription, distance):
        self.name = name
        self.discription = discription
        self.distance = distance

class Priority:
    def __init__(self):
        self.data = []

    def enqueue(self, item, priority_val):
        self.data.append({"item": item, "priority": priority_val})

    def get_all(self, order="nearest"):
        reverse_sort = True if order == "farthest" else False
        sorted_data = sorted(self.data, key=lambda x: x['priority'], reverse=reverse_sort)
        result = []
        for d in sorted_data:
            item = d['item']
            item['priority'] = d['priority'] 
            result.append(item)
        return result
    
    def display(self):
        print(f"\n--- СПИСОК ФАКТІВ (Завантажено: {len(self.data)}) ---")
        for entry in self.data:
            name = entry['item']['name'] 
            priority = entry['priority']
            print(f"{name}: {priority}")

queue = Priority()
queue.enqueue({"name": "Чорна діра TON 618", "info": "Це одна з наймасивніших чорних дір у Всесвіті. Її маса у 66 мільярдів разів перевищує масу Сонця. Якби вона була в центрі нашої системи, вона б поглинула все аж до орбіти Нептуна."}, 10400000000)
queue.enqueue({"name": "Туманність Стовпи Творіння (Nebula Pillars of Creation)", "info": "Ці гігантські колони з газу та пилу знаходяться в туманності Орел. Найвища «колона» має довжину близько 4 світлових років — це майже відстань від нашого Сонця до найближчої зірки Проксима Центавра."}, 6500)
queue.enqueue({"name": "Планета-алмаз (55 Cancri e)", "info": "Ця планета вдвічі більша за Землю і складається переважно з вуглецю. Через величезний тиск і температуру близько $2400^{\circ}C$, значна частина її маси може перебувати у формі алмазу."}, 40)
queue.enqueue({"name": "Нейтронна зоря (Пульсар)", "info": "Ці об'єкти настільки щільні, що одна чайна ложка речовини нейтронної зорі важила б на Землі близько 1 мільярда тонн (як ціла гора). Вони обертаються сотні разів на секунду, випромінюючи радіосигнали."}, 10000)
queue.enqueue({"name": "Планета-бродяга (Rogue Planet)", "info": "Це планети, які не обертаються навколо жодної зірки. Вони просто дрейфують у повній темряві міжзоряного простору. Вважається, що таких «сиріт» у нашій галактиці може бути навіть більше, ніж зірок."}, 20)
queue.enqueue({"name": "Комета Галлея", "info": "Це єдина комета, яку людина може побачити неозброєним оком двічі за життя. Вона повертається до Землі кожні 75–76 років. Наступна поява очікується у 2061 році"}, 0.0005)
queue.enqueue({"name": "Галактика Сомбреро (M104)", "info": "Вона отримала свою назву через незвичну форму: величезне яскраве ядро та тонку смугу пилу, що робить її схожою на мексиканський капелюх. У її центрі знаходиться чорна діра масою в мільярд Сонць"}, 29000000)
queue.enqueue({"name": "Гігантський Войд Волопаса (Boötes Void)", "info": "Це величезна ділянка космосу діаметром 330 мільйонів світлових років, де майже немає галактик. Якби Чумацький Шлях був у центрі цього Войду, ми б дізналися про існування інших галактик лише у 1960-х роках"}, 700000000)
queue.enqueue({"name": "Олімп (Olympus Mons) на Марсi", "info": "Найвищий вулкан і гора в Сонячній системі. Його висота — 21,9 км, що майже втричі вище за Еверест. Він настільки великий, що його основа закрила б усю площу Франції"}, 0.00002)
queue.enqueue({"name": "Магнітар", "info": "і поля.Цікавий факт: Це тип нейтронної зорі з найпотужнішим магнітним полем у Всесвіті. Якби магнітар знаходився на відстані половини шляху до Місяця, він би миттєво стер дані з усіх кредитних карток на Землі та розірвав би а"}, 50000)
queue.display()

app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/")
def home(request: Request, order: str = "nearest"):
    objects = queue.get_all(order)
    return templates.TemplateResponse("diary.html", {
        "request": request, 
        "objects": objects,
        "current_order": order
    })
@app.get("/objects")
def get_objects(order: str = "nearest"):
    return queue.get_all(order)