#!/usr/bin/python
import stats
import plot

def main():
    num = 15
    st = stats.Loadstats()

    st.loadCpu(True)
    st.loadMem(True)
    st.loadTemp(True)

    time_lbl = []
    with open('time.log', 'r') as f:
        s = f.readlines()
        # print(len(s))
        for x in range(len(s) - 1, len(s) - num-1, -1):
            time_lbl.append(s[x])

    cpu_plt = []
    with open('cpu_use.log', 'r') as f:
        s = f.readlines()
        # print(len(s))
        for x in range(len(s) - 1, len(s) - num-1, -1):
            cpu_plt.append(s[x].split(',')[:-1])

    cpu = plot.Plot()
    cpu.plot(cpu_plt, 'm', time_lbl, num, 'cpu_usege.png',
            figname = 'CPU utilization', labelname = 'Processor:')

    mem_plt = []
    with open('mem.log', 'r') as f:
        s = f.readlines()
        for x in range(len(s) - 1, len(s) - num-1, -1):
            mem_plt.append(s[x])

    mem = plot.Plot()
    mem.plot(mem_plt, 's', time_lbl, num, 'mem_usege.png',
            figname = 'MEM utilization', labelname = 'Utilization:')

    temp_plt = []
    with open('cpu_temp.log', 'r') as f:
        s = f.readlines()
        for x in range(len(s) - 1, len(s) - num-1, -1):
            temp_plt.append(s[x].split(',')[:-1])
    temp = plot.Plot()
    temp.plot(temp_plt, 'm', time_lbl, num, 'temp.png',
            figname = 'CPU Temperature', labelname = 'Core:')


if __name__ == '__main__':
    main()
