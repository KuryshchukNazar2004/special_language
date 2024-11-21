import os
import requests
import base64

# Параметри репозиторію
repo_owner = "KuryshchukNazar2004"
repo_name = "special_language"
base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"

# Папка для збереження лабораторних
output_dir = "labs"
os.makedirs(output_dir, exist_ok=True)

# Отримання списку віток
branches_url = f"{base_url}/branches"
response = requests.get(branches_url)

if response.status_code == 200:
    branches = response.json()
    for branch in branches:
        branch_name = branch["name"]
        
        # Пропускаємо вітку lab9, якщо є
        if branch_name == "lab9":
            continue

        print(f"Завантаження файлів із вітки: {branch_name}")
        
        # URL для отримання файлу main.py
        file_url = f"{base_url}/contents/main.py?ref={branch_name}"
        file_response = requests.get(file_url)

        if file_response.status_code == 200:
            file_content = file_response.json()
            if "content" in file_content:
                decoded_content = base64.b64decode(file_content["content"]).decode("utf-8")
                
                # Збереження файлу у відповідну папку
                branch_dir = os.path.join(output_dir, branch_name)
                os.makedirs(branch_dir, exist_ok=True)
                file_path = os.path.join(branch_dir, "main.py")
                
                with open(file_path, "w") as f:
                    f.write(decoded_content)
                print(f"Лабораторна {branch_name} збережена у {file_path}")
            else:
                print(f"Файл у вітці {branch_name} не знайдено.")
        else:
            print(f"Не вдалося завантажити файл з вітки {branch_name}: {file_response.status_code}")
else:
    print(f"Помилка отримання списку віток: {response.status_code}")
