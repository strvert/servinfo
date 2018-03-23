import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from matplotlib import cm
import numpy as np
import seaborn as sns


class Plot:

    def plot(self, y_plt, dim, x_lbl, num, savename, figname = 'figure', labelname = 'line:'):
        sns.set()
        pyplot.figure(figsize=(12, 4))
        cnt = 0

        if dim == 'm':
            plt_array = zip(*y_plt)
            for x in plt_array:
                cnt += 1
                self.plt = []
                for y in x:
                    self.plt.append(float(y))

                # print(plt)
                pyplot.plot(range(num), self.plt, label=labelname+str(cnt), lw=1, color=np.array(cm.jet(cnt / num))*0.75)
        elif dim == 's':
            self.plt = []
            for x in y_plt:
                self.plt.append(float(x))
            pyplot.plot(range(num), self.plt, label=labelname+str(cnt), lw=1, color=np.array(cm.jet(cnt / num))*0.75)

        pyplot.title(figname)
        x_lblf = []
        for x in range(0, num, 2):
            x_lblf.append(x_lbl[x])
        pyplot.xticks(range(0, num, 2), x_lblf)
        # pyplot.xlabel('Time')
        # pyplot.ylabel('%')
        pyplot.xlim([0, num-1])
        pyplot.ylim([0, 100])
        pyplot.legend(bbox_to_anchor=(0.69,0.98), loc=2, borderaxespad=0, ncol=2)
        pyplot.savefig(savename, bbox_inches='tight')
