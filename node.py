import paramiko
import select

class node(object):
    def __init__(self,nodeDetails ) :# ip,user='root',password='root@123'):
        self.ip = nodeDetails['ip']
        self.user = nodeDetails['user']
        self.password = nodeDetails['password']
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
        self.login()
    def login(self):
        self.ssh.connect(self.ip,username=self.user,password=self.password)
    def checkLogfile(self,logFile):
        channel = self.ssh.get_transport().open_session()
        channel.exec_command("tailf -0 %s" % logFile)
        while True:
            if channel.exit_status_ready():
                break
            rl, wl, xl = select.select([channel], [], [], 0.0)
            if len(rl) > 0:
                yield channel.recv(1024)

    def shellCmd(self,cmd,verbose = True):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        stdin.write("%s\n" % self.password)
        stdin.flush()
        #print type(stdin),type(stderr),type(stdout)
        stdout = stdout.readlines()
        stderr = stderr.readlines()

        if verbose :
            print stdout
            print stderr

        return stdout,stderr

    def cliCmd(self,cmd):
        cmd = '/opt/tms/bin/cli -m config -t "%s"' % cmd
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        stdin.write("%s\n" % self.password)
        stdin.flush()
        #print type(stdin),type(stderr),type(stdout)
        stdout = stdout.readlines()
        stderr = stderr.readlines()

        return stdout,stderr

    def updatePsqlQuery(self,query,db):
        result = []
        query = 'psql -U postgres -d %s -c "%s" ' % (db, query)
        output = self.shellCmd(query)[1] # needs error handle
        #print output

    def psqlQuery(self,query,db):
        result = []
        query = 'psql -U postgres -d %s -c "\copy ( %s ) to \'/tmp/1\' delimiter \'|\'"' % (db,query)
        #print query
        output = self.shellCmd(query)[0] # needs error handle
        output = self.shellCmd('cat /tmp/1')[0]
        print output
        for line in output:
            line = line.split('|')
            line = map(lambda x : x.rstrip('\n'),line)
            for w in xrange(len(line)) :
                if line[w] == '\\N':
                    line[w] = None
            line = map(lambda w : str(w).replace('\\N','None'),line)
            result.append(tuple(line))

        return result

#node = node('52.77.205.226',user='ad1214',password='admin@123')

#node.login()
#node.shellCmd('sudo ps -ef')