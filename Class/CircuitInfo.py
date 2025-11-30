class CircuitInfo:
    def __init__ (self, Vendor_Id, A_End_Port, Z_End_Port, Vendor_name, Status, Corp_Site):
        if Vendor_Id is None:
            self.__Vendor_Id = ""
        else:
            Vendor_Id = Vendor_Id.strip()
            self.__Vendor_Id = Vendor_Id
            if "EPL" in Vendor_Id:
                self.__Vendor_Id = Vendor_Id.replace(" ", "")
            if "00/VLXX/549279/LVLC" in Vendor_Id:
                self.__Vendor_Id = "52/KGFN/111961/TWCS"
            if "22156292342" in Vendor_Id:
                self.__Vendor_Id = "091MUMB623035859389"

        if A_End_Port is None:
            self.__A_End_Port = ""
        else:
            self.__A_End_Port = A_End_Port.strip()

        if Z_End_Port is None:
            self.__Z_End_Port = ""
        else:
            self.__Z_End_Port = Z_End_Port.strip()
            
        if Vendor_name is None:
            self.__Vendor_name = ""
        else:
            self.__Vendor_name = Vendor_name.strip()

        if Status is None:
            self.__Status = ""
        else:
            self.__Status = Status.strip()

        if Corp_Site is None:
            self.__Corp_Site = ""
        else:
            self.__Corp_Site = Corp_Site.strip()

    def getVendorId(self):
        return self.__Vendor_Id

    def getAEndPort(self):
        return self.__A_End_Port

    def getZEndPort(self):
        return self.__Z_End_Port

    def getVendorName(self):
        return self.__Vendor_name

    def getStatus(self):
        return self.__Status

    def getCorpSite(self):
        return self.__Corp_Site

