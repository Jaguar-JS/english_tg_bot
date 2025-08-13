
```
├─ .env                     # 🔑 Змінні середовища (API ключі, проксі, токени бота)
│
├─ bot.py                   # 🚀 Точка входу – ініціалізація aiogram бота, запуск polling/webhook
├─ config.py                # ⚙️ Налаштування (токени, проксі, параметри моделі)
├─ constants.py             # 📌 Константи (словники, шляхи, теми)
│
├─ handlers/                # 📥 Обробники команд, повідомлень та callback'ів
│  ├─ gpt_interface.py      # Виклики GPT, відповіді на повідомлення користувача
│  ├─ start.py              # /start і привітання
│  ├─ help.py               # /help або інфо
│  └─ errors.py             # Обробка винятків та помилок
│
├─ services/                # 🔌 Сервіси та інтеграції
│  ├─ gpt_client.py         # Обгортка OpenAI API (AsyncOpenAI з http_client)
│  ├─ prompts_loader.py     # Завантаження та кешування текстових промптів
│  ├─ scenario_builder.py   # Генерація сценаріїв уроків
│  ├─ exercise_generator.py # Генерація вправ
│  └─ translator.py         # Переклад текстів
│
├─ utils/                   # 🛠 Допоміжні інструменти
│  ├─ logger.py             # Логування
│  ├─ keyboards.py          # Клавіатури aiogram
│  ├─ session.py            # Менеджмент сесій користувачів
│  └─ tts.py                # Text-to-Speech (за потреби)
│
└─ data/                    # 📂 Статичні ресурси
   ├─ img/
   │  └─ avatar.png         # Аватар бота
   ├─ audio/
   └─ prompts/
      ├─ scenario_builder_prompt.txt
      ├─ bot_dialogue_prompt.txt
      ├─ grammar_tutor_prompt.txt
      ├─ translate_prompt.txt
      └─ exercise_prompt.txt
```


