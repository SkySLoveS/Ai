from utils.AI import AI
import json

Ai = AI()

path_to_transcript = input("Введите путь к транскрипту в формате txt: ")
transcript = ""
with open(path_to_transcript, 'r', encoding='utf-8') as f:
    for line in f:
        transcript += line
result = Ai.request(transcript)

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)