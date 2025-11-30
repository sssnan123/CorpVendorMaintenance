from . import ShortDescGenerator
from . import DateTimeGenerator
from . import CISGenerator
from . import ImpleGenerator

# 获取Service-Now的Payloads信息
def getPayloads(startTime, endTime, isWinter, assignee, validCircuitsList):

    # 获取Change开始及结束时间
    plannedStartTime, plannedEndTime = DateTimeGenerator.getPlannedTime(startTime, endTime, isWinter)

    # 获取Payload中的UTC时间
    startDate = DateTimeGenerator.getStartTimeInPayloads(startTime)

    # 获取整个change的持续时间
    changeDuration = DateTimeGenerator.getChangeDuration(plannedStartTime, plannedEndTime)

    # 获取Short Description
    shortDescription = ShortDescGenerator.getShortDescription(plannedStartTime, plannedEndTime, validCircuitsList)

    # 获取所有链路信息
    cis = CISGenerator.getCIS(validCircuitsList)

    # 获取Implementation Plan中的链路信息
    cisInImplementation = CISGenerator.getCISInDeclaration(cis)

    # 获取Implementation Plan中Vendor的时间
    vendorTimeInImplementation = DateTimeGenerator.getVendorTimeInImplementation(startTime, endTime, isWinter)

    # 获取checks和traffic
    generalInfo, backupInfo, checks, traffic, costOut, costOutVerification, costIn = ImpleGenerator.getImplementationInfo(validCircuitsList)

    # 获取Implementation Plan
    implementation = ImpleGenerator.getImplementation(plannedStartTime, vendorTimeInImplementation, cisInImplementation, validCircuitsList)

    # 生成Payloads
    payloads = {
        'source': 'Neteng',
        'table': 'x_ebay_change_mgmt_import_change_api_data',
        'payload': {
            'short_description': shortDescription,
            'category': 'Corp NetOps',
            'change_duration': changeDuration,
            'type': 'Maintenance',
            'type_of_change': 'normal',
            'subtype': 'Circuit',
            'start_date': startDate,
            'assigned_to': assignee,
            'requested_by' : assignee,
            'cis': cis,
            'x_ebay_change_mgmt_not_able_to_find_ci': 'true',
            'implementation_plan': implementation,
            'business_justification': (
                'Vendor Maintenance - Vendor is performing maintenance on a core circuit.\n'
                '\n'
                'Core circuits provide connectivity between data centers/Offices in the Corp Network.\n'
                '\n'
                'While there are protections in place to minimize the impact of a circuit going down, there could be packet loss or multiple outages during the maintenance window.\n'
                '\n'
                'Moving traffic away from the circuit manually before the vendor maintenance begins allows us to remove traffic from the link with no impact, and to return traffic to the link after the maintenance is complete and verified to have been completed successfully.\n'
                '\n'
                'Available network capacity has been verified for the core circuits that will be unavailable during the maintenance window.\n'
                '\n'
                'External Email\n'
                '\n'
                '$External Email$'
            ),
            'rollback_plan': (
                '======================================================================\n'
                'Rollback plan: Cost-in procedure\n'
                '======================================================================\n'
                '\n'
                '\n'
            ) + costIn,
            'verification_plan': (
                '======================================================================\n'
                'Verification plan: Post CR configuration, traffic rate, errors/CRC counters\n'
                '======================================================================\n'
                '\n'
                '\n'
            ) + checks + traffic,
            'environment': 'Production',
            'assigned_group': 'Corp NetOps',
            'human_trigger': 'True',
            'status': 'New',
            'risk' : 'Low'
        }
    }

    return payloads
