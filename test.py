from time import sleep
import os
import schedule

commandBase = 'python'


def job_login():
    os.system(commandBase + ' -m unittest ./Test/Login.py')


def job_admin_check_order():
    os.system(commandBase + ' -m unittest ./Test/Create_Orders/Admin_Check_Order.py')


def job_customer_manager_check_order():
    os.system(commandBase + ' -m unittest ./Test/Create_Orders/Customer_Manager_Check_Order.py')


def job_delivery_manager_check_order():
    os.system(commandBase + ' -m unittest ./Test/Create_Orders/Delivery_Manager_Check_Order.py')


def job_clearance_manager_check_order():
    os.system(commandBase + ' -m unittest ./Test/Create_Orders/Clearance_Manager_Check_Order.py')


def job_account_chain_check_order():
    os.system(commandBase + ' -m unittest ./Test/Create_Orders/Account_Chain_Check_Order.py')


def job_financial_manager_check_order():
    os.system(commandBase + ' -m unittest ./Test/Create_Orders/Financial_Manager_Check_Order.py')


def job_financial_check_order():
    os.system(commandBase + ' -m unittest ./Test/Create_Orders/Financial_Check_Order.py')


def job_account_uae_check_order():
    os.system(commandBase + ' -m unittest ./Test/Create_Orders/Account_Uae_Check_Order.py')


def job_clearance_check_order():
    os.system(commandBase + ' -m unittest ./Test/Create_Orders/Clearance_Check_Order.py')


def job_marketing_manager_check_order():
    os.system(commandBase + ' -m unittest ./Test/Create_Orders/Marketing_Manager_Check_Order.py')


def job_marketing_check_order():
    os.system(commandBase + ' -m unittest ./Test/Create_Orders/Marketing_Check_Order.py')


def job_persons():
    os.system(commandBase + ' -m unittest ./Test/Persons.py')


def job_new_persons():
    os.system(commandBase + ' -m unittest ./Test/New_Persons.py')


def job_check_wallet():
    os.system(commandBase + ' -m unittest ./Test/Financial_Manager/Check_Wallet.py')


def job_check_payment():
    os.system(commandBase + ' -m unittest ./Test/Financial_Manager/Check_Payment.py')


def job_check_warehouses_new():
    os.system(commandBase + ' -m unittest ./Test/Warehouses/Check_Warehouses_New.py')


def job_check_warehouses_old():
    os.system(commandBase + ' -m unittest ./Test/Warehouses/Check_Warehouses_Old.py')


def job_load_without_track_number():
    os.system(commandBase + ' -m unittest ./Test/Warehouses/Load_Without_Track_Number.py')


def job_warehouses_receive_confirm_box():
    os.system(commandBase + ' -m unittest ./Test/Delivery_Manager/Warehouses_Receive_Confirm_Box.py')


def job_deliver_cars():
    os.system(commandBase + ' -m unittest ./Test/Delivery_Manager/Deliver_Cars.py')


def job_latest_packages():
    os.system(commandBase + ' -m unittest ./Test/Warehouses/Latest_Packages.py')


def job_warehouses_show_op_state():
    os.system(commandBase + ' -m unittest ./Test/Delivery_Manager/Warehouses_Showopstate.py')


def job_main():
    os.system(commandBase + ' -m unittest ./Test/main.py')


def job_clearance_menu():
    os.system(commandBase + ' -m unittest ./Test/Clearance/Menu.py')


def job_financial_menu1():
    os.system(commandBase + ' -m unittest ./Test/Financial_Manager/Financial_Menu1.py')


def job_financial_menu2():
    os.system(commandBase + ' -m unittest ./Test/Financial_Manager/Financial_Menu2.py')


def job_financial_manager_menu1():
    os.system(commandBase + ' -m unittest ./Test/Financial_Manager/Menu1.py')


def job_financial_manager_menu2():
    os.system(commandBase + ' -m unittest ./Test/Financial_Manager/Menu2.py')


def job_delivery_manager_menu():
    os.system(commandBase + ' -m unittest ./Test/Delivery_Manager/Menu.py')


def job_delivery_menu():
    os.system(commandBase + ' -m unittest ./Test/Delivery_Manager/Delivery_Menu.py')


def job_manager_menu_others():
    os.system(commandBase + ' -m unittest ./Test/Delivery_Manager/Manager_Menu_Others.py')


def job_warehouses_menu():
    os.system(commandBase + ' -m unittest ./Test/Warehouses/Menu.py')


def job_crm_menu():
    os.system(commandBase + ' -m unittest ./Test/Crm/Menu.py')


def job_export_menu1():
    os.system(commandBase + ' -m unittest ./Test/Export/Menu1.py')


def job_export_menu2():
    os.system(commandBase + ' -m unittest ./Test/Export/Menu2.py')


def job_export_menu_others1():
    os.system(commandBase + ' -m unittest ./Test/Export/Menu_Others1.py')


def job_uae_menu():
    os.system(commandBase + ' -m unittest ./Test/Uae/Uae_Menu.py')


def job_uae_delivery():
    os.system(commandBase + ' -m unittest ./Test/Uae/Uae_Delivery.py')


def job_chain_financial_menu():
    os.system(commandBase + ' -m unittest ./Test/Chain/Chain_Financial_Menu.py')


def job_chain_manager_menu1():
    os.system(commandBase + ' -m unittest ./Test/Chain/Chain_Manager_Menu1.py')


def job_chain_manager_menu2():
    os.system(commandBase + ' -m unittest ./Test/Chain/Chain_Manager_Menu2.py')


def job_chain_menu1():
    os.system(commandBase + ' -m unittest ./Test/Chain/Chain_Menu1.py')


def job_chain_menu2():
    os.system(commandBase + ' -m unittest ./Test/Chain/Chain_Menu2.py')


def job_chain_warehouse_menu():
    os.system(commandBase + ' -m unittest ./Test/Chain/Chain_Warehouse_Menu.py')


def job_admin_report1():
    os.system(commandBase + ' -m unittest ./Test/Admin/Report1.py')


def job_admin_report2():
    os.system(commandBase + ' -m unittest ./Test/Admin/Report2.py')


def job_admin_report3():
    os.system(commandBase + ' -m unittest ./Test/Admin/Report3.py')


def job_admin_report4():
    os.system(commandBase + ' -m unittest ./Test/Admin/Report4.py')


def job_admin_report5():
    os.system(commandBase + ' -m unittest ./Test/Admin/Report5.py')


def job_admin_report6():
    os.system(commandBase + ' -m unittest ./Test/Admin/Report6.py')


def job_admin_report7():
    os.system(commandBase + ' -m unittest ./Test/Admin/Report7.py')


def job_admin_report8():
    os.system(commandBase + ' -m unittest ./Test/Admin/Report8.py')


job_login()
job_admin_check_order()
job_customer_manager_check_order()
job_delivery_manager_check_order()
job_clearance_manager_check_order()
job_account_chain_check_order()
job_financial_manager_check_order()
job_financial_check_order()
job_account_uae_check_order()
job_clearance_check_order()
job_marketing_manager_check_order()
job_marketing_check_order()
job_persons()
job_new_persons()
job_check_wallet()
job_check_payment()
job_check_warehouses_new()
job_check_warehouses_old()
job_load_without_track_number()
job_warehouses_receive_confirm_box()
job_deliver_cars()
job_latest_packages()
job_warehouses_show_op_state()
job_main()
job_clearance_menu()
job_financial_menu1()
job_financial_menu2()
job_financial_manager_menu1()
job_financial_manager_menu2()
job_delivery_manager_menu()
job_delivery_menu()
job_manager_menu_others()
job_warehouses_menu()
job_crm_menu()
job_export_menu1()
job_export_menu2()
job_export_menu_others1()
job_uae_menu()
job_uae_delivery()
job_chain_financial_menu()
job_chain_manager_menu1()
job_chain_manager_menu2()
job_chain_menu1()
job_chain_menu2()
job_chain_warehouse_menu()
job_admin_report1()
job_admin_report2()
job_admin_report3()
job_admin_report4()
job_admin_report5()
job_admin_report6()
job_admin_report7()

# schedule.every().day.at("09:02").do(job_login)
# schedule.every().day.at("12:00").do(job_login)
# schedule.every().day.at("12:10").do(job_new_persons)
# schedule.every().day.at("12:30").do(job_main)
# schedule.every().day.at("13:00").do(job_admin_check_order)
# schedule.every().day.at("13:30").do(job_customer_manager_check_order)
# schedule.every().day.at("14:00").do(job_clearance_manager_check_order)
# schedule.every().day.at("14:30").do(job_clearance_check_order)
# schedule.every().day.at("15:00").do(job_financial_manager_check_order)
# schedule.every().day.at("15:30").do(job_financial_check_order)
# schedule.every().day.at("16:00").do(job_check_payment)
# schedule.every().day.at("16:30").do(job_warehouses_show_op_state)
# schedule.every().day.at("17:00").do(job_main)
# schedule.every().day.at("17:30").do(job_main)

# schedule.every(30).seconds.do(job)
# schedule.every(10).minutes.do(job_login)
# schedule.every(12).minutes.do(job_new_persons)


while True:
    schedule.run_pending()
    sleep(1)
