# Конспект по линуксу

## команды
	pwd показывает ту директорию в которой мы находимся внутри линукса
	cd позволяет перейти в другую директорию
	cat чет открыть(это одно из применений)
		так же с помощью cat можно объеденять файлы: cat 1.txt 2.txt
	tac - как и cat только выводит в обратном порядке
	echo выводит текст в консоль: echo "привет"
		echo можно так же перенаправить вывод в файл
	ls -a - посмотреть скрытые файлы
	ls -l посмотреть в виде списка
	touch чет добавляет
	ls -l / какую-то хуйню в виде списка выводит
	ls -la выводит файлы текущей дериктории в виде списка
	ls -R путь - рекурсивно выводит все, что есть
	rm для удаления файлов
	cd .. - перейти в родительскую директорию
	echo * - выводит все аргументы
	touch {1..50}.txt - создаст 50 текстовых документа
	touch user_{ivan,alex,petr}.txt - создаст 3 текстовых документа
	echo $() - таким образом можно подставлять результаты выполнения других команд
	mkdir - команда для создания дерикторий
	-p флаг, который позволяет создавать вложенные дериктории, если таких нет
	mkdir -p {2020..2024}/{01..12}
	rm -rf {2020..2024}
	history - смотреть историю команд
	history | less - пиздатенько смотреть историю команд
	history | grep "ключевое слово" - поиск команды из истории
	cp - копировать, что либо 
	cp ~/.bash_history bash_history.backup
	!номер - повторить команду под конкретным номером
	!! - повторить предыдущую команду
	cd - - возвращает в предыдущую директорию
	du -sh ...* - размер дерикторий
	можно перенаправлять поток вывода:
		например: pwd > 1.txt
	printf  - позволяет печатать форматированный текст
		printf "first line\nsecond line\n fird line\n" > 4.txt
	2> - чтобы перенаправить сообщение об ошибке
		например: ls ne_cysh_file 2> 4.txt
	&> выводит и stdout and stderr
	wc -l - модет посчитать кол-во файлов, мб чет еще
		ls -la /usr/bin/ | grep zip | wc -l
	sort - сортирует
	uniq - удаляет повторы
## Полезные горячие клавиш:
	cntr + A курсор в начало
	cntr + E курсор в конец
	cntr + Home по командам в лево
	cntr + End по командам в право
	сntr + w удалляет предыдущие команды
	сntr + y хуйня которая возвращает удаленную команду, с помощью cntr + w

## соединение команд, которые впадлу куда-то относить:
	```ls -la /usr/bin/ | grep zip
	ls -la - выводит все файлы, grep zip - фильтрует, чтобы были только с расширением zip
	и это все можно передать куда-нибудь, например дописать: "> aboba.txt"
	ls *.txt | tee output.txt - все по стандарту, tee сохраняет вывод в текстовый файл output.txt, короче хуйня позваляет и видеть, что выводит и сохранять```
## какая-то забавная залупа, которая зачем-то существует
	/dev/null - если туда перенаправить вызов, то нихуя не произойдет(все исчезнет), ответ попадет в так называемую "черную дыру"
	> - перенапрявляет вывод, как я понял
	>> - дозаписывает хуйня
	printf - более удобная хуйня, чем echo "привет\nвторая линия..."
    > при перенаправлении вывода создает новый файл или перезаписывает существующий (для стандартного вывода).
    2> при перенаправлении вывода программы создает новый файл или перезаписывает существующий (для вывода ошибок).
    &> при перенаправлении вывода создает новый файл или перезаписывает существующий (для стандартного вывода и вывода ошибок).
    >> создает новый файл или дозаписывает в существующий (для стандартного вывода).
    2>> создает новый файл или дозаписывает в существующий (для вывода ошибок).
    &>> при перенаправлении вывода создает новый файл или дозаписывает в существующий (для стандартного вывода и вывода ошибок).
    | используется для передачи вывода одной команды в качестве ввода для другой команды.
	
	
	
	если хочется и перенаправить вывод в файл и одновременно увидеть результат, то можно использовать команду tee
			ls -la *.txt | tee output.txt
	mkdir - создать директорию
	шоб удалить директорию надо rm -r имя директории
	mkdir -p - позволяет создавать дерево, то есть директории в директории
	еще мона короч если надо хуйню крутую сделать mkdir -p another/{one,two}inner - тут создастся директория another в которой
	будут директории one, two в которых будет директория inner
	touch - можно создать пустой файл
	true > имя документа - так тоже можно создать пустой документ
	nano имя файла - работать/редачить текстовый документ
## часто бывает, что нужно посмотреть не весь файл, а только его начало или конец, для этого существуют команды head and tail примеры использования
	head -n1 file.txt(сначала команда, потом -n и тут скока первых строчек хочешь увидеть дальше имя файла)
	с tail все просто наоборот
	watch -n1 date - конкретно в этом примере это тема откроет окошка и будет время с датой обновлять раз в 1 секунду
	можно обойтись без приставки -n1, но тогда  по умолчанию будет обновляться раз в 2 секунды все
	watch -g "кманда" - будет показывать до тез пор, пока в команде чет не поменяется 
	mv имя текущего файла имя нового файла - так название мона менять(присваивать новое имя)
	stats ивя фвйла - можно посотреть всю инфу о файлею Дату измененияч, дату посмледнего открытия...
	touch -am --date="tomorrow" tests.txt
	touch -am --date="1228-09-02" tests.txt
	а вот так можно менять инфу о фалйах
	можно назначать большой команде какую-то одну букву
	для этого есть утилита alias буква или имя,какое мы хотим назначить="за место какой команды"
	но это все сохраниться в текующем сиансе, чтобы сохранить навсегда, то надо перейти 
	с помозую man можно посомтреть, документацию по использованию команды
	так же это можно делать так - команда --help
	
## переменные окружения
	env 
	когда мы хотим использовать переменные окружения, то надо перед этим поставить значек долара
	шоб создать самим  переменную, надо написать export переменная(вроде только с капсом)=значение
	так переменная буддет созднана только в текущей сессии 
	чтобы сохранить эту переменную навсегда, то надо прописать echo "export MY_VARIABLE=123" >> ~/.bashrc
	tr - заменяет одни символы на другие символы tr ":" "\n"
	path - кароче сложная тема 
	но с нее мона скрипты вызывать
	чтобы добавить тудой директорию, надо изменить в файлике ~/.bashrc в конец написать export PATH=$PATH:и чет сюда еще, например $Home
	$PATH пишется еще раз, чтобы все, что юыло оставалось
	чтобы скрипт написать, если ты в той директории, которая тебе нужна, то можешь написать
	micro имя файла, туда переходишь и пишешь скрипт
	в первой строчке скрипта там должно быть #!/bin/bashrc
	тута ты пишешь скрипт, потом, чтобы дать команду на исполнения этого скрпипта, надо написать chmod +x hello
	а потом еще перезапустить надо это командой: source ~/.bashrc
	чтобы твоя программка работала, надо, чтобы в переменной PATH был указан путь в директорию, в которой твоя программа написана
	либо же указывать путь
	CDPATH - с помощью  этой переменной можно сделелать, чтобы например при поиске cd искалось не только в той директории
	в которой ты находишься, а еще в какой-то еще. Ее ты как раз указываешь
	можно перевести, как путь cd
	export CDPATH=$HOME таким образом мы добавим в поиск текущую директорию текущего пользователя в CDPATH
	и когда мы будем чет искать, то искаться тока тут и будет
	и теперь мы можем быстро переместиться 
	чтобы такую штуку сохранить, надо в .bashrc прописать export CDPATH=.:$HOME/code
	
## есть жесткие и мягкие ссылки на файлы
	ln original hard_link_to_original
	ln -s original soft_link_to
	отличие в том, что если удалить оригинальный файл, то мягкая ссылка будет ссылаться в пустоту, а в твердой 
	будет еще все. Получается, что изначальный файл - это тоже твердая ссылка.
	в основном используют мягкие сслыки
	
## есть разные пользователи, соответственно есть и их группы 
	чтоб группы пользователя чекнуть: groups
	а для определенного: groups aboba
	пользователи храняться в cat /etc/passwd
	можно так же группы чекнуть кста cat /etc/group
	чтобы создать нового пользователя надо написать sudo adduser и имя нового пользователя
	чтобы зайти от нового пользователя, то надо написать su - имя пользователя 
	но новый пользователь будет лохом сначала, поэтому ему нужно добавить права админа от старого
	sudo cat /etc/sudoers вот сдеся
	можно создать группу так sudo groupadd имя группы
	шоб добавить пользователей в группу, надо sudo usermod -aG имя группы имя пользователя, которого хотим добавить
	еще один способ добавить в группу sudo adduser sterx friends
	
    Можно менять пароль с помощью sudo passwd имя юзера

## права на доступ ко всяким разным файлам
	-rw-r--r-- - в первом прочерки будет не прочерк, если это директория, дальше р - значит можно читать файл
	в - значит можно менять, прочерк значит нельзя исполнять, дальше идет можно читать группе конкретной, дальше всем...
	чтобы менять права chmod o-r эта уберет права на чтение(r) аверс(остальным)(o) так же можно u(user) and g(group)
	для директорий тоже самое се 
	chown - чтобы менять пользователя, который владеет этим файлом , а
	chgrp - чтобы менять группу, владеющую этим фалйом
	
	
	
## короче есть же по три права у юзера группы и остальны:
	легче понять будет, что всего 3 права есть и три единицы в 10 системе счисление - это 7, и так можно для каждой группы одновременно
	чтобы мозгу не трахать можно права раздавать с кайфом через chmod три циферки имя файла
	
## архивы и сжатие
	чтобы создать архив tar -cvf new_file_name.tar old_file_name
	для распаковки нахой надо tar -xvf original.tar
	чтобы создать сжатый архив tar -czvf original.tar.gz original
	шоб распоковать tar -xzvf original.tar.gz
	
## скачали короче чтобы зазиповать хуйню
	теперь, чтобы зазиповать надо zip -r new_file_name.zip old_file_name
	чтобы распоковать unzip file_name.zip
	
## поиск
	which - показывает, где лежит исполнимый файл
	locate - поиск файлов по предварительно создаваемому индексу
	cat /etc/os-release - просмотр версии дистрибутива линукс
	find - да выводит всякую хуйню, вроде все погнял и ничего особенного нема
	
    c помощью split -b по сколько надо разделять file_name ну тут типа начальное имя блоков
    ну а назад можно с помощью cat test.mov.* > new_file 
	
## установка программ: 
	apt - мы уже знаем
	для удаление sudo apt remove/purge program_name
	purge - удалит еще конфигурационные файлы, которые использовала это программа
	с помощью apt search например youtube мы можем посмотреть пакеты ютуба
	а шоб внутри посмотреть инфу об определенном пакете 
	apt show пакет 
	
	
## турминальный мультиплекстеры:
	нужны для того, чтобы при закрытии сессии скрипт продолжал выполлняться и можно было сразу несколько процессов делать
	tmux - один из них
	создавать сессии можно tmux new-session -s name
	чтобы создать в ней еще один процесс, нужно горячими клавишами заебашить cntl + B руки отпустил и кавычки двойные
	отсоедениться можно с помощью cntl + B руки отпустил и d 
	чтобы поглядеть, какие процессы работают, нужно написать pstree -a
	чтобы подключиться обратно к сессии, нужно написать tmux attach -t session_name
	чтобы по панелям летать нужно прописывать там cntl + B руки опустил и вверх или вниз нажал(смотря )
	cntr + d - выход
	4.34 - интересный видосик, но на будущее скорее всего 

```
htop - с помощью этого можно килять запущенные скрипты
сначала идет cntrl + B потом идет комнда
например: чтобы найти запущенный скрипт, нудно нажать k
в htop первая строчка отвечает за проуесс айди, потжтому с поммощью этого можно посылать хуйню
прямо из командной строки
чтобы кильнуть можно написать kill -9 айдишник процесса 
чтобы быстро найти айдишник прроцесса, надло написать ps -A | grep ключевое слово
killall  name - закрывает все работающие программы содержащие ключевое слово


wget - хуйня чтобы скачивать из инета всякую парашу, можно дажже сайты целые выкачивать
batcat - лучше, чем просто cat
```

## make файлы: 
	чтобы создать make файл, нужно через любой текстовый редактор написать скрипт туда и название мэйк файла с заглавной буквы
	например micro Makefile
	внутри пишешь название скрипта двоеточие, ентер таб и пишешь сам скрипт
	 вот пример: 
	hello:
		echo hello world
		
		
	а вообще стоит делать так:
	.PHONY: hello
	hello:
		echo hello world
		
	это делается для того, чтобы в случае если скрипт и файл названы одинаково не было конфликта
	
```	
хуй знает, для всего ли это работает, но свернуть vim можно комбинацией cntrl + z
посмотреть свернутые процессы можно командой jobs
чтобы запустить свенутый процесс утилита fg (запуститься первая программа)
либо fg %номер программы
но процесс свернутый не работает фоново, а просто поставлен на паузу
чтобы запустить, чтобы  он работал в бэке, надо написать bg %1 или любой другой номер процесса
	
	
	
	
	пусть будет сдесь: https://stackoverflow.com/?newreg=c1c3136785d74781bb0b1cf20ac269c4 
	https://www.labirint.ru/books/850120/ сайт крутяк вообще
	https://github.com/madscheme/introducing-python
```