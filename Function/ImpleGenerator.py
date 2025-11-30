from . import DateTimeGenerator

def getImplementationInfo(validCircuitsList):

    generalInfo = (
        '# DEVICES LIST:\n'
        '\n'
        'Device Name          Vendor                 Interface                    IP                              Role\n'
        '-------------------------------------------------------------------------------------------------------------\n'
    )
    backupInfo = ""
    checks = ""
    costOut = ""
    costOutVerification = ""
    costIn = ""
    traffic = '\n# Check Netranger for traffic on devices:\n'


    for item in validCircuitsList:

        aEnd = item.getAEndPort().split(":")
        aEndDeviceName = aEnd[0]
        aEndInterface = aEnd[1]
        zEndDeviceName = ""
        zEndInterface = ""
        if ":" in item.getZEndPort():
            zEnd = item.getZEndPort().split(":")
            zEndDeviceName = zEnd[0]
            zEndInterface = zEnd[1]

        costOutVerification = costOutVerification + (
            '\n'
            '# On $HUBDeviceName$:\n'
            '\n'
            '\tshow configuration | display set | match $PeerIP$\n'
            '\tshow bgp neighbor $PeerIP$ | no-more\n'
            '\tshow route receive-protocol bgp $PeerIP$ | no-more\n' 
            '\tshow route advertising-protocol bgp $PeerIP$ | no-more\n'
            '\tshow route protocol bgp next-hop $PeerIP$ | no-more\n'
        )

        checks = checks + (
            '\n'
            '# On $HUBDeviceName$:\n'
            '\n'
            '\tshow interfaces $HUBEndInterface$ extensive | no-more\n'
            '\tshow ospf interface $HUBEndInterface$ detail | no-more\n'
            '\tshow interfaces diagnostics optics $HUBEndInterface$ | no-more\n'
            '\tshow interfaces $HUBEndInterface$ statistics | match "rate|error"\n'
            '\tshow configuration | display set | match $PeerIP$\n'
            '\tshow bgp neighbor $PeerIP$ | no-more\n'
            '\tshow route receive-protocol bgp $PeerIP$ | no-more\n'
            '\tshow route advertising-protocol bgp $PeerIP$ | no-more\n'
            '\tshow route protocol bgp next-hop $PeerIP$ | no-more\n'
            '\tshow log messages | no-more\n'
            '\tping $PeerEndIP$ source $HUBEndIP$ count 1000 size 1472 do-not-fragment rapid bypass-routing\n'
        )

        # 如果不是最后一个有效组件时
        if item != validCircuitsList[-1]:

            # 基本信息
            generalInfo = (generalInfo
                + (aEndDeviceName + "                 $AEndVendor$                     " + aEndInterface + "     $AEndIP$           $SPOKE|HUB$\n")
                + (zEndDeviceName + "                $ZEndVendor$               " + zEndInterface + " $ZEndIP$             $SPOKE|HUB$\n")
                + (
                    '\n'
                    'Group: $HUBGROUP$\n'
                    'Policy: $HUBPOLICY$\n'
                    '\n'
                    'Device Name          Vendor                 Interface                    IP                              Role\n'
                    '-------------------------------------------------------------------------------------------------------------\n'
                )
            )

            # 备份信息
            backupInfo = backupInfo + aEndDeviceName +  " & " + zEndDeviceName + " & "

            traffic = (traffic
                + ("\n")
                + ("\t# For " + aEndDeviceName + " also change the variable in the URL below:\n")
                + ("\n")
                + ("\thttps://gns-netranger.corp.ebay.com//cgi-bin/netranger/nr-searchmenu.cgi?searchonly=no&custom=no&location=&name=" + aEndDeviceName + "&unit=bps&desc=%23%23GRAPH%26s%3D-86400%23%23&status=on&searchbutton=Search\n")
                + ("\n")
                + ("\t# For " + zEndDeviceName + " also change the variable in the URL below:\n")
                + ("\n")
                + ("\thttps://gns-netranger.corp.ebay.com//cgi-bin/netranger/nr-searchmenu.cgi?searchonly=no&custom=no&location=&name=" + zEndDeviceName + "&unit=bps&desc=%23%23GRAPH%26s%3D-86400%23%23&status=on&searchbutton=Search\n")
            )

            costOut = costOut + (
                '\n'
                '# On $HUBDeviceName$:\n'
                '\n'
                '\tping $CR Number$\n'
                '\tconfigure private\n'
                '\n'
                '\tset protocols bgp group $HUBGROUP$ neighbor $PeerIP$ import $HUBPolicy$\n'
                '\tset protocols bgp group $HUBGROUP$ neighbor $PeerIP$ export $HUBPolicy$\n'
                '\n'
                '\tshow | compare\n'
                '\tcommit and-quit\n'
            )

            costIn = costIn + (
                '\n'
                '# On $HUBDeviceName$:\n'
                '\n'
                '\tping $CR Number$\n'
                '\tconfigure private\n'
                '\n'
                '\tdelete protocols bgp group $HUBGROUP$ neighbor $PeerIP$ import $HUBPolicy$\n'
                '\tdelete protocols bgp group $HUBGROUP$ neighbor $PeerIP$ export $HUBPolicy$\n'
                '\n'
                '\tshow | compare\n'
                '\tcommit and-quit\n'
            )
        else:
            generalInfo = (generalInfo 
                + (aEndDeviceName + "                 $AEndVendor$                     " + aEndInterface + "     $AEndIP$           $SPOKE|HUB$\n")
                + (zEndDeviceName + "                $ZEndVendor$               " + zEndInterface + " $ZEndIP$             $SPOKE|HUB$\n")
                + (
                    "\n"
                    'Group: $HUBGROUP$\n'
                    'Policy: $HUBPOLICY$\n'
                )
            )

            backupInfo = backupInfo + aEndDeviceName +  " & " + zEndDeviceName + "\n"

            traffic = (traffic
                + ("\n")
                + ("\t# For " + aEndDeviceName + " also change the variable in the URL below:\n")
                + ("\n")
                + ("\thttps://gns-netranger.corp.ebay.com//cgi-bin/netranger/nr-searchmenu.cgi?searchonly=no&custom=no&location=&name=" + aEndDeviceName + "&unit=bps&desc=%23%23GRAPH%26s%3D-86400%23%23&status=on&searchbutton=Search\n")
                + ("\n")
                + ("\t# For " + zEndDeviceName + " also change the variable in the URL below:\n")
                + ("\n")
                + ("\thttps://gns-netranger.corp.ebay.com//cgi-bin/netranger/nr-searchmenu.cgi?searchonly=no&custom=no&location=&name=" + zEndDeviceName + "&unit=bps&desc=%23%23GRAPH%26s%3D-86400%23%23&status=on&searchbutton=Search")
            )

            costOut = costOut + (
                '\n'
                '# On $HUBDeviceName$:\n'
                '\n'
                '\tping $CR Number$\n'
                '\tconfigure private\n'
                '\n'
                '\tset protocols bgp group $HUBGROUP$ neighbor $PeerIP$ import $HUBPolicy$\n'
                '\tset protocols bgp group $HUBGROUP$ neighbor $PeerIP$ export $HUBPolicy$\n'
                '\n'
                '\tshow | compare\n'
                '\tcommit and-quit'
            )

            costIn = costIn + (
                '\n'
                '# On $HUBDeviceName$:\n'
                '\n'
                '\tping $CR Number$\n'
                '\tconfigure private\n'
                '\n'
                '\tdelete protocols bgp group $HUBGROUP$ neighbor $PeerIP$ import $HUBPolicy$\n'
                '\tdelete protocols bgp group $HUBGROUP$ neighbor $PeerIP$ export $HUBPolicy$\n'
                '\n'
                '\tshow | compare\n'
                '\tcommit and-quit'
            )

    return generalInfo, backupInfo, checks, traffic, costOut, costOutVerification, costIn

def getImplementation(plannedStartTime, vendorTimeInImplementation, cisInDeclaration, validCircuitsList):

    # 在Implementation Plan中的起始时间
    startTimeInImplementation = DateTimeGenerator.getStartTimeInImplementation(plannedStartTime)

    # 在Implementation Plan中的Vendor的维护时间
    declaration = (("Vendor Start Date           Vendor End Date        Window\n")
        + (vendorTimeInImplementation)
        + ("\n\n")
        + (cisInDeclaration)
        + ("\n\n")
        + ("Start this change 30 minutes in advance at " + startTimeInImplementation + "PT\n\n")
    )

    generalInfo, backupInfo, checks, traffic, costOut, costOutVerification, costIn = getImplementationInfo(validCircuitsList)
    
    partOne = (
        'SOP #1: https://wiki.vip.corp.ebay.com/pages/viewpage.action?pageId=667980709#CorpNetworkEngineeringSOP:CircuitMaintenanceoftheBGPenabledOFFICE(SPOKE)WANrouters.-SOP#1(HubtoSpoke-OnlyBGPisenabled)\n'
        '\n'
        '\n'
        '\n'
        '1. General info\n'
        '======================================================================\n'
        '\n'
    ) + generalInfo + (
        '\n'
        '\n'
        '\n'
    )

    partTwo = (
        '2. Backup the configuration of the devices.\n'
        '======================================================================\n'
        '\n'
        'Use netbrain backup devices '
    ) + backupInfo + (
        '\n'
        '\n'
        '\n'
    )

    partThree = (
        '3. Pre-checks: Existing configuration, traffic rate, errors/CRC counters\n'
        '======================================================================\n'
        '\n'
        '###################################################################\n'
        '###################################################################\n'
        '###### VERIFY THE REDUNDANT CIRCUIT IS ACTIVE BEFORE PROCEEDING ######\n'
        '###################################################################\n'
        '###################################################################\n'
    ) + checks + traffic + (
        '\n'
        '\n'
        '\n'
        '\n'
    )

    partFour = (
        '4. Cost-out procedure:\n'
        '======================================================================\n'
    ) + costOut + (
        '\n'
        '\n'
        '\n'
        '\n'
    )
    
    partFive = (
        '5. Cost-out verification:\n'
        '======================================================================\n'
    ) + costOutVerification + traffic + (
        '\n'
        '\n'
        '\n'
        '\n'
    )

    partSix = (
        '6. Vendor maintenance in progress\n'
        '======================================================================\n'
        '\n'
        '# After vendor maintenance has been completed, circuit should be ready to put back in service.\n'
        '\n'
        '\n'
        '\n'
    )

    partSeven = (
        '7. Cost-in procedure:\n'
        '======================================================================\n'
    ) + costIn + (
        '\n'
        '\n'
        '\n'
        '\n'
    )

    partEight = (
        '8. Post-checks: Post CR configuration, traffic rate, errors/CRC counters\n'
        '======================================================================\n'
    ) + checks + traffic

    # 生成Implementation Plan
    implementation = ((declaration + partOne + partTwo)
        + (partThree + partFour + partFive)
        + (partSix + partSeven + partEight)
    )

    return implementation
