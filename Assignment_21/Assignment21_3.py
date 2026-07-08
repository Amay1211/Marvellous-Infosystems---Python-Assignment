from threading import Thread, Lock, current_thread, get_ident
counter = 0
lock = Lock()

def increment():
  print(f"theard Name : {current_thread().name} and id : {get_ident()}")
  global counter
  for _ in range(100000):
    with lock:  # prevents race condition
      counter += 1

def main():
  threads = [Thread(target=increment) for _ in range(5)]
  [t.start() for t in threads]
  [t.join() for t in threads]

if __name__ == '__main__':
  main()
  print("Final counter:", counter)
