############################# SSL Certificate ##########################################################################


    def addServerSslCertificateFiles(self, certificate, privateKey):
        browser = self.browser
        try:
            crtf = browser.find_element_by_xpath("//input[@id='ssl.cer']")
            pvkey = browser.find_element_by_xpath("//input[@id='ssl.key']")
            time.sleep(2)
            crtf.send_keys(certificate)
            pvkey.send_keys(privateKey)
            return True
        except Exception as e:
            self.log.error('Unable to uploadServerSSLCertificate files {}'.format(e))
            return False

    def noFileUploadServerSslCertificate(self):
        browser = self.browser
        try:
           time.sleep(3)
           upload = browser.find_element_by_xpath("//input[@id='ssl.upload']")
           upload.click()
           time.sleep(2)
           if self.errorServerSslCertificateNoFileUpload():
               time.sleep(3)
               return ["PASSED", True]
           return ["FAILED", False]
        except Exception as e:
           self.log.error('Unable to uploadServerSSLCertificate {}'.format(e))
           return ["FAILED" , False ]

    def correctFileUploadServerSslCertificate(self,certificate, privateKey):
        browser = self.browser
        self.addServerSslCertificateFiles(certificate, privateKey)
        try:
            time.sleep(3)
            upload = browser.find_element_by_xpath("//input[@id='ssl.upload']")
            upload.click()
            time.sleep(2)
            self.isSslConfirmationDialogUp()
            time.sleep(2)
            if self.successServerSslCertificateFileUpload():
                time.sleep(3)
                self.log.info('successfully uploaded ServerSSLCertificate')
                return ["PASSED", True]
            return ["FAILED", False]
        except Exception as e:
            self.log.error('Unable to uploadServerSSLCertificate {}'.format(e))
            return ["FAILED", False]

    def wrongFileUploadServerSslCertificate(self, certificate, privateKey):
        browser = self.browser
        self.addServerSslCertificateFiles(certificate, privateKey)
        try:
            time.sleep(3)
            upload = browser.find_element_by_xpath("//input[@id='ssl.upload']")
            upload.click()
            time.sleep(2)
            self.isSslConfirmationDialogUp()
            time.sleep(2)
            if self.errorServerSslCertificateFileUpload():
                time.sleep(3)
                self.log.error('wrong files are uploaded')
                return ["PASSED", True]
            return ["FAILED", False]
        except Exception as e:
            self.log.error('Unable to uploadServerSSLCertificate {}'.format(e))
            return ["FAILED", False]

    def restoreDefaultServerSslCertificate(self):
        browser = self.browser
        try:
            time.sleep(3)
            restore = browser.find_element_by_xpath("//input[@id='ssl.restore']")
            restore.click()
            time.sleep(2)
            self.isSslConfirmationDialogUp()
            time.sleep(2)
            if self.successServerSslCertificateRestore():
                time.sleep(3)
                return ["PASSED", True]
            return ["FAILED", False]
        except Exception as e:
            self.log.error('Unable to restore Server SSL Certificate {}'.format(e))
            return ["FAILED", False]

    def errorServerSslCertificateNoFileUpload(self):
        browser = self.browser
        try:
            wrongFile = browser.find_element_by_xpath("//div[@class='toast toast-error']")
            div = wrongFile.find_element_by_xpath("//div[@class='toast-message']")
            strText = div.text
            if 'Certificate file is required.' in strText:
                self.log.error('Certificate files are required')
                return True
            return False
        except Exception as e:
            self.log.error('Error {}'.format(e))
            return False

    def errorServerSslCertificateFileUpload(self):
        browser = self.browser
        try:
            wrongFile = browser.find_element_by_xpath("//div[@class='toast toast-error']")
            div = wrongFile.find_element_by_xpath("//div[@class='toast-message']")
            strText = div.text
            if 'Error uploading SSL Certificate.' in strText:
                self.log.error('wrong files are uploaded')
                return True
            return False
        except Exception as e:
            self.log.error('Error {}'.format(e))
            return False

    def successServerSslCertificateFileUpload(self):
        browser = self.browser
        try:
            wrongFile = browser.find_element_by_xpath("//div[@class='toast toast-success']")
            div = wrongFile.find_element_by_xpath("//div[@class='toast-message']")
            strText = div.text
            if 'Command completed successfully.' in strText:
                self.log.info('files are uploaded ')
                return True
            return False
        except Exception as e:
            self.log.error('Error {}'.format(e))
            return False

    def successServerSslCertificateRestore(self):
        browser = self.browser
        try:
            wrongFile = browser.find_element_by_xpath("//div[@class='toast toast-success']")
            div = wrongFile.find_element_by_xpath("//div[@class='toast-message']")
            strText = div.text
            if 'Command completed successfully.' in strText:
                self.log.info('Restore default SSl Certificate completed ')
                return True
            return False
        except Exception as e:
            self.log.error('Error {}'.format(e))
            return False

    def isSslConfirmationDialogUp(self, accept=True):
        browser = self.browser
        try:
            body = browser.find_element_by_xpath("//body[@ng-controller='MainController as mc']")
            modalDlg = body.find_element_by_class_name('modal-dialog')
            modalFooter = modalDlg.find_element_by_class_name('modal-footer')
            buttons = modalFooter.find_elements_by_tag_name('button')
            if accept is True:
                buttons[0].click()
            else:
                buttons[1].click()
        except Exception as e:
            self.log.error('Unable to accept on modal-dialog {}'.format(e))
            return False

