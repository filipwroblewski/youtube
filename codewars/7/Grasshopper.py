def check_alive(health):
    if health <= 0:
        return False
    else:
        return True


check_alive(5)  # True
check_alive(0)  # False
check_alive(-5) # False