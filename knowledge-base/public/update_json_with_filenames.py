import json

def update_json_with_filenames(json_path, output_json, html_folder):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Пройдемся по каждому объекту и добавим имя файла
    for index, item in enumerate(data):
        item["filename"] = f"{html_folder}/question_{index + 1}.html"  # Добавляем путь до HTML файлов
    
    # Сохраняем обновленный JSON
    with open(output_json, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Файл {output_json} успешно обновлен с добавлением путей к HTML файлам.")

# Укажи путь к JSON файлу, папке с HTML файлами и выходному JSON файлу
json_path = 'knowledge_base.json'  # Исходный JSON файл
output_json = 'updated_knowledge_base.json'  # Новый JSON с добавленными ссылками
html_folder = 'html'  # Папка, где будут храниться HTML файлы
update_json_with_filenames(json_path, output_json, html_folder)
