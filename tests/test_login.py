from time import sleep

from pom.login import Login
from pom.emp_list import EmpList
from pom.pim import Pim
from pom.logout import Logout

def test_login(conf):
    ob = Login(conf)
    ob.enter_username()
    ob.enter_password()
    ob.click_login()

def test_pim(conf):
    pob = Pim(conf)
    pob.select_pim()
    pob.add_emp()
    pob.f_name('ragu')
    pob.l_name('varan')
    pob.e_id()
    pob.save()
    pob.add_more()
    pob.f_name('admin')
    pob.l_name('adminl')
    pob.e_id()
    pob.save()
    pob.add_more()
    pob.f_name('emp3')
    pob.l_name('emp')
    pob.e_id()
    pob.save()

def test_emp(conf):
    eob=EmpList(conf)
    eob.emp_list()
    eob.view_emp()
#
def test_logout(conf):
    l_ob=Logout(conf)
    l_ob.click_dashboard()
    sleep(1)
    l_ob.click_profile()
    sleep(1)
    l_ob.click_logout()
    sleep(1)