import pymysql

from datetime import datetime


coon = pymysql.connect(host="localhost",
                       user="nac12",
                       password="EFFECTorAF%FECT54,504",
                       db="tasksDb",
                       cursorclass=pymysql.cursors.DictCursor)

cursor = coon.cursor()


def disply_tasks(cursor=cursor):
    SQL = "SELECT * FROM tampTAsks;"
    cursor.execute(SQL)
    return cursor.fetchall()


def add_tasks(_id, title, info, date, cursor=cursor, tag=None):
    try:
        if tag == None:
            tag = "tags"
        SQl = f"INSERT INTO tampTasks(id,title, full, taskDate, tag) VALUES({_id},'{title}','{info}','{date}', '{tag}');"
        cursor.execute(SQl)
        coon.commit()
        new_task = cursor.fetchone()
        return new_task
    except:
        SQl = f"select * from tamptasks WHERE id = {_id}"
        cursor.execute(SQl)
        new_task = cursor.fetchone()
        return new_task


def delete_task(row, _id):
    try:
        SQL = f"DELETE FROM tamptasks where {row} = {_id}"
        cursor.execute(SQL)
        coon.commit()
        removed_task = cursor.fetchone()
        return removed_task
    except:
        return False


execute = cursor.execute


def modefy_task(task, row, new_data):
    data = task

    SQL = f"UPDATE tamptasks set {row} = '{new_data}' where id = '{data}'"
    cursor.execute(SQL)
    coon.commit()


def main_select(type):
    def select_by_tag(): return cursor.execute(
        "SELECT * FROM tamptasks if tag in ('soft', 'hard')")

    def select_order_by_tag(): return cursor.execute(
        " SELECT * FROM tamptasks ORDER BY tag;")

    selects_dict = {"tag select": select_by_tag,
                    "tag order": select_order_by_tag}

    value = ""

    def get_select(key):
        for k, v in selects_dict.items():
            if key == k:
                value = v

        return value

    if type == 'value':
        return get_select
    else:
        return selects_dict




def del_many(qurey_list: list, col):

    for x in qurey_list:
        delete_task(col, x["id"])

#modefy_task(task_list[0], "title", "task one was been modefy")
