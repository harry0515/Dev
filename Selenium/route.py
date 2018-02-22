#################################  Static Routes  ##########################################################
    def clickExpandStaticRoutes(self):
        browser = self.browser
        try:
            expandLink = browser.find_element_by_xpath("//div[@heading='Static Routes']")
            aBtn = expandLink.find_element_by_tag_name("a")
            aBtn.click()
        except Exception as e:
            self.log.error('Unable to expand Static Routes {}'.format(e))

    def clickOnAddStaticRoute(self):
        browser = self.browser
        try:
            # addRoute = browser.find_element_by_xpath("/html/body/div/uib-accordion/div/div[4]/div[2]/div/button")
            expandLink = browser.find_element_by_xpath("//div[@heading='Static Routes']")
            addRoute = expandLink.find_element_by_xpath("div[2]/div/button")
            addRoute.click()
        except Exception as e:
            self.log.error('Unable to click on add Static Routes {}'.format(e))


    def selectStaticRouteType(self,type):
        browser = self.browser
        try:
            body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
            div = body.find_element_by_xpath("div[@class='modal fade ng-isolate-scope in']")
            div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
            div2 = div1.find_element_by_class_name("modal-body")
            if type=="net":
                types = div2.find_element_by_xpath("form/fieldset/div[1]/div/div/input[1]")
                types.click()
            if type=='host':
                types = div2.find_element_by_xpath("form/fieldset/div[1]/div/div/input[2]")
                types.click()
        except Exception as e:
            self.log.error('Unable to select on Static Routes types {}'.format(e))


    def selectStaticRouteDestinationIP(self,destinationIP):
        browser = self.browser
        try:
            body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
            div = body.find_element_by_xpath("div[@class='modal fade ng-isolate-scope in']")
            div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
            div2 = div1.find_element_by_class_name("modal-body")
            dstnIP = div2.find_element_by_xpath("form/fieldset/div[2]/div[1]/input")
            # dstnIP = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/fieldset/div[2]/div[1]/input")
            dstnIP.clear()
            dstnIP.send_keys(destinationIP)
        except Exception as e:
            self.log.error('Unable to select on Static Routes destinationIP {}'.format(e))

    def msgStaticRouteDestinationIP(self):
        browser = self.browser
        try:
            body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
            div = body.find_element_by_xpath("div[@class='modal fade ng-isolate-scope in']")
            div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
            div2 = div1.find_element_by_class_name("modal-body")
            dstnIP = div2.find_element_by_xpath("form/fieldset/div[2]/div[2]/div[1]/span")
            str1 = dstnIP.text
            return str1
            # dstnIP = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/fieldset/div[2]/div[1]/input")
        except Exception as e:
            self.log.error('please enter Invalid Static Routes destinationIP {}'.format(e))
            return False

    def msgStaticRouteGatewayIP(self):
        browser = self.browser
        try:
            body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
            div = body.find_element_by_xpath("div[@class='modal fade ng-isolate-scope in']")
            div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
            div2 = div1.find_element_by_class_name("modal-body")
            dstnIP = div2.find_element_by_xpath("form/fieldset/div[4]/div/div[1]/span")
            str1 = dstnIP.text
            return str1
            # dstnIP = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/fieldset/div[2]/div[1]/input")
        except Exception as e:
            self.log.error('please enter Invalid Static Routes GatewayIP {}'.format(e))
            return False

    def msgStaticRouteSubnetMaskNum(self):
        browser = self.browser
        try:
            body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
            div = body.find_element_by_xpath("div[@class='modal fade ng-isolate-scope in']")
            div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
            div2 = div1.find_element_by_class_name("modal-body")
            dstnSbntNum = div2.find_element_by_xpath("form/fieldset/div[3]/div/div[2]/div[1]/span")
            str1 = dstnSbntNum.text
            return str1
            # dstnIP = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/fieldset/div[2]/div[1]/input")
        except Exception as e:
            self.log.error('please enter Invalid Static Routes subnet mask Num {}'.format(e))
            return False

    def msgStaticRouteSubnetMask(self):
        browser = self.browser
        try:
            body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
            div = body.find_element_by_xpath("div[@class='modal fade ng-isolate-scope in']")
            div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
            div2 = div1.find_element_by_class_name("modal-body")
            dstnSbntNum = div2.find_element_by_xpath("form/fieldset/div[3]/div/div[2]/div[2]/span")
            str1 = dstnSbntNum.text
            return str1
            # dstnIP = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/form/fieldset/div[2]/div[1]/input")
        except Exception as e:
            self.log.error('please enter Invalid Static Routes subnet mask Num {}'.format(e))
            return False

    def selectStaticRouteSubnetNum(self,destinationSbntNum):
        browser = self.browser
        try:
            body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
            div = body.find_element_by_xpath("div[@class='modal fade ng-isolate-scope in']")
            div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
            div2 = div1.find_element_by_class_name("modal-body")
            dstnSbntNum = div2.find_element_by_xpath("form/fieldset/div[3]/div/div[1]/input[1]")
            dstnSbntNum.clear()
            dstnSbntNum.send_keys(destinationSbntNum)
        except Exception as e:
            self.log.error('Unable to select on Static Routes subnet {}'.format(e))


    def selectStaticRouteSubnet(self,destinationSbnt):
        browser = self.browser
        try:
            body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
            div = body.find_element_by_xpath("div[@class='modal fade ng-isolate-scope in']")
            div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
            div2 = div1.find_element_by_class_name("modal-body")
            dstnSbnt = div2.find_element_by_xpath("form/fieldset/div[3]/div/div[1]/input[2]")
            dstnSbnt.clear()
            dstnSbnt.send_keys(destinationSbnt)
        except Exception as e:
            self.log.error('Unable to select on Static Routes subnet {}'.format(e))

    def selectStaticRouteGatewayIP(self,gatewayIP):
        browser = self.browser
        try:
            body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
            div = body.find_element_by_xpath("div[@class='modal fade ng-isolate-scope in']")
            div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
            div2 = div1.find_element_by_class_name("modal-body")
            gtway = div2.find_element_by_xpath("form/fieldset/div[4]/div/input")
            gtway.clear()
            gtway.send_keys(gatewayIP)
        except Exception as e:
            self.log.error('Unable to select on Static Routes GatewayIP {}'.format(e))

    def clickOnStaticRouteSaveButton(self):
        browser = self.browser
        try:
            body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
            div = body.find_element_by_xpath("div[@class='modal fade ng-isolate-scope in']")
            div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
            div2 = div1.find_element_by_class_name("modal-body")
            save1 = div1.find_element_by_class_name("modal-footer")
            save = save1.find_elements_by_tag_name("button")
            save[0].click()
        except Exception as e:
            self.log.error('Unable to select on Static Routes save button{}'.format(e))

    def clickOnStaticRouteCancelButton(self):
        browser = self.browser
        try:
            body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
            div = body.find_element_by_xpath("div[@class='modal fade ng-isolate-scope in']")
            div1 = div.find_element_by_xpath("//div[@class='modal-content ng-scope']")
            div2 = div1.find_element_by_class_name("modal-body")
            save1 = div1.find_element_by_class_name("modal-footer")
            save = save1.find_elements_by_tag_name("button")
            save[1].click()
        except Exception as e:
            self.log.error('Unable to select on Static Routes cancel button{}'.format(e))

    def addstaticRoutes(self,type,destinationIP,destinationSbnt,gatewayIP):
        browser = self.browser
        try:
            time.sleep(3)
            self.clickOnAddStaticRoute()
            time.sleep(2)
            self.selectStaticRouteType(type)
            time.sleep(2)
            self.selectStaticRouteDestinationIP(destinationIP)
            time.sleep(2)
            self.selectStaticRouteSubnet(destinationSbnt)
            time.sleep(2)
            self.selectStaticRouteGatewayIP(gatewayIP)
            time.sleep(2)
            self.clickOnStaticRouteSaveButton()
            time.sleep(4)
            info = self.getStaticRouteInfo()
            dict1 = info[destinationIP]
            if dict1.get("Subnet Mask") == destinationSbnt and dict1.get("Gateway IP") == gatewayIP and dict1.get(
                    "Type") == type and dict1.get("Status") == 'Set':
                return ["PASSED", True]
            return ["FAILED", False]
        except Exception as e:
            self.log.error('Unable to add Static Routes {}'.format(e))
            self.clickOnStaticRouteCancelButton()
            return ["FAILED", False]

    def addstaticRoutesNum(self,type,destinationIP,destinationSbntNum,gatewayIP):
        browser = self.browser
        try:
            CIDR = {'0':'0.0.0.0','1':'128.0.0.0','2':'192.0.0.0','3':'224.0.0.0','4':'240.0.0.0','5':'248.0.0.0','6':'252.0.0.0','7':'254.0.0.0','8':'255.0.0.0',
                    '9': '255.128.0.0','10':'255.192.0.0','11':'255.224.0.0','12':'255.240.0.0','13':'255.248.0.0','14':'255.252.0.0','15':'255.254.0.0','16':'255.255.0.0',
                    '17': '255.255.128.0','18':'255.255.192.0','19':'255.255.224.0','20':'255.255.240.0','21':'255.255.248.0','22':'255.255.252.0','23':'255.255.254.0','24':'255.255.255.0',
                    '25': '255.255.255.128','26':'255.255.255.192','27':'255.255.255.224','28':'255.255.255.240','29':'255.255.255.248','30':'255.255.255.252','31':'255.255.255.254',
                    '32':'255.255.255.255',}
            time.sleep(3)
            self.clickOnAddStaticRoute()
            time.sleep(2)
            self.selectStaticRouteType(type)
            time.sleep(2)
            self.selectStaticRouteDestinationIP(destinationIP)
            time.sleep(2)
            self.selectStaticRouteSubnetNum(destinationSbntNum)
            time.sleep(2)
            self.selectStaticRouteGatewayIP(gatewayIP)
            time.sleep(2)
            self.clickOnStaticRouteSaveButton()
            time.sleep(4)
            info = self.getStaticRouteInfo()
            dict1 = info[destinationIP]
            if dict1.get("Subnet Mask") == CIDR.get(destinationSbntNum) and dict1.get("Gateway IP") == gatewayIP and dict1.get(
                    "Type") == type and dict1.get("Status") == 'Set':
                return ["PASSED", True]
            return ["FAILED", False]
        except Exception as e:
            self.log.error('Unable to add Static Routes {}'.format(e))
            self.clickOnStaticRouteCancelButton()
            return ["FAILED", False]

    def addstaticRoutesInvalid(self, type, destinationIP,destinationSbntNum, destinationSbnt, gatewayIP):
        browser = self.browser
        try:
            time.sleep(3)
            self.clickOnAddStaticRoute()
            time.sleep(2)
            self.selectStaticRouteType(type)
            time.sleep(2)
            self.selectStaticRouteDestinationIP(destinationIP)
            time.sleep(2)
            self.selectStaticRouteSubnetNum(destinationSbntNum)
            time.sleep(2)
            self.selectStaticRouteSubnet(destinationSbnt)
            time.sleep(2)
            self.selectStaticRouteGatewayIP(gatewayIP)
            time.sleep(2)
            msg1 = self.msgStaticRouteDestinationIP()
            msg2 = self.msgStaticRouteGatewayIP()
            msg3 = self.msgStaticRouteSubnetMask()
            msg4 = self.msgStaticRouteSubnetMaskNum()
            if msg1 and msg2 and msg3 and msg4:
                self.clickOnStaticRouteCancelButton()
                # msg = "Please enter a valid IP address"
                return ["PASSED" , True]
            return ["FAILED", False]
        except Exception as e:
            self.log.error('Unable to check invalid Static Routes {}'.format(e))
            return ["FAILED", False]

    def editStaticRoutes(self,type,OlddestinationIP,NewdestinationIP,destinationSbnt,gatewayIP):
        browser = self.browser
        try:
            time.sleep(3)
            dstnIP = self.getDestinationIP()
            num = dstnIP[OlddestinationIP]
            # editRoute = browser.find_element_by_xpath("/html/body/div/uib-accordion/div/div[4]/div[2]/div/div/table/tbody/tr[%d]/td[6]/span[2]"%num)
            expandLink = browser.find_element_by_xpath("//div[@heading='Static Routes']")
            editRoute = expandLink.find_element_by_xpath(
                "div[2]/div/div/table/tbody/tr[%d]/td[6]/span[2]" % num)
            editRoute.click()
            time.sleep(2)
            self.selectStaticRouteType(type)
            time.sleep(2)
            self.selectStaticRouteDestinationIP(NewdestinationIP)
            time.sleep(2)
            self.selectStaticRouteSubnet(destinationSbnt)
            time.sleep(2)
            self.selectStaticRouteGatewayIP(gatewayIP)
            time.sleep(2)
            self.clickOnStaticRouteSaveButton()
            time.sleep(4)
            info = self.getStaticRouteInfo()
            dict1 = info[NewdestinationIP]
            if dict1.get("Subnet Mask")==destinationSbnt and dict1.get("Gateway IP")==gatewayIP and dict1.get("Type")==type and dict1.get("Status")=='Set' :
                return ["PASSED", True]
            return ["FAILED", False]
        except Exception as e:
            self.log.error('Unable to edit Static Routes {}'.format(e))
            self.clickOnStaticRouteCancelButton()
            return ["FAILED", False]

    def getDestinationIP(self):
        browser = self.browser
        try:
            dstnIP={}
            i = 1
            expandLink = browser.find_element_by_xpath("//div[@heading='Static Routes']")
            tabpanel = expandLink.find_element_by_xpath("div[@role='tabpanel']")
            div = tabpanel.find_element_by_xpath("div[@class='panel-body']")
            div1 = div.find_element_by_tag_name("div")
            table = div1.find_element_by_tag_name("table")
            tbody = table.find_element_by_tag_name("tbody")
            trs = tbody.find_elements_by_xpath("tr[@class='ng-scope']")
            for tr in trs:
                td = tr.find_elements_by_tag_name("td")
                dstn = td[0].text
                dstnIP[str(dstn)] = i
                i +=1
            return dstnIP
        except Exception as e:
            self.log.error('Unable to get Static Routes destination IP {}'.format(e))
            return False

    def getStaticRouteInfo(self):
        browser = self.browser
        try:
            info = {}

            # trs = browser.find_elements_by_xpath(
            #     "/html/body/div/uib-accordion/div/div[4]/div[2]/div/div/table/tbody/tr")
            expandLink = browser.find_element_by_xpath("//div[@heading='Static Routes']")
            tabpanel = expandLink.find_element_by_xpath("div[@role='tabpanel']")
            div = tabpanel.find_element_by_xpath("div[@class='panel-body']")
            div1 = div.find_element_by_tag_name("div")
            table = div1.find_element_by_tag_name("table")
            tbody = table.find_element_by_tag_name("tbody")
            # trs = tbody.find_elements_by_tag_name("tr")
            trs = tbody.find_elements_by_xpath("tr[@class='ng-scope']")

            for tr in trs:
                dict1 = {}
                td = tr.find_elements_by_tag_name("td")
                dstnIP = td[0].text
                sbnt = td[1].text
                gtwy = td[2].text
                type = td[3].text
                status = td[4].text
                dict1["Subnet Mask"] = str(sbnt)
                dict1["Gateway IP"] = str(gtwy)
                dict1["Type"] = str(type)
                dict1["Status"] = str(status)
                info[str(dstnIP)] = dict1
            return info
        except Exception as e:
            self.log.error('Unable to get Static Routes destination IP {}'.format(e))
            return False

    def deleteStaticRoutes(self,destinationIP):
        browser = self.browser
        try:
            time.sleep(3)
            dstnIP = self.getDestinationIP()
            num = dstnIP[destinationIP]
            expandLink = browser.find_element_by_xpath("//div[@heading='Static Routes']")
            deleteRoute = expandLink.find_element_by_xpath(
                "div[2]/div/div/table/tbody/tr[%d]/td[6]/span[3]" % num)
            # deleteRoute = browser.find_element_by_xpath(
            #     "/html/body/div/uib-accordion/div/div[4]/div[2]/div/div/table/tbody/tr[%d]/td[6]/span[3]" %num)
            deleteRoute.click()
            time.sleep(2)
            div = browser.find_element_by_xpath("//div[@class='modal-content']")
            modalDlg = div.find_element_by_xpath("//div[@class='modal-footer']")
            button = modalDlg.find_elements_by_tag_name('button')
            button[0].click()
            time.sleep(4)
            dstnIP1 = self.getDestinationIP()
            if dstnIP1.get(destinationIP)==None:
                return ["PASSED",True]
            return ["FAILED", False]
        except Exception as e:
            self.log.error('Unable to delete Static Routes {}'.format(e))
            return ["FAILED",False]

    def openDiagnosticsPage(self):
        browser = self.browser
        try:
            userMenuHead = browser.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right']")
            span = userMenuHead.find_element_by_xpath("//span[@trees='navCtrl.menu_right']")
            li = span.find_element_by_tag_name('li')
            userBtn = li.find_element_by_tag_name('a')
            userBtn.click()
            time.sleep(2)
            dropDownMenu = li.find_element_by_tag_name('ul')
            leafMenus = dropDownMenu.find_elements_by_tag_name('li')
            for leafMenu in leafMenus:
                diagnosticMenu = leafMenu.find_element_by_tag_name('a')
                if 'diag' in diagnosticMenu.get_attribute('href'):
                    diagnosticMenu.click()
                    break
            time.sleep(5)
            browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
            src = browser.page_source
            browser.switch_to.default_content()
            if re.search(r'cClear Diagnostics', src):
                return ["PASSED", True]
            else:
                return ["FAILED", False]
        except Exception as e:
            self.log.error('Unable to open diagnostic page %s' % e)
            return ["FAILED", False]

    def diagnosticConnectivityCheck(self,IPaddress):
        browser = self.browser
        try:
            time.sleep(3)
            self.openDiagnosticsPage()
            time.sleep(2)
            body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
            div = body.find_element_by_xpath("div[@class='ng-scope']")
            div1 = div.find_element_by_xpath("iframe[@class='ng-scope']")
            browser.switch_to.frame(div1)
            input = browser.find_element_by_xpath("//input[@id='check_ip']")
            input.clear()
            input.send_keys(IPaddress)
            time.sleep(1)
            button = browser.find_element_by_xpath("//button[@id='ping_button']")
            button.click()
            browser.switch_to.default_content()
            time.sleep(20)
            if self.statusPingInfo():
                return ["PASSED", True]
            return ["FAILED", False]
        except Exception as e:
            self.log.error('Unable to check connectivity {}'.format(e))
            return ["FAILED", False]

    def statusPingInfo(self):
        browser = self.browser
        try:
            body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
            div = body.find_element_by_xpath("div[@class='ng-scope']")
            div1 = div.find_element_by_xpath("iframe[@class='ng-scope']")
            browser.switch_to.frame(div1)
            field = browser.find_element_by_xpath("//fieldset[@id='legend']")
            input = field.find_element_by_xpath("div[@id='ping_result']")
            str = input.text
            browser.switch_to.default_content()
            match = re.search(r' 0% packet loss', str)
            if match:
                return True
            return False
        except Exception as e:
            self.log.error('Unable to get status ping Info {}'.format(e))
            return False
#############################################################################################################

# ## Test Code ##
# log = testLogger('spifeeWebGUITools','spifee.log',False,False,True)
# spifee = Spifee("10.51.10.132","spifee","spifeepw")
# gui = cpacketWebGui(spifee, log)
# #print gui.loginAfterSessionTimeout('spifee','spifeepw','update')
# print gui.loginAfterSPIFEEAvailable()
# gui.openBrowserAndLogin()
# time.sleep(5)
# gui.openDiagnosticsPage()
# time.sleep(3)
# print gui.diagnosticConnectivityCheck("10.51.10.109")
# time.sleep(2)
# print gui.statusPingInfo()
################################ backup and restore ##############################
# print gui.openBackupRestorePage()
# time.sleep(5)
#
# OUTPUT_DIR = "/home/cpacket/automationsrc/output"
# strBackupFile = ''
# print gui.getSPIFEEUploadedConfigurationBackupFile()
# print gui.performSPIFEEUploadConfigBackup("/home/cpacket/automationsrc/input", "cpacket_nwsnap_from_cpacket-132_on_20180118_212237.bin")
################################# manage user#####################################################
# gui.openManageUsers()
# time.sleep(2)
# list = gui.getcVuPortInfo("alan")
# list1 = ['1','5','4','127','56','70','99','3','6','8','9','10','20','34','92','91','100']
# print gui.editcVuUser('alan',"TACACS+","L3",list1)
# print gui.getcVuAllUserInfo()
# print gui.importcVuUsers("/home/cpacket/automationsrc/input/cpacket-132_spf_users_Jan_05_2018_00_57_32.csv" )
# print gui.getcVuUserInfo("alan")
# print gui.exportcVuUsers('automation1', '/home/cpacket/spifee_automation/output')
# print gui.searchManageUsers("alan")
# print gui.addcVuUser("newuser3","TACACS+","L2","deselectAll",)
# userList = ['newuser11','newuser12','newuser13','newuser14','newuser15','newuser16','newuser17','newuser18','newuser19','newuser20']
# gui.addcVuUserAllTypes(userList,"selectAll")
# gui.deleteAllcVuUser(userList)
# print gui.addcVuUserSuccessMessage("newuser3")
# list2 = ['2','3','45','60','126','127']
# gui.clickOncVuUserEditBtn("newuser")
# time.sleep(2)
# gui.clickOncVuUserPortsBtn("newuser")
# time.sleep(2)
# print gui.selectIndividualPorts(list2,"newuser")
# gui.clickOncVuProvisionBtn()
#
# list1 = ["c400_10","c2440_88"]
# list2 = ["cstor240"]

# time.sleep(2)
# print gui.editcVuUser("newuser3","TACACS+","L3","selectAll")
# print gui.addcVuUser("hari","TACACS+","L2","selectAll")
# time.sleep(2)
# print gui.clickOncVuUserSelectBtn("newuser")
# print gui.clickOncVuProvisionBtn()
# print gui.selectcVuProDepro(list1)
# print gui.cVuProvisionMltplDevices("newuser",list1,list2,True)
# time.sleep(5)
# print gui.cVuDeprovisionMltplDevices("newuser",list1,list2,True)
# print gui.getcVuUserConsoleDataProvision()
# time.sleep(2)
# print gui.getcVuUserConsoleDataMltplDevicesProvison("newuser5",list1 )
# print gui.cVuDeprovisionMltplDevices("newuser3",list1,list2,True)
# time.sleep(2)
# print gui.deletecVuUser("newuser3")
# time.sleep(2)
# print gui.searchManageUsers("alan")
# print gui.exportcVuUsers("newuser4","/home/cpacket/automationsrc/output" )
# file = gui.getLatestcVuUserFileName("/home/cpacket/automationsrc/output")
# print gui.getcVuUserInfo("newuser2")

# print gui.readcVuUserFile(file)
# print gui.getcVuPortInfo("alan")
# gui.selectMltplcStorProDepro(list1)
# gui.selectMltplcVuProDepro(list2)
# print gui.clickcVuProDepro("10.51.10.10")
# print gui.clickcStorsProDepro("10.51.10.240")
# print gui.clickLocalcClearProDepro()
# print gui.provisioncVuUsers("hari",'c400_10',None,False)

# print gui.readcVuUserFile("/home/cpacket/automationsrc/output/cpacket-X9SCL-X9SCM_spf_users_Oct_31_2017_23_07_52.csv")
# print gui.getcVuUserConsoleDataMltplDevices("hari",list1+list2)
# time.sleep(4)

# print gui.clickOnAcceptProDepro("cancel")
# gui.clickOncVuAddUserBtn()
# print gui.clickOncVuUserEditBtn("alan")
# print gui.selectcVuUserAuthentication("TACACS+")
# print gui.selectcVuUserRole("L2")
# print gui.clickOncVuUserPortsBtn("alan")
# print gui.clickOncVuUserPortSelectDeselectBtn("alan","deselectAll")

# gui.clickOncVuConsoleBtn()
# print gui.getcVuUserConsoleData("hari","c400_10")

#
#########################################################################
#gui.openCapturesPage()
#time.sleep(5)
#gui.clickCStorMergedStartDownload()
# gui.openAdminPage()
# time.sleep(2)
# gui.clickExpandStaticRoutes()
# time.sleep(5)
# print gui.addstaticRoutes("host","1.1.1.4","32",None,"2.2.2.4")
# print gui.addstaticRoutesInvalid("Net","1.1.","-2","0","2.2.")
# time.sleep(2)
# print gui.editStaticRoutes("host","1.1.1.3","1.1.1.4",None,"255.255.255.255","2.2.2.4")
# print gui.getDestinationIP()
# print gui.getStaticRouteInfo()
# print gui.deleteStaticRoutes("1.1.1.4")
#print gui.getAuthServerInfo()
#gui.enableDisableTACACS('Disable')
#gui.enableDisableRADIUS('Disable')
#gui.clickExpandAddModifyDeleteCClearUsers()
#gui.clickExpandTACACSRADIUS()
#gui.clickExpandManageStacking()
#gui.clickExpandConfigureIPDNS()
#gui.clickExpandStaticRoutes()
#gui.clickExpandConfigureTimeSync()
#gui.clickExpandCounterGeneration()
# gui.clickExpandServerSslCertificate()
# time.sleep(2)
# print gui.restoreDefaultServerSslCertificate()
# print gui.noFileUploadServerSslCertificate()
# print gui.noFileUploadServerSslCertificate()
# print gui.wrongFileUploadServerSslCertificate("/home/harit/Downloads/wrong.txt", "/home/harit/Downloads/wrong.txt")
######################################################
# # # gui.addServerSslCertificateFiles("/home/harit/Downloads/10.51.10.130.cer", "/home/harit/Downloads/10.51.10.130.key" )
# gui.clickExpandOtherSystemSettings()
# time.sleep(2)
# print gui.spifeeGrafanaUpdate("10.51.10.132","allsmartreadyforescapevelocity", "cpacket", "cpcktsprvsrd")
# # print openSupervisorStatus("10.51.10.132","cpacket", "cpcktsprvsrd")

# print gui.correctFileUploadServerSslCertificate("/home/harit/Downloads/10.51.10.130.cer", "/home/harit/Downloads/10.51.10.130.key")
###########################################################