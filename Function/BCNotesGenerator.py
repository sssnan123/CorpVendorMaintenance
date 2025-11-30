import paramiko
import getpass

def getBCNotes(pet, validCircuitsList):

    BCNotes = (
        'BC Notes: Ok\n'

        'Routine (y/n): Y\n'
        'Time spend BC: 15m\n'
        'SOP present (y/n): Y\n'
        'SOP adherence (strict/template/partial/multiple): strict\n'
        'Risk assessment valid (y/n): Y\n'
        'Business Justification relevant (y/n): Y\n'
        'Script Verification (/SHARE/chg): na\n'
        'Alternate direct circuits: No maintenance on it.\n'
        '\n'

        'Impact Analysis\n'
        'No impact expected during this maintenance window.\n'
        '\n'
        '\n'
    )

    for item in validCircuitsList:

        # 如果Vendor Id为空直接跳过
        if item.getVendorId() == "":
            return BCNotes

        # 实例化SSHClient
        client = paramiko.SSHClient()

        # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接SSH服务端，以用户名和密码进行认证
        client.connect(hostname="lvs1-automation.bb.ebay.com", port=22, username = getpass.getuser(), password = pet)

        # 生成命令
        command = "/usr/local/mtbb/bin/view_alternate_circuit_throughput.py -c " + item.getVendorId()

        # 输出追加VendorID
        BCNotes = BCNotes + item.getVendorId() + "\n"

        # 打开一个Channel并执行命令
        stdin, stdout, stderr = client.exec_command(command)  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值

        # 打印执行结果
        BCNotes = BCNotes + stdout.read().decode("utf-8") + "\n"

        # 关闭SSHClient
        client.close()

    return BCNotes

