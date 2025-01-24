Официальная документация для голосового помощника Джарвис 

 

1. Общее описание 

Джарвис — это голосовой помощник, созданный для выполнения голосовых команд, автоматизации управления приложениями и поиска информации в интернете. Он использует Google API и другие внешние сервисы для обработки запросов, может вести диалоги на разные темы, а также поддерживает голосовые команды для управления программами, такими как FL Studio и Photoshop. 

 

2. Основные функции и возможности 

Управление системными настройками (громкость, яркость, спящий режим). 

Запуск и закрытие приложений (браузер, Telegram, Photoshop, FL Studio, Premiere Pro и другие). 

Запуск игр (по выбору пользователя из списка). 

Взаимодействие с FL Studio и Photoshop (управление воспроизведением, записью, создание слоёв, выбор инструментов и т.д.). 

Поиск информации в интернете через Google API. 

Поддержка голосовых диалогов (ответы на заранее определенные вопросы и темы). 

 

3. Установка 

Требования: 

Операционная система: Windows 10 или новее. 

Python версии 3.8 или выше. 

Интернет-соединение для работы с Google API и другими внешними сервисами. 

Установка необходимых библиотек: 

pip install speech_recognition pyttsx3 pyautogui pygetwindow google-api-python-client 
 

Настройка Google API: 

Зарегистрируйтесь на Google Cloud Console. 

Получите ключ API и добавьте его в проект. 

Запуск: 

Запустите main.py и активируйте голосовой помощник командой «Джарвис». 

 

4. Конфигурация 

Для корректной работы программы можно изменить конфигурацию в соответствии с вашими предпочтениями: 

Настройки звука и яркости — команды для установки значений громкости и яркости. 

Настройки путей к программам и играм — убедитесь, что пути в app_control.py соответствуют расположению программ на вашем устройстве. 

API ключи — добавьте ключи Google API и Telegram API в файл конфигурации. 

 

5. Примеры команд для управления 

Системные команды: 

«Джарвис, громкость на [уровень]%» 

«Джарвис, яркость на [уровень]%» 

«Джарвис, спящий режим» 

Запуск и закрытие приложений: 

«Джарвис, открой [название приложения]» 

«Джарвис, закрой [название приложения]» 

Запуск игр: 

«Джарвис, открой игру» 

Джарвис предложит выбрать игру из списка (Игра 1, Игра 2 и т.д.). 

Поиск в интернете: 

«Джарвис, найди в интернете [запрос]» 

 

6. Юридические положения 

Авторские права 

Все права на данный проект принадлежат его разработчику. Использование кода и логики Джарвиса в коммерческих или публичных целях возможно только с разрешения разработчика. Запрещается копирование, распространение и модификация проекта без указания источника и разрешения. 

Ограничение ответственности 

Джарвис предназначен для личного использования. Разработчик не несет ответственности за возможные последствия, связанные с использованием программы, включая ошибки работы или сбои, вызванные внешними факторами. 

Условия использования 

Использование Джарвиса подразумевает согласие с тем, что: 

Программа используется на страх и риск пользователя. 

Программа требует доступ к определённым API и личным данным (например, Google API и Telegram API). 

 

7. Часто задаваемые вопросы (FAQ) 

1. Какие команды активируют Джарвиса? 

Для активации используйте команду «Джарвис». 

2. Как изменить настройки программы? 

Для изменения настроек откройте файл конфигурации и отредактируйте пути к программам или уровни громкости. 

3. Можно ли добавлять новые программы для управления? 

Да, просто добавьте их в app_control.py, указав путь и название. 

4. Почему некоторые команды не работают? 

Убедитесь, что программы установлены в указанном пути и что у вас есть интернет-соединение для работы с API. 

 

8. Будущие улучшения 

Возможные функции, которые планируется добавить в будущих версиях Джарвиса: 

Улучшение диалоговой системы — добавление более сложной базы данных для ответов на любые вопросы. 

Поддержка новых API — интеграция с другими API для повышения функциональности. 

Расширение управления программами — добавление команд для новых профессиональных программ. 

Гибкая настройка команд — возможность добавлять и настраивать команды пользователем через интерфейс. 

 

9. Лицензия 

Этот проект распространяется под лицензией MIT. Подробности смотрите в файле LICENSE в корневой папке проекта. 

 

10. Примеры использования 

Пример 1: Запуск игры 

Пользователь: «Джарвис, открой игру» 

Джарвис: «Хорошо, сэр, какую игру вам открыть сегодня? Игра 1: Minecraft, Игра 2: Counter Strike...» 

Пользователь: «Открой игру 1» 

Джарвис: «Minecraft открыт.» 

Пример 2: Поиск информации 

Пользователь: «Джарвис, найди в интернете последние новости по технологии ИИ» 

Джарвис: Выполняет поиск и озвучивает результат. 

 

11. Будущие версии и развитие проекта Джарвис 

Развитие Джарвиса включает создание трёх различных моделей для удовлетворения потребностей различных пользователей. В будущем планируется разрабатывать каждую из них с набором уникальных функций: 

Базовая версия: 

Модель Джарвиса для повседневного использования, включающая основные функции для удобства и быстрой навигации. Включает управление системными настройками, запуск и закрытие приложений, поиск информации и стандартные диалоги. 

Подходит для тех, кто хочет использовать Джарвис как персонального помощника для домашних и повседневных задач. 

Расширенная версия для бизнеса: 

Модель Джарвиса с дополнительными функциями для бизнеса, такими как планирование, организация задач, создание отчётов и взаимодействие с корпоративными приложениями. 

Предназначена для пользователей, которые хотят использовать Джарвис как бизнес-ассистента, чтобы повысить свою продуктивность. 

Полная версия для профессионалов: 

Модель Джарвиса с полным набором функций для профессионального использования, включая управление сложными программами, поддержку работы с данными, расширенную настройку и интеграцию с инструментами разработки. 

Подходит для профессионалов и энтузиастов, которым требуется высокая степень контроля и мощные функции для работы и творчества. 

Каждая из версий будет регулярно обновляться и получать новые возможности на основании обратной связи пользователей. 

 

12. Благодарность пользователям 

Спасибо, что выбрали Джарвиса! Мы искренне благодарим каждого пользователя за то, что поддерживаете наш проект. Мы стараемся делать Джарвиса максимально полезным и удобным, а ваша поддержка помогает нам развивать его и добавлять новые функции. 

Поддержка пользователей позволяет команде Джарвиса двигаться вперёд и создавать семейство продуктов, которые улучшают качество жизни и работы. Спасибо за ваш вклад и поддержку, которая помогает Джарвису становиться лучше! 
