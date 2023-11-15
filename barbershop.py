import threading
import time
import random

num_visitors = 100
num_barbers = 4

semaphore = threading.Semaphore(num_barbers)

def barber(visitor_id):
    semaphore.acquire()
    
    print(f"Парикмахер начал стрижку посетителя {visitor_id}")
    time.sleep(2)
    print(f"Посетитель {visitor_id} стрижка закончена")
    
    semaphore.release()

def visitor(visitor_id):
    # time.sleep(random.randint(0, 2))
    # Занимаем кресло парикмахера
    barber(visitor_id)

barber_threads = []
for i in range(num_barbers):
    t = threading.Thread(target=barber, args=(f"№{i+1}",))
    barber_threads.append(t)
    t.start()

visitor_threads = []
for i in range(num_visitors):
    t = threading.Thread(target=visitor, args=(i+1,))
    visitor_threads.append(t)
    t.start()

for t in visitor_threads:
    t.join()

for t in barber_threads:
    t.join()
