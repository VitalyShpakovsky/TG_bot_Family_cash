<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Readme.md</title>
  <link rel="stylesheet" href="CSS/style.css">
  <link rel="stylesheet" href="CSS/normalize.css">
</head>
<body>
  <div class="container">
    <h1 class="title">
      Телеграмм бот версия 0.1.2
    </h1>
    <p>
        Данный телеграмм бот учет семейного бюджета.
    </p>
    <h2>
        Список команд телеграмм бота:
    </h2>
        <ul>
        <li><a href="#p1">/user</a></li>
        <li><a href="#p2">/add</a></li>
        <li><a href="#p3">/stat</a></li>
        </ul>
    <h3 id="p1"> Команда /user</h3>
        <p> После ввода запрашивает ввести имя пользователя и записывает его в базу</p>
    <h3 id="p2"> Команда /add</h3>
        <p> После ввода запрашивает выбор действия внести расход или доход. После вносит в базу полученную информацию</p>
    <h3 id="p3"> Команда /stat</h3>
        <p> После ввода запрашивает выбор действия: (расходы за год, расходы за текущий месяц). 
            После выводит информацию об общих расходах за выбранный период по пользователям</p>
    <h2>    
        Обновления
    </h2>
        <div>
            <p> Версия 0.1.1</p>
            <p> Расширена команда /add (добавлена возможность внесения дохода) и добавлена команда /mount</p>
        </div>
        <div>
            <p> Версия 0.1.2</p>
            <p> Заменена команда /mount на команду /stat и расширены ее возможности</p>
        </div>
    <h2>    
        Установка
    </h2>
        <p>Скопируйте с репозитория в выбранную директорию. Создайте файл .env куда внесите токен бота.</p>
        <img src="Image/file_env.jpg" alt="Image">
  </div>
</body>
"# TG_bot_Family_cash" 