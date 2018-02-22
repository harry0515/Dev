def openManageUsers(self):
    try:
        browser = self.browser
        userMenuHead = browser.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right']")
        span = userMenuHead.find_element_by_xpath("//span[@trees='navCtrl.menu_right']")
        li = span.find_element_by_tag_name('li')
        userBtn = li.find_element_by_tag_name('a')
        userBtn.click()
        time.sleep(2)
        dropDownMenu = li.find_element_by_tag_name('ul')
        leafMenus = dropDownMenu.find_elements_by_tag_name('li')
        for leafMenu in leafMenus:
            softwareUpdateMenu = leafMenu.find_element_by_tag_name('a')
            if 'usermgmt' in softwareUpdateMenu.get_attribute('href'):
                softwareUpdateMenu.click()
                break
        time.sleep(5)
        strSrc = browser.page_source
        if 'Manage Users' in strSrc:
            return ["PASSED", True]
        else:
            return ["FAILED", False]

    except Exception as e:
        self.log.error('Unable to open admin page %s' % e)
        return ["FAILED", False]


def getStatus(self):
    browser = self.browser
    try:
        strStatus = browser.find_element_by_id('user_form_msg').text
    except Exception as e:
        self.log.error('Unable to get status %s' % e)
    return strStatus


def clickOnNgClick(self, string):
    browser = self.browser
    try:
        button = browser.find_element_by_xpath("//button[@ng-click='%s']" % string)
        button.click()
    except Exception as e:
        self.log.error('Unable to click' % e)


def clickOncVuProvisionBtn(self):
    self.clickOnNgClick('users.clickProvision()')


def clickOncVuAddUserBtn(self):
    self.clickOnNgClick('users.addUser()')


def clickOncVuSaveAllBtn(self):
    self.clickOnNgClick('users.saveAll()')


def clickOncVuDeprovisionBtn(self):
    self.clickOnNgClick('users.clickDeprovision()')


def clickOncVuExportBtn(self):
    self.clickOnNgClick('users.exportUsers()')


def clickOncVuImportBtn(self):
    self.clickOnNgClick('users.clickImport()')


def clickOncVuDeleteBtn(self):
    self.clickOnNgClick('users.deleteManyUsers()')


def clickOncVuConsoleBtn(self):
    self.clickOnNgClick('users.consoleLogOpen = !users.consoleLogOpen')


def clickSelectAllCheckBox(self):
    browser = self.browser
    try:
        selectCB = browser.find_element_by_xpath('//input[@ng-change="users.selectAll()"]')
        selectCB.click()
    except Exception as e:
        self.log.error('Unable to click select check box %s' % e)


def findcVuUser(self, user):
    browser = self.browser
    names = []
    try:
        username = browser.find_elements_by_xpath('//td[@ng-bind="user.username"]')
        for nam in username:
            name = nam.text
            names.append(name)
        if user in names:
            return True
        return False
    except Exception as e:
        self.log.error('Unable to find username %s' % e)
        return False


def clickOncVuUserSelectBtn(self, user):
    browser = self.browser
    try:
        num = int(self.userNameToNumber(user))
        time.sleep(1)
        tbody = browser.find_elements_by_tag_name("tbody")
        tr = tbody[0].find_elements_by_tag_name("tr")
        td = tr[num].find_elements_by_tag_name("td")
        input = td[1].find_element_by_tag_name("input")
        input.click()
        return True
    except Exception as e:
        self.log.error('Unable to click select btn %s' % e)
        return False


def userNameToNumber(self, user):
    browser = self.browser
    names = {}
    i = 0
    try:
        username = browser.find_elements_by_xpath('//td[@ng-bind="user.username"]')
        for nam in username:
            name = nam.text
            names[name] = i
            i = i + 1
        return names[user]
    except Exception as e:
        self.log.error('Unable to change username to number %s' % e)
        return False


def clickOncVuUserEditBtn(self, user):
    browser = self.browser
    try:
        num = int(self.userNameToNumber(user))
        time.sleep(1)
        tbody = browser.find_elements_by_tag_name("tbody")
        tr = tbody[0].find_elements_by_tag_name("tr")
        td = tr[num].find_elements_by_tag_name("td")
        input = td[7].find_elements_by_tag_name("i")
        input[0].click()
        return True
    except Exception as e:
        self.log.error('Unable to click on cVu user edit button %s' % e)
        return False


def clickOncVuUserDeleteBtn(self, user):
    browser = self.browser
    try:
        num = int(self.userNameToNumber(user))
        time.sleep(1)
        tbody = browser.find_elements_by_tag_name("tbody")
        tr = tbody[0].find_elements_by_tag_name("tr")
        td = tr[num].find_elements_by_tag_name("td")
        input = td[7].find_elements_by_tag_name("i")
        input[1].click()
        return True
    except Exception as e:
        self.log.error('Unable to click on cVu user delete button %s' % e)
        return False


def clickOncVuUserSaveBtn(self, user):
    browser = self.browser
    try:
        num = int(self.userNameToNumber(user))
        time.sleep(1)
        tbody = browser.find_elements_by_tag_name("tbody")
        tr = tbody[0].find_elements_by_tag_name("tr")
        td = tr[num].find_elements_by_tag_name("td")
        input = td[7].find_elements_by_tag_name("i")
        input[0].click()
        return True
    except Exception as e:
        self.log.error('Unable to click on cVu user save button %s' % e)
        return False


def selectcVuUserAuthentication(self, authenticate, user=None):
    browser = self.browser
    try:
        if user == None:
            num = 0
        else:
            num = int(self.userNameToNumber(user))
            time.sleep(1)
        tbody = browser.find_elements_by_tag_name("tbody")
        tr = tbody[0].find_elements_by_tag_name("tr")
        td = tr[num].find_elements_by_tag_name("td")
        select = Select(td[3].find_element_by_tag_name("select"))
        select.select_by_visible_text(authenticate)
        return True
    except Exception as e:
        self.log.error('Unable to select cVu user authentication %s' % e)
        return False


def selectcVuUserRole(self, level, user=None):
    browser = self.browser
    try:
        if user == None:
            num = 0
        else:
            num = int(self.userNameToNumber(user))
            time.sleep(1)
        tbody = browser.find_elements_by_tag_name("tbody")
        tr = tbody[0].find_elements_by_tag_name("tr")
        td = tr[num].find_elements_by_tag_name("td")
        select = Select(td[4].find_element_by_tag_name("select"))
        select.select_by_visible_text(level)
        return True
    except Exception as e:
        self.log.error('Unable to select cVu user Role %s' % e)
        return False


def clickOncVuUserPortsBtn(self, user=None):
    browser = self.browser
    try:
        if user == None:
            num = 0
        else:
            num = int(self.userNameToNumber(user))
            time.sleep(1)
        tbody = browser.find_elements_by_tag_name("tbody")
        tr = tbody[0].find_elements_by_tag_name("tr")
        td = tr[num].find_elements_by_tag_name("td")
        button = td[5].find_element_by_tag_name("button")
        button.click()
        return True
    except Exception as e:
        self.log.error('Unable to click on cVu user port button %s' % e)
        return False


def clickOncVuUserPortSelectDeselectBtn(self, ports, user=None):
    browser = self.browser
    try:
        if user == None:
            num = 0
        else:
            num = int(self.userNameToNumber(user))
            time.sleep(1)
        tbody = browser.find_elements_by_tag_name("tbody")
        tr = tbody[0].find_elements_by_tag_name("tr")
        td = tr[num].find_elements_by_tag_name("td")
        div = td[5].find_element_by_tag_name("div")
        if ports == "selectAll":
            select = div.find_element_by_xpath("//div[2]/div/div/port-select/div[1]/div[1]/button[1]")
            select.click()
            time.sleep(1)
            done = div.find_element_by_xpath("//div[2]/div/div/port-select/div[2]/div/button")
            done.click()
            return True
        if ports == "deselectAll":
            select = div.find_element_by_xpath("//div[2]/div/div/port-select/div[1]/div[1]/button[2]")
            select.click()
            time.sleep(1)
            done = div.find_element_by_xpath("//div[2]/div/div/port-select/div[2]/div/button")
            done.click()
            return True
        return False
    except Exception as e:
        self.log.error('Unable to click on cVu user port select deselect button %s' % e)
        return False


def clickOncVuUserPortDeselect(self, user=None):
    browser = self.browser
    try:
        if user == None:
            num = 0
        else:
            num = int(self.userNameToNumber(user))
            time.sleep(1)
        tbody = browser.find_elements_by_tag_name("tbody")
        tr = tbody[0].find_elements_by_tag_name("tr")
        td = tr[num].find_elements_by_tag_name("td")
        div = td[5].find_element_by_tag_name("div")
        select = div.find_element_by_xpath("//div[2]/div/div/port-select/div[1]/div[1]/button[2]")
        select.click()
    except Exception as e:
        self.log.error('Unable to click on cVu user port select deselect button %s' % e)
        return False


def clickOnPortDone(self, user):
    browser = self.browser
    try:
        if user == None:
            num = 0
        else:
            num = int(self.userNameToNumber(user))
            time.sleep(1)
        tbody = browser.find_elements_by_tag_name("tbody")
        tr = tbody[0].find_elements_by_tag_name("tr")
        td = tr[num].find_elements_by_tag_name("td")
        div = td[5].find_element_by_tag_name("div")
        done = div.find_element_by_xpath("//div[2]/div/div/port-select/div[2]/div/button")
        done.click()
        return True
    except Exception as e:
        self.log.error('Unable to click on cVu user port select deselect button %s' % e)
        return False


def selectIndividualPorts(self, portList, user=None):
    browser = self.browser
    try:
        if user == None:
            num = 0
        else:
            num = int(self.userNameToNumber(user))
            time.sleep(1)
            num = num

        for port in portList:
            prt = int(port)
            if prt % 6 == 0:
                row = prt / 6
                row = row + 1
                body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
                div = body.find_element_by_xpath("//div[@ng-if='mc.features.maintenance']")
                form = div.find_element_by_xpath("//form[@name='usersForm']")
                tbody = form.find_element_by_tag_name("tbody")
                tr = tbody.find_elements_by_tag_name("tr")
                td = tr[num].find_elements_by_tag_name("td")
                portSelect = td[5].find_element_by_xpath("//port-select[@class='ng-scope ng-isolate-scope']")
                input = portSelect.find_element_by_xpath("//div[1]/div[%d]/div[6]/span/input" % row)
                # input = browser.find_element_by_xpath(
                #     "html/body/div/div/div[2]/form/table/tbody/tr[%d]/td[6]/div/div[2]/div/div/port-select/div[1]/div[%d]/div[6]/span/input" % (
                #         num, row))
                input.click()
                # time.sleep(1)
            else:
                row, cln = divmod(prt, 6)
                row = row + 2
                body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
                div = body.find_element_by_xpath("//div[@ng-if='mc.features.maintenance']")
                form = div.find_element_by_xpath("//form[@name='usersForm']")
                tbody = form.find_element_by_tag_name("tbody")
                tr = tbody.find_elements_by_tag_name("tr")
                td = tr[num].find_elements_by_tag_name("td")
                portSelect = td[5].find_element_by_xpath("//port-select[@class='ng-scope ng-isolate-scope']")
                input = portSelect.find_element_by_xpath("//div[1]/div[%d]/div[%d]/span/input" % (row, cln))
                # input = browser.find_element_by_xpath(
                #     "html/body/div/div/div[2]/form/table/tbody/tr[%d]/td[6]/div/div[2]/div/div/port-select/div[1]/div[%d]/div[%d]/span/input" % (
                #         num, row, cln))
                input.click()
                # time.sleep(1)
        self.clickOnPortDone(user)
    except Exception as e:
        self.log.error('Unable to click on cVu user ports %s' % e)
        return False


# def addcVuUserSuccessMessage(self, user):
#     browser = self.browser
#     try:
#         toast = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]")
#         strText = toast.text
#         print strText
#         if strText == "Saved user" + user:
#             return True
#         return False
#     except Exception as e:
#         self.log.error('Unable to display success message %s' % e)
#         return False
#
# def deletecVuUserSuccessMessage(self, user):
#     browser = self.browser
#     try:
#         toast = browser.find_element_by_xpath("//div[@class='toast toast-success']")
#         msg = toast.find_element_by_xpath("//div[@class='toast-message']")
#         time.sleep(2)
#         strText = msg.text
#         if strText == "Deleted user" + user:
#             return True
#         return False
#     except Exception as e:
#         self.log.error('Unable to display success message %s' % e)
#         return False
#################################### add cVu User ##########################
def addcVuUserUsername(self, user):
    browser = self.browser
    try:
        table = browser.find_element_by_tag_name("table")
        tbody = table.find_elements_by_tag_name("tbody")
        tr = tbody[0].find_element_by_tag_name("tr")
        td = tr.find_elements_by_tag_name("td")
        nameIn = td[2].find_element_by_tag_name("input")
        nameIn.clear()
        nameIn.send_keys(user)
        return True
    except Exception as e:
        self.log.error('Unable to add username %s' % e)
        return False


def addcVuUser(self, user, authentication, level, portList):
    browser = self.browser
    errorString = ''
    errorCount = 0
    try:
        time.sleep(2)
        self.clickOncVuAddUserBtn()
        time.sleep(1)
        self.addcVuUserUsername(user)
        time.sleep(1)
        self.selectcVuUserAuthentication(authentication)
        time.sleep(1)
        self.selectcVuUserRole(level)
        time.sleep(1)
        self.clickOncVuUserPortsBtn()
        time.sleep(2)
        self.clickOncVuUserPortDeselect()
        time.sleep(2)
        self.selectIndividualPorts(portList)
        time.sleep(2)
        tbody = browser.find_elements_by_tag_name("tbody")
        tr = tbody[0].find_elements_by_tag_name("tr")
        td = tr[0].find_elements_by_tag_name("td")
        input = td[7].find_elements_by_tag_name("button")
        input[0].click()
        time.sleep(3)
        if self.findcVuUser(user):
            return ["Adding cVu user successful", True]
        return ["Adding cVu user Failed", False]
    except Exception as e:
        self.log.error('Unable to add cVu users %s' % e)
        errorString += "Unable to add cVu user"
        errorCount += 1
        return [errorString, False]


def addcVuUserAllPorts(self, user, authentication, level, ports):
    browser = self.browser
    errorString = ''
    errorCount = 0
    try:
        time.sleep(2)
        self.clickOncVuAddUserBtn()
        time.sleep(1)
        self.addcVuUserUsername(user)
        time.sleep(1)
        self.selectcVuUserAuthentication(authentication)
        time.sleep(1)
        self.selectcVuUserRole(level)
        time.sleep(1)
        self.clickOncVuUserPortsBtn()
        time.sleep(2)
        self.clickOncVuUserPortSelectDeselectBtn(ports)
        time.sleep(2)
        tbody = browser.find_elements_by_tag_name("tbody")
        tr = tbody[0].find_elements_by_tag_name("tr")
        td = tr[0].find_elements_by_tag_name("td")
        input = td[7].find_elements_by_tag_name("button")
        input[0].click()
        time.sleep(2)
        if self.findcVuUser(user):
            return ["Adding cVu user successful", True]
        return ["Adding cVu user Failed", False]
    except Exception as e:
        self.log.error('Unable to add cVu users %s' % e)
        errorString += "Unable to add cVu user"
        errorCount += 1
        return [errorString, False]


def addcVuUserAllTypes(self, user, ports):
    browser = self.browser
    errorString = ''
    errorCount = 0
    try:
        time.sleep(2)
        userList = user
        i = 0
        authentication = ["RADIUS", "TACACS+"]
        level = ['Admin', 'L1', 'L2', 'L3', 'L3 Restricted']
        for auth in authentication:
            for lv in level:
                self.clickOncVuAddUserBtn()
                time.sleep(1)
                self.addcVuUserUsername(userList[i])
                time.sleep(1)
                self.selectcVuUserAuthentication(auth)
                time.sleep(1)
                self.selectcVuUserRole(lv)
                time.sleep(1)
                self.clickOncVuUserPortsBtn()
                time.sleep(2)
                self.clickOncVuUserPortSelectDeselectBtn(ports)
                time.sleep(2)
                tbody = browser.find_elements_by_tag_name("tbody")
                tr = tbody[0].find_elements_by_tag_name("tr")
                td = tr[0].find_elements_by_tag_name("td")
                input = td[7].find_elements_by_tag_name("button")
                input[0].click()
                i = i + 1
                time.sleep(2)
        return ["PASSED", True]
    except Exception as e:
        self.log.error('Unable to add cVu users %s' % e)
        errorString += "Unable to add cVu user"
        errorCount += 1
        return [errorString, False]


###################### provision and Deprovision##############################################
def selectcVuProDepro(self, cVuNames):
    browser = self.browser
    try:
        body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
        div = body.find_element_by_xpath("//div[@class='modal fade ng-isolate-scope in']")
        div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
        div2 = div1.find_element_by_class_name("modal-body")
        form = div2.find_element_by_tag_name("form")
        table = form.find_elements_by_tag_name("table")
        tbody = table[0].find_elements_by_tag_name("tbody")
        tr = tbody[1].find_elements_by_tag_name("tr")
        time.sleep(1)
        IPs = {}
        i = 0
        for trs in tr:
            cVuIPs = trs.find_elements_by_tag_name("td")
            str1 = str(cVuIPs[1].text)
            IPs[str1] = i
            i = i + 1
        for cVuName in cVuNames:
            td = tr[int(IPs[cVuName])].find_elements_by_tag_name("td")
            input = td[0].find_element_by_tag_name("input")
            input.click()
            # time.sleep(1)
    except Exception as e:
        self.log.error('Unable to click cVu provision and deprovision %s' % e)
        return False


def selectcStorProDepro(self, cStorNames):
    browser = self.browser
    try:
        body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
        div = body.find_element_by_xpath("//div[@class='modal fade ng-isolate-scope in']")
        div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
        div2 = div1.find_element_by_class_name("modal-body")
        form = div2.find_element_by_tag_name("form")
        table = form.find_elements_by_tag_name("table")
        tbody = table[1].find_elements_by_tag_name("tbody")
        tr = tbody[1].find_elements_by_tag_name("tr")
        time.sleep(1)
        # tr = browser.find_elements_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/form/table[2]/tbody[2]/tr")
        IPs = {}
        i = 0
        for trs in tr:
            cStorIPs = trs.find_elements_by_tag_name("td")
            str1 = str(cStorIPs[1].text)
            IPs[str1] = i
            i = i + 1
        for cStorName in cStorNames:
            td = tr[int(IPs[cStorName])].find_elements_by_tag_name("td")
            input = td[0].find_element_by_tag_name("input")
            input.click()
            # time.sleep(1)
    except Exception as e:
        self.log.error('Unable to click cVu provision deprovision  %s' % e)
        return False


def selectLocalcClearProDepro(self):
    browser = self.browser
    try:
        input = browser.find_element_by_xpath("//input[@ng-model='vm.cclearSelected']")
        input.click()
        return True
    except Exception as e:
        self.log.error('Unable to click on local cClear provision deprovision  %s' % e)
        return False


def clickOnAcceptProDepro(self):
    browser = self.browser
    try:
        body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
        div = body.find_element_by_xpath("//div[@class='modal fade ng-isolate-scope in']")
        div1 = div.find_element_by_xpath("//div[@class='modal-content']")
        div2 = div1.find_element_by_xpath("//div[@class='modal-footer']")
        input = div2.find_element_by_xpath("//button[@class='btn btn-success ng-binding']")
        # input = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[3]/button[1]")
        input.click()
        return True
    except Exception as e:
        self.log.error('Unable to click accept provision deprovision  %s' % e)
        return False


def selectAllcStorProDepro(self):
    browser = self.browser
    try:
        body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
        div = body.find_element_by_xpath("//div[@class='modal fade ng-isolate-scope in']")
        div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
        div2 = div1.find_element_by_class_name("modal-body")
        form = div2.find_element_by_tag_name("form")
        table = form.find_elements_by_tag_name("table")
        tbody = table[1].find_elements_by_tag_name("tbody")
        tr = tbody[1].find_elements_by_tag_name("tr")
        # tr = browser.find_elements_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/form/table[2]/tbody[2]/tr")
        IPs = {}
        i = 0
        for trs in tr:
            cStoreIPs = trs.find_elements_by_tag_name("td")
            str1 = str(cStoreIPs[2].text)
            IPs[i] = str1
            i = i + 1
        print IPs[2]
        time.sleep(1)
        for ip in IPs:
            self.selectcStorProDepro(IPs[ip])
        return True
    except Exception as e:
        self.log.error('Unable to select all cStor provision and deprovision %s' % e)
        return False


def selectAllcVuProDepro(self):
    browser = self.browser
    try:
        body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
        div = body.find_element_by_xpath("//div[@class='modal fade ng-isolate-scope in']")
        div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
        div2 = div1.find_element_by_class_name("modal-body")
        form = div2.find_element_by_tag_name("form")
        table = form.find_elements_by_tag_name("table")
        tbody = table[0].find_elements_by_tag_name("tbody")
        tr = tbody[1].find_elements_by_tag_name("tr")
        # tr = browser.find_elements_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/form/table[1]/tbody[2]/tr")
        IPs = {}
        i = 0
        for trs in tr:
            cVuIPs = trs.find_elements_by_tag_name("td")
            str1 = str(cVuIPs[2].text)
            IPs[i] = str1
            i = i + 1
        print IPs[2]
        time.sleep(1)
        for ip in IPs:
            self.selectcVuProDepro(IPs[ip])
        return True
    except Exception as e:
        self.log.error('Unable to select all cVu provision and deprovision %s' % e)
        return False


def cVuProvisionMltplDevices(self, user, cVuNames, cStorNames, cClear):
    errorString = ''
    try:
        time.sleep(5)
        if self.findcVuUser(user):
            self.clickOncVuUserSelectBtn(user)
            time.sleep(2)
            self.clickOncVuProvisionBtn()
            time.sleep(3)
            if (cVuNames or cStorNames) and cClear:
                self.selectcVuProDepro(cVuNames)
                time.sleep(1)
                self.selectcStorProDepro(cStorNames)
                time.sleep(1)
                self.selectLocalcClearProDepro()
                time.sleep(1)
                self.clickOnAcceptProDepro()
                time.sleep(1)
                self.clickOncVuUserSelectBtn(user)
                time.sleep(5)
                if self.getcVuUserConsoleDataProvison(user, cVuNames, cStorNames):
                    self.clickOncVuConsoleBtn()
                    return ["cVu Provision successful", True]
                self.clickOncVuConsoleBtn()
                return ["cVu Provision Failed", False]
            if (cVuNames or cStorNames):
                self.selectcVuProDepro(cVuNames)
                time.sleep(1)
                self.selectcStorProDepro(cStorNames)
                time.sleep(1)
                self.clickOnAcceptProDepro()
                time.sleep(1)
                self.clickOncVuUserSelectBtn(user)
                time.sleep(5)
                if self.getcVuUserConsoleDataProvison(user, cVuNames, cStorNames):
                    self.clickOncVuConsoleBtn()
                    return ["cVu Provision successful", True]
                self.clickOncVuConsoleBtn()
                return ["cVu Provision Failed", False]
            return ["FAILED", False]
        else:
            self.log.error(" No cVu user")
            return ["FAILED", False]
    except Exception as e:
        self.log.error('Unable to perform cVu user provision %s' % e)
        errorString += "Unable to perform cVu user provision"
        return [errorString, False]


def cVuDeprovisionMltplDevices(self, user, cVuNames, cStorNames, cClear):
    errorString = ''
    try:
        time.sleep(5)
        if self.findcVuUser(user):
            self.clickOncVuUserSelectBtn(user)
            time.sleep(2)
            self.clickOncVuDeprovisionBtn()
            time.sleep(3)
            if (cVuNames or cStorNames) and cClear:
                self.selectcVuProDepro(cVuNames)
                time.sleep(1)
                self.selectcStorProDepro(cStorNames)
                time.sleep(1)
                self.selectLocalcClearProDepro()
                time.sleep(1)
                self.clickOnAcceptProDepro()
                time.sleep(2)
                self.clickOncVuUserSelectBtn(user)
                time.sleep(5)
                if self.getcVuUserConsoleDataDeprovison(user, cVuNames, cStorNames):
                    self.clickOncVuConsoleBtn()
                    return ["cVu Deprovision successful", True]
                self.clickOncVuConsoleBtn()
                return ["cVu Deprovision Failed", False]
            if (cVuNames or cStorNames):
                self.selectcVuProDepro(cVuNames)
                time.sleep(1)
                self.selectcStorProDepro(cStorNames)
                time.sleep(1)
                self.clickOnAcceptProDepro()
                time.sleep(1)
                self.clickOncVuUserSelectBtn(user)
                time.sleep(5)
                if self.getcVuUserConsoleDataDeprovison(user, cVuNames, cStorNames):
                    self.clickOncVuConsoleBtn()
                    return ["cVu Deprovision successful", True]
                self.clickOncVuConsoleBtn()
                return ["cVu Deprovision Failed", False]
            return ["FAILED", False]
        else:
            self.log.error(" No cVu user")
            return ["FAILED", False]
    except Exception as e:
        self.log.error('Unable to perform cVu user Deprovision %s' % e)
        errorString += "Unable to perform cVu user Deprovision"
        return [errorString, False]


def getcVuUserConsoleDataProvison(self, user, cVuNames, cStorNames):
    try:
        errorcount = 0
        self.clickOncVuConsoleBtn()
        time.sleep(3)
        msg = self.getcVuUserConsoleData()
        string = []
        if cVuNames:
            for device in cVuNames:
                string1 = "Provision/Update [" + user + "] on cVu [" + device + "]: OK"
                string.append(string1)
                if not string1 in msg:
                    errorcount += 1
        if cStorNames:
            for device in cStorNames:
                string1 = "Provision/Update [" + user + "] on [" + device + "]: OK"
                string.append(string1)
                if not string1 in msg:
                    errorcount += 1
        if errorcount > 0:
            return False
        else:
            return True
    except Exception as e:
        self.log.error('error in device provision or deprovision %s' % e)
        return False


def getcVuUserConsoleData(self):
    browser = self.browser
    try:
        body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
        div = body.find_element_by_xpath("//div[@ng-if='mc.features.maintenance']")
        div1 = div.find_element_by_xpath("//div[@popup-class='consolelog']")
        table = div1.find_element_by_xpath("//table[@class='consolelog table-striped']")
        trs = table.find_elements_by_tag_name("tr")
        # trs = browser.find_elements_by_xpath(
        #     "/html/body/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/table/tbody/tr")
        time.sleep(2)
        msg = []
        for tr in trs[:100]:
            td = tr.find_elements_by_tag_name("td")
            str1 = td[1].text
            msg.append(str(str1))
        return msg
    except Exception as e:
        self.log.error('error in device provision or deprovision %s' % e)
        return False


def getcVuUserConsoleDataDeprovison(self, user, cVuNames, cStorNames):
    try:
        errorcount = 0
        self.clickOncVuConsoleBtn()
        time.sleep(3)
        msg = self.getcVuUserConsoleData()
        string = []
        if cVuNames:
            for device in cVuNames:
                string1 = "Deprovision [" + user + "] on cVu [" + device + "]: OK"
                string.append(string1)
                if not string1 in msg:
                    errorcount += 1
        if cStorNames:
            for device in cStorNames:
                string1 = "Deprovision [" + user + "] on [" + device + "]: OK"
                string.append(string1)
                if not string1 in msg:
                    errorcount += 1
        if errorcount > 0:
            return False
        else:
            return True
    except Exception as e:
        self.log.error('error in device provision or deprovision %s' % e)
        return False


################################### cVu user edit#####################################################
def editcVuUserAllPorts(self, user, authenticate, level, ports):
    errorString = ''
    try:
        time.sleep(2)
        self.clickOncVuUserEditBtn(user)
        time.sleep(1)
        self.selectcVuUserAuthentication(authenticate, user)
        time.sleep(1)
        self.selectcVuUserRole(level, user)
        time.sleep(1)
        self.clickOncVuUserPortsBtn(user)
        time.sleep(2)
        self.clickOncVuUserPortSelectDeselectBtn(ports, user)
        time.sleep(1)
        self.clickOncVuUserSaveBtn(user)
        time.sleep(5)
        userDict = self.getcVuUserInfo(user)
        time.sleep(2)
        actualDict = userDict[user]
        if actualDict['Authenticate'] == str(authenticate.lower()) and actualDict['Level'] == level:
            return ["Editing cVu user successful", True]
        return ["Editing cVu user Failed", False]
    except Exception as e:
        self.log.error('Unable to perform cVu user edit %s' % e)
        errorString += "Unable to edit cVu user"
        return [errorString, False]


def editcVuUser(self, user, authenticate, level, portList):
    errorString = ''
    try:
        time.sleep(2)
        self.clickOncVuUserEditBtn(user)
        time.sleep(1)
        self.selectcVuUserAuthentication(authenticate, user)
        time.sleep(1)
        self.selectcVuUserRole(level, user)
        time.sleep(1)
        self.clickOncVuUserPortsBtn(user)
        time.sleep(2)
        self.clickOncVuUserPortDeselect(user)
        time.sleep(1)
        self.selectIndividualPorts(portList, user)
        time.sleep(1)
        self.clickOncVuUserSaveBtn(user)
        time.sleep(5)
        if self.checkUserInfo(user, authenticate, level, portList):
            return ["Editing cVu user successful", True]
        return ["Editing cVu user Failed", False]
    except Exception as e:
        self.log.error('Unable to perform cVu user edit %s' % e)
        errorString += "Unable to edit cVu user"
        return [errorString, False]


########################### cVu user export##########################


def exportcVuUsers(self, user, filePath):
    browser = self.browser
    errorCount = 0
    errorMsg = ''
    try:
        time.sleep(3)
        self.clickOncVuUserSelectBtn(user)
        time.sleep(1)
        self.clickOncVuExportBtn()
        time.sleep(10)
        actualUser = self.getcVuUserInfo(user)
        time.sleep(3)
        file = self.getLatestcVuUserFileName(filePath)
        userInfoDict = self.readcVuUserFile(file)
        time.sleep(3)
        self.clickOncVuUserSelectBtn(user)
        # compare the user info with the one in the exported file
        for key in userInfoDict:
            actualDict = actualUser[key]
            userDict = userInfoDict[key]

            for key in userDict:
                if key == 'Ports':
                    portList = actualDict[key]
                    strPort = ",".join(portList)
                    if userDict[key] not in strPort:
                        errorCount += 1
                        errorMsg += "Incorrect user info " + userDict[key] + "\n"
                else:
                    if actualDict[key] != userDict[key]:
                        errorCount += 1
                        errorMsg += "Incorrect user info " + userDict[key] + "\n"

        if errorCount > 0:
            return [errorMsg, False]
        else:
            return ["Exporting cVu User successful", True]
    except Exception as e:
        self.log.error('Unable to export cVu Users %s' % e)
        return ["Error: [spifeeWeb exportcVuUsers] Unable to process.", False]


def checkUserInfo(self, user, authentication, level, portList):
    browser = self.browser
    try:
        userDict = self.getcVuUserInfo(user)
        time.sleep(2)
        actualDict = userDict[user]
        if actualDict['Authenticate'] == str(authentication.lower()) and actualDict['Level'] == level and set(
                actualDict["Ports"]) == set(portList):
            return True
        return False
    except Exception as e:
        self.log.error('Unable to checkUserInfo %s' % e)
        return False


def getcVuUserInfo(self, user):
    browser = self.browser
    userDict = {}
    infoDict = {}

    try:
        num = int(self.userNameToNumber(user))
        time.sleep(1)
        body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
        div = body.find_element_by_xpath("//div[@ng-if='mc.features.maintenance']")
        form = div.find_element_by_xpath("//form[@name='usersForm']")
        tbody = form.find_element_by_tag_name("tbody")
        tr = tbody.find_elements_by_tag_name("tr")
        # tr = browser.find_elements_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr")
        td = tr[num].find_elements_by_tag_name("td")
        userName = td[2].text
        authenticate = td[3].text
        level = td[4].text
        # status = td[6].find_element_by_class_name('status-div').text
        # time.sleep(2)
        infoDict['Authenticate'] = str(authenticate.lower())
        infoDict['Level'] = str(level)
        # time.sleep(2)
        infoDict['Ports'] = self.getcVuPortInfo(user)
        # infoDict['Status'] = status
        # time.sleep(5)
        userDict[str(userName)] = infoDict
    except NoSuchElementException as e:
        self.log.error('Unable to get cVu User info %s' % e)

    return userDict


def getcVuAllUserInfo(self):
    browser = self.browser
    userDict = {}

    try:
        body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
        div = body.find_element_by_xpath("//div[@ng-if='mc.features.maintenance']")
        form = div.find_element_by_xpath("//form[@name='usersForm']")
        tbody = form.find_element_by_tag_name("tbody")
        tr = tbody.find_elements_by_tag_name("tr")
        length = len(tr)
        # tr = browser.find_elements_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr")
        for num in range(length):
            infoDict = {}
            td = tr[num].find_elements_by_tag_name("td")
            userName = td[2].text
            authenticate = td[3].text
            level = td[4].text
            infoDict['Authenticate'] = str(authenticate.lower())
            infoDict['Level'] = str(level)
            infoDict['Ports'] = self.getcVuPortInfo(str(userName))
            userDict[str(userName)] = infoDict
    except NoSuchElementException as e:
        self.log.error('Unable to get cVu User info %s' % e)

    return userDict


def getcVuPortInfo(self, user):
    browser = self.browser
    portList = []
    try:
        num = int(self.userNameToNumber(user))
        time.sleep(1)
        body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
        div = body.find_element_by_xpath("//div[@ng-if='mc.features.maintenance']")
        form = div.find_element_by_xpath("//form[@name='usersForm']")
        tbody = form.find_element_by_tag_name("tbody")
        tr = tbody.find_elements_by_tag_name("tr")
        # tr = browser.find_elements_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr")
        td = tr[num].find_elements_by_tag_name("td")
        span = td[5].find_element_by_tag_name("span")
        hov = ActionChains(browser).move_to_element(span)
        hov.perform()
        time.sleep(2)
        # tooltips = td[5].find_element_by_xpath("div[@class='popover ng-isolate-scope top fade in']")
        # popover = tooltips.find_element_by_xpath("div[@class='popover-inner']")
        # # deviceName = popover.find_element_by_xpath("h3[@ng-bind='title']").text
        # popover_content = popover.find_element_by_xpath("div[@class='popover-content']")
        # ngscope = popover_content.find_element_by_xpath("div[@class='ng-scope']")
        # # time.sleep(1)
        # spans = ngscope.find_elements_by_tag_name('span')
        spans = td[5].find_elements_by_xpath("div/div[2]/div/div/span")
        time.sleep(2)
        for span in spans:
            port = span.text.replace(',', '')
            portList.append(str(port))

        portList1 = sorted(int(i) for i in portList)
        # time.sleep(1)
        portList2 = [str(i) for i in portList1]
        # browser.switch_to.default_content()
        # time.sleep(1)
        return portList2
    except Exception as e:
        self.log.error('[getPortGroupInfoFromTable]: Unable to find web element %s' % e)
        return False


def getLatestcVuUserFileName(self, filepath):
    newestFile = max(glob.iglob(os.path.join(filepath, '*.csv')), key=os.path.getctime)
    return newestFile


def readcVuUserFile(self, file):
    userInfoDict = {}
    with open(file, 'r') as f:
        userInfoList = []
        portList = []
        userDict = {}
        read_data = f.read().lstrip()
        read_data = read_data.replace('\n', '')
        read_data = read_data.replace('"', '')
        userInfoList = read_data.split(',')
        strUser = userInfoList[0].lstrip()
        strAuthenticate = userInfoList[2].lstrip()
        userDict['Authenticate'] = strAuthenticate
        strLevel = userInfoList[4].upper().lstrip()
        userDict['Level'] = strLevel
        # The ports
        for x in range(5, len(userInfoList)):
            strPort = userInfoList[x].lstrip()
            strPort = strPort.replace('[', '')
            strPort = strPort.replace(']', '')
            portList.append(strPort)

        port = ",".join(portList)
        userDict['Ports'] = port
        userInfoDict[strUser] = userDict
    f.close()

    return userInfoDict


#################### cVu user import ##########################


def importcVuUsers(self, file):
    errorCount = 0
    errorMsg = ''
    browser = self.browser
    try:
        time.sleep(2)
        userInfoDict = self.readcVuUserFile(file)
        time.sleep(2)
        self.clickOncVuImportBtn()
        time.sleep(1)
        div = browser.find_element_by_xpath("//div[@class='modal-content']")
        form = div.find_element_by_xpath("//form[@name='importUsers']")
        browse = form.find_element_by_tag_name('input')
        browse.send_keys(file)
        time.sleep(1)
        modalDlg = div.find_element_by_xpath("//div[@class='modal-footer']")
        button = modalDlg.find_element_by_tag_name('button')
        button.click()
        time.sleep(1)
        div1 = browser.find_element_by_xpath("//div[@class='modal-content']")
        modalDlg1 = div1.find_element_by_xpath("//div[@class='modal-footer']")
        button1 = modalDlg1.find_element_by_tag_name('button')
        button1.click()
        time.sleep(10)
        # for user in userInfoDict:
        #     userDict = self.getcVuUserInfo(user)
        #     time.sleep(2)
        #     actualDict = userDict[user]
        #     print actualDict
        #     userInfoDict1 = userInfoDict[user]
        #     print userInfoDict1
        #     if actualDict['Authenticate'] == userInfoDict1['Authenticate'] and actualDict['Level'] == userInfoDict1['Level'] and set(
        #             actualDict["Ports"]) == set(actualDict["Ports"]):
        #         return True
        #     return False

        for key in userInfoDict:
            uDict = self.getcVuUserInfo(key)
            time.sleep(2)
            actualDict = uDict[key]
            userDict = userInfoDict[key]
            for key in userDict:
                if key == 'Ports':
                    portList = actualDict[key]
                    strPort = ",".join(portList)
                    if userDict[key] not in strPort:
                        errorCount += 1
                        errorMsg += "Incorrect user info " + userDict[key] + "\n"
                else:
                    if actualDict[key] != userDict[key]:
                        errorCount += 1
                        errorMsg += "Incorrect user info " + userDict[key] + "\n"

        # browser.switch_to.default_content()

        if errorCount > 0:
            return [errorMsg, False]
        else:
            return ["Importing cVu User successful", True]

    except Exception as e:
        self.log.error('Unable to import cVu Users %s' % e)
        return ["Error: [spifeeWeb importcVuUsers] Unable to find web element.", False]


############################# cVu user delete all#############################################
def deletecVuUser(self, user):
    browser = self.browser
    errorCount = 0
    errorString = ''
    try:
        time.sleep(2)
        self.clickOncVuUserSelectBtn(user)
        time.sleep(1)
        self.clickOncVuDeleteBtn()
        time.sleep(4)
        if not self.findcVuUser(user):
            return ["PASSED", True]
        return ["FAILED", False]
    except Exception as e:
        self.log.error('Unable to delete %s' % e)
        errorString += "Unable to delete cVu user"
        errorCount += 1
        return [errorString, False]


def deleteAllcVuUser(self, userList):
    browser = self.browser
    errorCount = 0
    errorString = ''
    try:
        time.sleep(2)
        for user in userList:
            self.clickOncVuUserSelectBtn(user)
        time.sleep(2)
        self.clickOncVuDeleteBtn()
        time.sleep(3)
        return ["PASSED", True]
    except Exception as e:
        self.log.error('Unable to delete all  %s' % e)
        self.log.error('Unable to delete %s' % e)
        errorString += "Unable to delete cVu user"
        errorCount += 1
        return [errorString, False]


############################################## cVu search manage user#############################
def searchManageUsers(self, user):
    totalErrors = 0
    errorString = ''
    browser = self.browser
    try:
        body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
        div = body.find_element_by_xpath("//div[@ng-if='mc.features.maintenance']")
        div1 = div.find_element_by_xpath("//div[@class='col-xs-3']")
        input = div1.find_element_by_tag_name("input")
        input.clear()
        input.send_keys(user)
        form = div.find_element_by_xpath("//form[@name='usersForm']")
        tbody = form.find_element_by_tag_name("tbody")
        trs = tbody.find_elements_by_tag_name("tr")
        # trs = browser.find_elements_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr")
        names = []
        for tr in trs:
            td = tr.find_elements_by_tag_name("td")
            name = td[2].text
            names.append(name)
        if user not in names:
            errorString += "unable to search cVu user"
            totalErrors += 1
        else:
            Msg = "PASSED"
    except Exception as e:
        self.log.error('Unable to search Manage user %s' % e)
        return ["Error: search Manage User Unable to find web element.", False]
    if totalErrors > 0:
        return [errorString, False]
    else:
        time.sleep(3)
        input = browser.find_element_by_xpath("/html/body/div/div/div[1]/div/div[1]/input")
        input.clear()
        return [Msg, True]
