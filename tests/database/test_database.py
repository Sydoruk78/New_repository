import pytest
import datetime
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")
    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1,25)
    water_qnt = db.select_product_qnt_by_id(1)
    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'qwer', 'dds', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)
    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print('Замовлення', orders)
    assert len(orders) == 1
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


@pytest.mark.ind_database
def test_insert_new_order():
    db = Database()
    db.insert_new_order(2,2,2)
    order = db.get_todays_orders()
    assert len(order) == 1
    assert order[0][0] == 2
    db.delete_new_orders()
    

@pytest.mark.ind_database
def test_float_and_negative_data_in_order():
    db = Database()
    db.insert_new_order(2,1.5,3)
    db.insert_new_order('3','4',-5)
    order = db.get_todays_orders()
    print(order)
    assert len(order) == 2
    assert order[1][0] == 4
    assert order[1][1] == -5
    assert order[0][0] == 1.5
    assert order[0][1] == 3
    db.delete_new_orders()


@pytest.mark.ind_database
def test_join_illegal_id_order():
    db = Database()
    db.insert_new_order(2,1,2)
    db.insert_new_order(3,3,3)
    order = db.get_todays_orders()
    print(order)
    orders = db.get_detailed_orders()
    print(orders)
    assert len(orders) == 2
    db.delete_new_orders()


@pytest.mark.ind_database
def test_date_in_order():
    db = Database()
    db.insert_new_order(2,2,2)
    order = db.get_todays_orders()
    today = datetime.datetime.now()
    str_today = f"{today.year}-{today.month}-{today.day}"
    assert order[0][2]==str_today
    db.delete_new_orders()
  
@pytest.mark.ind_database
def test_insert_new_product_name_int():
    db = Database()
    db.insert_product(99, 555, 'без цукру', 15)
    product = db.select_product_by_id(99)
    assert product[0][0] == '555'
    assert product[0][1] == 'без цукру'
    assert product[0][2] == 15
    db.delete_product_by_id(99)











