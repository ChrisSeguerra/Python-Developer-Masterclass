# Abstruction (Generalize code into reusable form)

turkey_cooking_time = 14
ham_cooking_time = 5


def cooking_end_time(start_time, duration):
    end_time = (start_time + duration) % 24  # OR return (start_time + duration) % 24
    return end_time   


# print(cooking_end_time(15, 7))

print(f"Take the turkey out of the oven at {cooking_end_time(20, turkey_cooking_time)} o'clock.")

print(f"Take the ham out of the oven at {cooking_end_time(13, ham_cooking_time)} o'clock.")