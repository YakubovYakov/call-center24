import os
import json
from bs4 import BeautifulSoup

def process_html_files(folder_path, output_json):
    data = []
    file_count = 1
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".html"):
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                soup = BeautifulSoup(content, 'html.parser')
                
                # Извлекаем заголовок (или вопрос)
                title = soup.find(['h1', 'h2', 'strong', 'u'])
                
                # Извлекаем основной текст (или ответ)
                body_content = ""
                
                # Собираем текст из параграфов и списков
                paragraphs = soup.find_all('p')
                lists = soup.find_all(['ul', 'ol'])
                
                for p in paragraphs:
                    body_content += p.get_text(strip=True) + "\n"
                
                for list_tag in lists:
                    for item in list_tag.find_all('li'):
                        body_content += "- " + item.get_text(strip=True) + "\n"
                
                # Если title или body_content пустые, устанавливаем значение по умолчанию
                question = title.get_text(strip=True) if title else f"Информация {file_count}"
                answer = body_content if body_content else "Ответ не найден"
                
                data.append({
                    "id": file_count,
                    "question": question,
                    "answer": answer
                })
                
                new_filename = f"question_{file_count}.html"
                os.rename(file_path, os.path.join(folder_path, new_filename))
                
                file_count += 1
    
    # Сохранение данных в JSON
    with open(output_json, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    print(f"Все данные сохранены в {output_json}")

# Укажи путь к папке с HTML файлами и имя выходного JSON файла
folder_path = '/Users/a777/Downloads/24/data'
output_json = 'knowledge_base.json'
process_html_files(folder_path, output_json)
