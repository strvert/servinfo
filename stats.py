import subprocess
import re


class Loadstats:

    def res_cmd(self, cmd):
        return subprocess.Popen(
                cmd, stdout=subprocess.PIPE,
                shell=True).communicate()[0].decode()

    def loadCpu(self, filesave = False):
        stats = self.res_cmd('sar 1 1 -P ALL')
        p = r'秒\s*\d{1,2}\s*(\d{1,3}\.\d{2})\s*(\d{1,3}\.\d{2})\s*(\d{1,3}\.\d{2})\s*(\d{1,3}\.\d{2})\s*(\d{1,3}\.\d{2})'
        p2 = r'(\d\d)時(\d\d)分(\d\d)秒'
        time = re.findall(p2, stats)
        use = re.findall(p, stats)
        cpu_total = []

        for x in use:
            z = 0
            for y in x:
                z += int(float(y))
            cpu_total.append(z)

        if filesave:
            with open('cpu_use.log', 'a') as f:
                for x in cpu_total:
                    f.write(str(x) + ',')
                f.write('\n')
            with open('time.log', 'a') as f:
                f.write(time[0][0] + ':' + time[0][1] + '\n')

        return cpu_total

    def loadMem(self, filesave=False):
        stats = self.res_cmd('sar 1 1 -r')
        p = r'秒\s+\d+\s+\d+\s+\d+\s+(\d{1,3}\.\d{2})'
        mem = re.findall(p, stats)
        if filesave:
            with open('mem.log', 'a') as f:
                f.write(mem[0] + '\n')

    def loadTemp(self, filesave=False):
        stats = self.res_cmd('sensors')
        p = r'Core\s\d{1,2}:\s+\+(\d{1,3}\.\d{1})°C\s+\(high'
        temp = re.findall(p, stats)
        if filesave:
            with open('cpu_temp.log', 'a') as f:
                for x in temp:
                    f.write(x + ',')
                f.write('\n')
