# Травицкий Сергей
# Домашнее задание к занятию  «Очереди RabbitMQ»

### Инструкция по выполнению домашнего задания

1. Сделайте fork [репозитория c шаблоном решения](https://github.com/netology-code/sys-pattern-homework) к себе в Github и переименуйте его по названию или номеру занятия, например, https://github.com/имя-вашего-репозитория/gitlab-hw или https://github.com/имя-вашего-репозитория/8-03-hw).
2. Выполните клонирование этого репозитория к себе на ПК с помощью команды `git clone`.
3. Выполните домашнее задание и заполните у себя локально этот файл README.md:
   - впишите вверху название занятия и ваши фамилию и имя;
   - в каждом задании добавьте решение в требуемом виде: текст/код/скриншоты/ссылка;
   - для корректного добавления скриншотов воспользуйтесь инструкцией [«Как вставить скриншот в шаблон с решением»](https://github.com/netology-code/sys-pattern-homework/blob/main/screen-instruction.md);
   - при оформлении используйте возможности языка разметки md. Коротко об этом можно посмотреть в [инструкции по MarkDown](https://github.com/netology-code/sys-pattern-homework/blob/main/md-instruction.md).
4. После завершения работы над домашним заданием сделайте коммит (`git commit -m "comment"`) и отправьте его на Github (`git push origin`).
5. Для проверки домашнего задания преподавателем в личном кабинете прикрепите и отправьте ссылку на решение в виде md-файла в вашем Github.
6. Любые вопросы задавайте в чате учебной группы и/или в разделе «Вопросы по заданию» в личном кабинете.

Желаем успехов в выполнении домашнего задания.

---

### Задание 1. Установка RabbitMQ

Используя Vagrant или VirtualBox, создайте виртуальную машину и установите RabbitMQ.
Добавьте management plug-in и зайдите в веб-интерфейс.

*Итогом выполнения домашнего задания будет приложенный скриншот веб-интерфейса RabbitMQ.*

[Срипт для установки](https://github.com/travickiy67/RabbitMQ/blob/main/files/sh.sh)  

**Скрин1**

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img1.1.png)  

**Скрин2**

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img1.3.png)  

**Скрин3**

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img1.4.png)  

---

### Задание 2. Отправка и получение сообщений

Используя приложенные скрипты, проведите тестовую отправку и получение сообщения.
Для отправки сообщений необходимо запустить скрипт producer.py.

Для работы скриптов вам необходимо установить Python версии 3 и библиотеку Pika.
Также в скриптах нужно указать IP-адрес машины, на которой запущен RabbitMQ, заменив localhost на нужный IP.

```shell script
$ pip install pika
```
**Добавил нового пользователя и виртуальный хост, в скрипты добавленна еще одна очередь и сообщение. Первые запуски были с очередью helo.**  
[producer.py](https://github.com/travickiy67/RabbitMQ/blob/main/files/producer.py)

[consumer.py](https://github.com/travickiy67/RabbitMQ/blob/main/files/consumer1.py)
 
Зайдите в веб-интерфейс, найдите очередь под названием hello и сделайте скриншот.
После чего запустите второй скрипт consumer.py и сделайте скриншот результата выполнения скрипта

*В качестве решения домашнего задания приложите оба скриншота, сделанных на этапе выполнения.*

**Скрин 1**  

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img2.2.png)

**Скрин 2**  

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img2.4.png)

*auto_ack=True, после прочтения сообщения удаляется*  

**Cкрин 3**  

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img2.3.png)

*auto_ack=False, сообщение сохраняется*  

**Скрин 4-5**  

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img2.5.png)  

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img2.6.png)  

Для закрепления материала можете попробовать модифицировать скрипты, чтобы поменять название очереди и отправляемое сообщение.

*Добавил еще очередь и сообщение*  

**Скрин 6-7**

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img2.7.png)   

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img2.8.png)  
---

### Задание 3. Подготовка HA кластера

Используя Vagrant или VirtualBox, создайте вторую виртуальную машину и установите RabbitMQ.
Добавьте в файл hosts название и IP-адрес каждой машины, чтобы машины могли видеть друг друга по имени.

Пример содержимого hosts файла:
```shell script
$ cat /etc/hosts
192.168.0.10 rmq01
192.168.0.11 rmq02
```
После этого ваши машины могут пинговаться по имени.

**Поменял имена хостов, прописал в hosts. на сервере сменил полюзователя и дал ему права на host /**

**Скрин 1**  

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img3.1.png)
 
Затем объедините две машины в кластер и создайте политику ha-all на все очереди.

*В качестве решения домашнего задания приложите скриншоты из веб-интерфейса с информацией о доступных нодах в кластере и включённой политикой.*

**Скрин 2-5**

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img3.4.png)

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img3.5.png) 

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img3.6.png)

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img3.7.png)


Также приложите вывод команды с двух нод:

```shell script
$ rabbitmqctl cluster_status

```
**Скрин 6-7**
![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img3.2.png)

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img3.3.png)

Для закрепления материала снова запустите скрипт producer.py и приложите скриншот выполнения команды на каждой из нод:

```shell script
$ rabbitmqadmin get queue='hello'
```
**Скрин 8-9**

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img3.8.png)

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img3.9.png)

После чего попробуйте отключить одну из нод, желательно ту, к которой подключались из скрипта, затем поправьте параметры подключения в скрипте consumer.py на вторую ноду и запустите его.

*Приложите скриншот результата работы второго скрипта.*

**Перенаправил на вторую ноду**

**Скрин 10**

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img4.0.png)

## Дополнительные задания (со звёздочкой*)
Эти задания дополнительные, то есть не обязательные к выполнению, и никак не повлияют на получение вами зачёта по этому домашнему заданию. Вы можете их выполнить, если хотите глубже шире разобраться в материале.

### * Задание 4. Ansible playbook

Напишите плейбук, который будет производить установку RabbitMQ на любое количество нод и объединять их в кластер.
При этом будет автоматически создавать политику ha-all.

*Готовый плейбук разместите в своём репозитории.*

**Заработал не сразу, пришлось много покапать информации. Саму программу не сложно поставить, но чтобы подтянуть все условия, оказалось не так просто**  

[Плейбук=>](https://github.com/travickiy67/RabbitMQ/blob/main/files/rabbitmq.yml)  

**Скрин 1-3**  

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img5.0.png)

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img5.1.png)

![img](https://github.com/travickiy67/RabbitMQ/blob/main/img/img5.2.png)

**Обновленный playbook способный установить rabbitmq на любое количество машин. Требуется только редактирование файлов шаблонов, и связанность машин по SSH, (предпстительно). Необходимо знать IP адреса и имена машин для редактирования файлов шаблона.**  

[Playbook_update](https://github.com/travickiy67/RabbitMQ/tree/main/update_playbook)
