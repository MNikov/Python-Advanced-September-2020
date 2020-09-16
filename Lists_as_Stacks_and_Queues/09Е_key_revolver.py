from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intel_value = int(input())
bullets_shot = 0
total_shots = 0
is_magazine_empty = False

while locks:
    bullet = bullets.pop()
    lock = locks.popleft()
    if bullet <= lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.appendleft(lock)
    bullets_shot += 1
    total_shots += 1
    if bullets_shot == gun_barrel_size and bullets:
        bullets_shot = 0
        print('Reloading!')
    if not bullets:
        is_magazine_empty = True
        break

money_earned = intel_value - (total_shots * bullet_price)

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
elif is_magazine_empty:
    print(f"Couldn't get through. Locks left: {len(locks)}")
