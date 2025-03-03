# РЕЛЯЦИОГННЫЕ БАЗЫ ДАННЫХ
## преимущества
-   Доступ к данным возможен для нескольких пользователей одновеременно
-	Действует защита от повреждения данных пользователями
-	Существуют эффективные методы сохранения и считывания данных
-	Данные определены схемами и имеют ограничения
-	Объединения позволяют найти отношение между различнными типами данных
	-Декларативный (в противоположность императивному) язык запросов SQL 
	
Так они называются, потому что они показывают отношения между различными типами данных в форме
прямоугольных таблиц

## SQL
	SQL не является API илипротоколом. Это декларативный язык: вы говорите, что нужно сделать, а
	не как жто сделать
	SQL - универсальный язык реляционных баз данных


```
ГЛАВА 14 - программирование баз данных(sqlite)
система управелния базами данных(СУБД) - это программное обеспечение, которое управляет крупными коллекциями данных
типы данных в sqlite:
	тип данных sqlite		Описание						Соответствующий тип данных Python
	NULL					Неизвестное значение			None
	INTEGER					Целое число						int
	REAL					Вещественное число				float
	TEXT					Строковое значение				str
	BLOB					Двоичный большой объект			может быть л.бым объектом
```
Первичные ключи - то есть уникальный номер каждой строки в отдельном столбике, например индификационный номер пользователя(как я понял)
индификационный столбец - столбец с уникальными значениями, на которые будем ссылаться, чтобы достать данные конкретной строки
если столбец не содержит данных, считается, что он имеет знаение NULL
псевдокод процесса использования sqlite:
	присоедениться к базе данных
	получить курсор для базы данных(курсор - это объект, который может получать доступ к данным в базе данных и манипулировать ими)
	выполнить операции с базой данных
	зафиксировать изменнения в базе данных
	закрыть соединение с базой данных

Создание и удаление таблиц
	для создания таблицы используется инструкция CREATE TABLE
	для удаления таблицы используется инструкция DROP TABLE
	общий вормат сощдание таблицы: CREATE TABLE имя таблицы(имя столбца1 тип данных, имя столбца2 тип данных ...)
	можно назначить столбец в качестве первичного ключа указав ограничение PRIMARY KEY
	при создании первичного ключа так же рекомендуетя использовать ограничение NOT NULL. Оно указывает на то, что столбец нельзя оставить пустым
	CREATE TABLE имя таблицы(имя столбца1 тип данных PRIMARY KEY, имя столбца2 тип данных ...)
	так же, чтобы не возникало ошидки, когда создаешь таблицу с именем, которая уже есть, то можно использовать
	CREATE TABLE IF NOT EXISTS, тогда таблица будет создана, если такой еще не существует, в противном случае ничего нового создано не будет
	обзий формат удаления таблицы .execute('DROP TABLE имя таблицы')
	в целях предотвращения ошибки прри удалении несуществующий таблицы рекомендуетя дописывать IF EXISTS
	INSERT - инструкция, используется для вставки новой строки в таблицу
	VALUES - добавление значений в столбцы
	вот общий формат этой хуйни
		INSERT INTO имя тбалицы (имя столбца1, имя столбца2...)
		VALUES (значение1, знаение2...) (можно вставить нулевое значение написав NULL)
		можно присвоить нулевое значение столбцу просто оставив его без внимания
		NULL должно использоваься только для заполнения неизвестных данных 
		чтобы столбцу никогда не присвоилось значение NULL, при создании таблицы нужно использовать ограничение NOT NULL
	вот например: CREATE TABLE (ItemId INTEGER PRIMARY KEY Not NULL, ItemName TEXT NOT NULL, PRICE REAL NOT NULL)

## Вставка значений переменных:
	''' INSERT INTO Inventory (ItemName, Price) VALUES (?, ?)'''
	вопросительные знаки появляются как местозаполнители значений
	потом мы пеердаем эту хуйню в .execute(строка с вопросами, (сюда уже переменные вместе вопросов))

## МЕТОДЫ:
	.execute() - отправляет строку в СУБД , которая в свою очередь, выполянет ее в базе данных
	
## извлечение данных из базы данных(ахуть, об этом целая подглава, хотя там одна инструкция SELECT)
	начало с очень простой формы инструкции - SELECT столбцы FROM Таблица(если хочется все столбцы сразу, то вместе имен столбцов можно написать '*')
	и эта хуйня короче не выводит резутьтат. Чтобы получить результат програмы нужно вызвать метод .fetchall() или .fetchone()
	fetchall() - возвращает рещультат инструкции в виде списка кортежей
	fetchone() - делает тоже самое, но по одной строчке при каждом вызове
	
	стобцы - одно или несколько имен столбцов
	таблица - имя таблицы
	а еще короче можно критерий поиска добавлять, например: SELECT столбцы FROM таблица WHERE критерий (price > 10.00)
	а еще можно использовать операторы AND, OR, NOT, например так можно критерии разные делать
	если хочется найти нужное строковое значение, то надо четко написать, как и есть в базе данных,
	иначе применить функцию lower(имя столбца). Так же и upper тоже есть 

## Использование оператора LIKE
	этот оператор применяется, если надо найти, чтобы в строчке было именно это слово, а на другие не смотреть
	ну то есть, если нам нужны именно плитки шоколадные, а в строках есть названия типо "плитка молочного шоколада"
	то нам через WHERE набирать придется полный текст, и так с каждой плиткой, но это кринж вообще
	именно для этого можно просто написать SELECT столбец FROM таблица WHERE столбец, в котором искать "%Плитка%"
	
## Сортировка результатов запроса SELECT
	если хотим отсортировать, то надо использовать ORDER BY
	SELECT столбец/цы FROM таблица ORDER BY по какому столбцу сортировать
	
## Агрегатные функции
	агрегатные функции выполняют вычесление на наборе значений из таблицы базы данных и возвращает одно значение 
	ФУНКЦИИ
		AVG - функция вычисляет среднее значение стобца содержащего числовые данные
			SELECT AVG(столбец) FROM таблица
			после вычесления надо потом достать результат, так как функция создает кортеж с одним элементом
			medium = cur.fetchone()[0]  # Извлекаем среднее значение из результата запроса
		SUM - все понятно и так, и делать надо все тоже самое, что и с AVG
		так же все с
		MIN
		MAX
		COUNT - вычесляет сколько строк в таблице
		COUNT(*) - ну он означает, что все строки таблицы посчитает
	
ну тут вроде нормальный пример, нормального рабочего кода

ДЛЯ НАЧАЛА СОЗДАНИЕ ТАБЛИЦИ В БАЗЕ ДАННЫХ
```python
import sqlite3


def main():
    try:
        with sqlite3.connect('inventory.db') as conn:
            cur = conn.cursor()
            sql = '''CREATE TABLE Inventory (ItemId INTEGER PRIMARY KEY NOT NULL,
                     ItemName TEXT,
                     Price REAL)'''
            cur.execute(sql)
            cur.execute('''EploseID INTEGER PRIMARY KEY NOT NULL,
                           Name TEXT,
                           Position TEXT''')

            conn.commit()

    except sqlite3.Error as e:
        print(f'ошибка при работе с базами данных {e}')


if __name__ == '__main__':
    main()
```
ТЕПЕРЬ РАБОТА С ТАБЛИЦЕЙ
```python
import sqlite3


def main():
    try:
        with sqlite3.connect('inventory.db') as conn:
            cur = conn.cursor()
            again = input('а надо ли тебе вообще еще данные водить? (д/н)')

            while again.lower() == 'д':
                item_name = input('введите название инструмента')
                price = float(input('введите цену инструмента'))

                cur.execute('''INSERT INTO Inventory (ItemName, Price)
                               VALUES 
                                      ('молоток', 14.99),
                                      ('плоскогубцы', 12.99),
                                      ('электродрель', NULL),
                                      (?, ?)''',
                            (item_name, price))

                again = input('хотите продолжить? (д/н)')

            conn.commit()

    except ValueError:
        print('а ты нахуй цену словами писать начал, дурачек!??')


def tabl_select():
    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute('SELECT ItemName, Price FROM Inventory')
    results = cur.fetchall()
    conn.close()

    for row in results:
        print(f'{row[0]:50} {row[1]}')


def tabl_select2():
    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute('SELECT ItemName, Price FROM Inventory')
    results = cur.fetchone()
    znachnone = 0

    while results is not None:
        if results[1] is not None:
            print(f'{results[0]:45} {results[1]:5}')

        else:
            print(f'{results[0]:45} {znachnone:5}')

        results = cur.fetchone()

    conn.close()


def sred_znach():
    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute('SELECT AVG(Price) FROM Inventory')
    medium = cur.fetchone()[0]  # Извлекаем среднее значение из результата запроса
    cur.execute('SELECT MAX(Price) FROM Inventory')
    max_ch = cur.fetchone()[0]  # извлекаем максимальное значение
    cur.execute('SELECT MIN(Price) FROM Inventory')
    min_ch = cur.fetchone()[0]  # извлекаем минимальное значение
    cur.execute('SELECT SUM(Price) FROM Inventory')
    sum_ch = cur.fetchone()[0]  # извлекаем сумму чисел
    cur.execute('SELECT COUNT(Price) FROM Inventory')
    kol_str = cur.fetchone()[0]  # извлекаем количество строк
    result = [medium, max_ch, min_ch, sum_ch, kol_str]
    conn.close()
    return result


def sred_znach1():
    res = sred_znach()
    for i in res:
        print(i)


if __name__ == "__main__":
    main()
    tabl_select()
    tabl_select2()
    sred_znach1()
```
## Обновление и удаление существующих строк
	UPDATE - инструкция для изменения значения 
	общий формат записи
		UPDATE таблица
		SET столбец = значение
		WHERE критерий
		
		UPDATE Inventory
		SET Price = 37327
		WHERE ItemId = 3/ если мы хотим все определенные элементы изменить WHERE ItemName LIKE "%дрель%"
		чтобы несколько столюцов изменить 
			SET столбец1 = значение 1
			SET столбец2 = значение 2
			...
	чтобы узнать скока строк изменилось можно использовать атрибут .rowcount
	DELETE - используется для удаления строк
	общий формат DELETE FROM таблица WHERE критерий(условное выражение)
		DELETE FROM Inventory WHERE ItemId == 10
	Ну удалять несколько строк сразу можно так же, как их и менять
	посчитать скока строк было удалено можно также как и посчитать скока их удалено было
	
## Подробнее о первичных ключах
-	составной ключ - это ключ, созданный путем совмещения двух или более существующих столбцов
	пока не забыл
	тут интересно знать, что 
-   при создании таблицы автоматом создается RowId, но при вызове всех столбцов таблицы он отображаться не будет
	но можно его глянуть .execute(SELECT RowId FROM таблица)
	.fetchall()
-	при добавлении строки, можно присвоить значение в столбик RowId, если такого значения еще не было, иначе программа выдаст ошибку
	так же UPDATE можноиспользовать
	но если присвоить значение NULL, то он не выдаст ошибку, а сам автоматом число подставит
	когда мы назначяем первичный ключ, то он становиться псевдонимом RowId, то есть по факту мы с ним и работаем
	на самом деле первичный ключ может быть любым типом данных
	
## Составные ключи
	общий формат создания составного первичного ключа
	CREATE TABLE имя таблицы (имя стобца1 тип данных1,
							  имя столбца2 тип данных2,
							  ...
							  PRIMARY KEY (имя столбца1, имя столбца2 ...)) (стоит не забывать применять NOT NULL)
							  
							  
## Обработка исключений базы данных
	короче, в sqlite3 есть собственные ошибки, поэтому в целях нормальной обработки стоит делать красиво
		
		conn = None
		try:
			conn = sqlite3.connect(имя базы данных)
			cur = conn.Cursor()
			# дальше тут операции с базой данных идут
			
		except sqlite3.Error:
			# ответка на исключение базы данных
			
		except Exception:
			# ответка на общее исключение
		finally:
			if conn is not None:
				conn.close()
				
	finaly будет выполняться всегда, так что, чтобы заккрывать файл, стоит использовать его
	
Операции CRUD
	четырмя базовыми операциями приложения базы данных являются создание, чтение, обновление и удаление
	CRUD образованна от 4ех английских слов create, read, update, delete
	создание - это процесс создания нового набора данных в базе данных. Он осуествляется с помощью INSERT
	чтение - это процесс чтения существубщего набора из бащы  данных. Он осуществляется с помощью инструкции SELECT
	обновление - это процесс добавление или изменения существующего набора данных из быз данных. Он осуществляется с помощью UPDATE
	удаление - процесс удаления. Осуществляется с помощью DELETE
	
Реляционные данные
	в реляционной базе данных столбец из одной таблицы может быть ассоцирован со столбцом из дпугих таблиц. Эта ассоциация создает связь между таблицами
	Внешние ключи - это столбец в одной таблице, который ссылается на первичный ключ в другой таблице 
	ну как пользоваться внешними клюачами надо будет выучить самому, мне лень этим пока что заниматься))




Тут полная работа
опять же создание
```python
import sqlite3


def main():
    try:
        with sqlite3.connect('inventory.db') as conn:
            cur = conn.cursor()
            create_inventory_table = '''CREATE TABLE IF NOT EXISTS Inventory (
                                                    itemID INTEGER PRIMARY KEY NOT NULL,
                                                    ItemName TEXT,
                                                    Price REAL)'''
            cur.execute(create_inventory_table)

            conn.commit()

    except sqlite3.Error as e:
        print(f'ошибка при работе с базами данных {e}')


if __name__ == '__main__':
    main()


# работа с базой данных
import sqlite3
EXIT = 5


def main():
    while True:
        answer_user = display_meny()
        if answer_user == EXIT:
            print('выход из программы')
            break

        if answer_user == 1:
            create_table()

        if answer_user == 2:
            read_position()

        if answer_user == 3:
            update_position()

        if answer_user == 4:
            delete_position()


def display_meny():
    print('\n ----- Меню ведения учета инструментов -----')
    print('1. Создать новую позицию')
    print('2. Прочитать позицию')
    print('3. Обновить позицию')
    print('4. Удалить позицию')
    print('5. Выйти из программы')
    answer_user = int(input('Введите свой вариант: '))

    if 0 < answer_user < 6:
        return answer_user
    else:
        print('совсем даун, смотри куда тыкаешь')


def create_table():
    print('создать новую позицию')

    with sqlite3.connect('inventory.db') as conn:
        cur = conn.cursor()
        name_user = input('Название позиции: ')
        price_position = float(input('Цена: '))

        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                    VALUES 
                            (?, ?)''',
                    (name_user, price_position))
        conn.commit()


def read_position():
    read_user = input('Введите название искомой позиции: ').strip()
    print(f'ищем позицию {read_user}')
    result = display_open(read_user)
    if result:
        print(f'{result} строк(а) найдено')


def update_position():
    upt_position = input('введите название искомой позиции: ')
    found = display_open(upt_position)
    if found:
        update = int(input('Введите ID искомой позиции: '))
        new_name = input('Введите новое название позиции: ')
        new_price = float(input('введите новую цену: '))
        upt(update, new_name, new_price)
        print(f'{found} строк(а) обновлена')


def delete_position():
    del_position = input('введите название искомой позиции: ')
    found = display_open(del_position)
    if found:
        id_del = int(input('Введите ID удаляемой позиции'))
        question = input('Вы точно хотите удалить позицию? (д/н): ')
        if question.lower() == 'д':
            delete_pos(id_del)


def display_open(name):
    print(f'Ищем позицию: {name}')
    with sqlite3.connect('inventory.db') as conn:
        cur = conn.cursor()
        cur.execute('''
                SELECT * FROM Inventory
                WHERE upper (ItemName) == ?
            ''', (name,))

        results = cur.fetchall()
        print(f'Найдено записей: {len(results)}')

        if results:
            print('Найденные позиции:')
            for row in results:
                print(f'ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')
        else:
            print('Позиции с таким названием не найдены.')
    return len(results)


def upt(id_new_pos, new_name, new_price):
    try:
        with sqlite3.connect('inventory.db') as conn:
            cur = conn.cursor()
            cur.execute('''UPDATE Inventory
                           SET ItemName = ?,
                               Price = ?
                           WHERE itemID = ?
                           ''', (new_name, new_price, id_new_pos))
            conn.commit()
            if cur.rowcount > 0:
                print("Обновление успешно выполнено.")
            else:
                print("Запись не найдена или данные не изменены.")

    except sqlite3.Error as err:
        print(f'ошибочка {err}')


def delete_pos(id_del):
    try:
        with sqlite3.connect('inventory.db') as conn:
            cur = conn.cursor()
            cur.execute('''DELETE FROM Inventory WHERE ItemId == ?
                        ''', (id_del,))
            conn.commit()
    except sqlite3.Error as err:
        print(f'ошибочка вышла {err}')


if __name__ == '__main__':
    main()

# ну и удаление таблицы
import sqlite3


def drop():
    try:
        with sqlite3.connect('inventory.db') as conn:
            cur = conn.cursor()
            drop_table = 'DROP TABLE IF EXISTS Inventory'
            cur.execute(drop_table)
            cur.execute(drop_table)

            conn.commit()

    except sqlite3.Error as e:
        print(f'ошибка при работе с базами данных {e}')


if __name__ == '__main__':
    drop()
```