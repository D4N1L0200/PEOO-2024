# print("Digite seu nome completo:")
# full_name = input()
# print(f"Bem-vindo ao Python, {full_name.split()[0]}")

print("Digite seu nome completo:")

full_name = input().strip()
space_idx = full_name.index(" ")

print(f"Bem-vindo ao Python, {full_name[:space_idx]}")
