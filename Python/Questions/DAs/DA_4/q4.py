import math
import os

def verify_log_identities():
    x = 2.0
    log_identity_1 = math.log(x) + math.log(x)
    log_identity_2 = 2 * math.log(x)

    with open('log_res/log_identity_1_result.txt', 'w') as file:
        file.write(f'The result of log(x) + log(x) is: {log_identity_1}')

    with open('log_res/log_identity_2_result.txt', 'w') as file:
        file.write(f'The result of 2 * log(x) is: {log_identity_2}')

def verify_trig_identities():
    angle_rad = math.radians(45)  # Convert degrees to radians
    sin_identity = math.sin(angle_rad)
    cos_identity = math.cos(angle_rad)
    tan_identity = math.tan(angle_rad)

    with open('tri_res/sin_identity_result.txt', 'w') as file:
        file.write(f'The result of sin(45 degrees) is: {sin_identity}')

    with open('tri_res/cos_identity_result.txt', 'w') as file:
        file.write(f'The result of cos(45 degrees) is: {cos_identity}')

    with open('tri_res/tan_identity_result.txt', 'w') as file:
        file.write(f'The result of tan(45 degrees) is: {tan_identity}')

# Create folders if they don't exist
os.makedirs('log_res', exist_ok=True)
os.makedirs('tri_res', exist_ok=True)

# Verify and store log identities
verify_log_identities()

# Verify and store trigonometric identities
verify_trig_identities()
