


    def clickExpandOtherSystemSettings(self):
        browser = self.browser
        try:
            expandLink = browser.find_element_by_xpath("//div[@heading='Other System Settings']")
            aBtn = expandLink.find_element_by_tag_name("a")
            aBtn.click()
            return ["PASSED",True]
        except Exception as e:
            self.log.error('Unable to expand Server SSL Certificate {}'.format(e))
            return ["FAILED",False]

    def spifeeGrafanaUpdate(self, spifeeIP, passwd, username, password):
        browser = self.browser
        try:
            [pid_bf, tm_bf] = self.openSupervisorStatus(spifeeIP, username, password)
            time.sleep(2)
            expandLink = browser.find_element_by_xpath("//div[@heading='Other System Settings']")
            div = expandLink.find_elements_by_tag_name("div")
            div1 = div[1].find_element_by_tag_name("div")
            div2 = div1.find_element_by_tag_name("fieldset")
            upload = div2.find_element_by_tag_name("button")
            time.sleep(2)
            upload.click()
            self.isGrafanaConfirmationDialogUp()
            time.sleep(2)
            if self.testGrafanaSSH(spifeeIP, passwd):
                time.sleep(2)
                status = self.checkSupervisorStatus(pid_bf, tm_bf,spifeeIP, username, password)
                time.sleep(4)
                if status:
                   return ["PASSED", True]

            return ["PASSED", True]
        except Exception as e:
            self.log.error('Unable to upload {}'.format(e))
            return ["FAILED", False]

    def checkSupervisorStatus(self, pid_bf, tm_bf,spifeeIP, username, password):

        try:
            time.sleep(2)
            [pid_af,tm_af] = self.openSupervisorStatus(spifeeIP, username, password)
            time.sleep(4)
            if pid_bf != pid_af:
                if tm_bf != tm_af:
                    return True

            return False
        except Exception as e:
            self.log.error('Unable to check supervisor {}'.format(e))
            return False

    def isGrafanaConfirmationDialogUp(self, accept=True):
        browser = self.browser
        try:
            modalFooter = browser.find_element_by_class_name('modal-footer')
            buttons = modalFooter.find_elements_by_tag_name('button')
            time.sleep(2)
            if accept is True:
                buttons[0].click()
            else:
                buttons[1].click()
        except Exception as e:
            self.log.error('Unable to accept on modal-dialog {}'.format(e))
            return False

    def openSSHClientConnection(self, spifeeIP, passwd):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=spifeeIP, port=22, password=passwd)
        except paramiko.AuthenticationException as e:
            self.log.info("Authentication failed when connecting to {} ".format(e))
            sys.exit(1)
        except Exception as e:
            self.log.error("could not SSH to {} as exception {}".format(spifeeIP, e))
            sys.exit(1)
        return ssh

    def testGrafanaSSH(self, spifeeIP, passwd):
        ssh = self.openSSHClientConnection(spifeeIP, passwd)
        try:
            ftp = ssh.open_sftp()
            fh = ftp.file('/media/DATA_1/DATA001/module/graph-engine/service/etc/grafana/grafana.ini', "r", -1)
            time.sleep(2)
            data = fh.read()
            time.sleep(2)
            out = data.split("\n")
            l = "domain =" + spifeeIP
            for line in out:
                if re.search(line, l):
                    return True
            return False
        except Exception as e:
            self.log.error("unable to get SSH data {}".format(e))
            return False

    def openSupervisorStatus(self, spifeeIP, username, password):
        browser1 = webdriver.Firefox()

        try:
            browser1.get("http://%s:%s@%s:9002/" % (username, password, spifeeIP ))
            time.sleep(4)
            form = browser1.find_element_by_tag_name("form")
            table = form.find_element_by_tag_name("table")
            tbody = table.find_element_by_tag_name("tbody")
            tr = tbody.find_elements_by_tag_name("tr")
            td = tr[16].find_elements_by_tag_name("td")
            span = td[1].find_element_by_tag_name("span")
            str = span.text
            time.sleep(2)
            str1 = str.split(" ")
            pid = str1[1]
            tm = str1[3]
            browser1.close()
            return [pid, tm]
        except Exception as e:
            self.log.error("unable to open supervisor status {}".format(e))
            browser1.close()
            return False