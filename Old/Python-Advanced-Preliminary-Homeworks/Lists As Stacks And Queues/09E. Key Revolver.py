from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(b) for b in input().split()]
locks = deque([int(l) for l in input().split()])
intel_value = int(input())
bullets_shot = 0
total_bullets_shot = 0
is_magazine_empty = False

while locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    if current_bullet <= current_lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.appendleft(current_lock)
    bullets_shot += 1
    total_bullets_shot += 1
    if bullets_shot == gun_barrel_size and bullets:
        print('Reloading!')
        bullets_shot = 0
    if not bullets:
        is_magazine_empty = True
        break

money_earned = intel_value - total_bullets_shot * bullet_price
if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
elif is_magazine_empty:
    print(f"Couldn't get through. Locks left: {len(locks)}")
