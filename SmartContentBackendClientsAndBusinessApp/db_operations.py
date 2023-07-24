# db_operations.py
from django.db import connection

# client
def call_insert_client(first_name, last_name, address_id, email, phone, profile_picture, user_id):
    with connection.cursor() as cursor:
        cursor.execute("CALL insert_client(%s, %s, %s, %s, %s, %s, %s)", [first_name, last_name, address_id, email, phone, profile_picture, user_id])


def call_update_client(client_id, first_name, last_name, address_id, email, phone, profile_picture, user_id):
    with connection.cursor() as cursor:
        cursor.execute("CALL update_client(%s, %s, %s, %s, %s, %s, %s, %s)", [client_id, first_name, last_name, address_id, email, phone, profile_picture, user_id])





def call_insert_industry(name):
    with connection.cursor() as cursor:
        cursor.execute("CALL insert_industry(%s)", [name])


def call_update_industry(id, name):
    with connection.cursor() as cursor:
        cursor.execute("CALL update_industry(%s, %s)", [id, name])

def call_delete_industry(id):
    with connection.cursor() as cursor:
        cursor.execute("CALL delete_industry(%s)", [id])



def call_insert_address(city, country, postal_code, street):
    with connection.cursor() as cursor:
        cursor.execute("CALL insert_address(%s, %s, %s, %s)", [city, country, postal_code, street])

def call_update_address(id, city, country, postal_code, street):
    with connection.cursor() as cursor:
        cursor.execute("CALL update_address(%s, %s, %s, %s, %s)", [id, city, country, postal_code, street])

def call_delete_address(id):
    with connection.cursor() as cursor:
        cursor.execute("CALL delete_address(%s)", [id])






def call_insert_business(name, target_audience, experience_years, reach_range, phone, 
                         address_id, website, mail, industry_id, schedule, 
                         copy_languages, client_id, mission, vision, values):
    with connection.cursor() as cursor:
        cursor.execute("CALL insert_business(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                       [name, target_audience, experience_years, reach_range, phone, 
                        address_id, website, mail, industry_id, schedule, 
                        copy_languages, client_id, mission, vision, values])
                        
def call_update_business(business_id, name, target_audience, experience_years, reach_range, phone, 
                         address_id, website, mail, industry_id, schedule, 
                         copy_languages, client_id, mission, vision, values):
    with connection.cursor() as cursor:
        cursor.execute("CALL update_business(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                       [business_id, name, target_audience, experience_years, reach_range, phone, 
                        address_id, website, mail, industry_id, schedule, 
                        copy_languages, client_id, mission, vision, values])
