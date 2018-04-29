# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

# this plots horizontal lines for each y value of m

for m in np.linspace(1,50,100):
    plt.plot([0,50],[m,m])

plt.savefig('51-1.jpg',dpi=300)
plt.show()
print('plot done')

c={}
with open('color.table') as f:
    for line in f:
        fields=line.split('\t')
        colorname=fields[0].lower()
        hexcode=fields[1]
        c[colorname]=hexcode

names=c.keys()
names=sorted(names)

print(names)

blues=[c['alice blue'],c['light blue'],c['baby blue'],c['light sky blue'],c['maya blue'],
       c['cornflower blue'],c['bleu de france'],c['azure'],c['blue sapphire'],c['cobalt'],
       c['blue'],c['egyptian blue'],c['duke blue']]
ax=plt.gca()
ax.set_color_cycle(blues)

# this plots horizonial lines for each y value of m.

for i,m in enumerate(np.linspace(1,50,100)):
    plt.plot([0,50],[m,m])

plt.savefig('51-2.jpg',dpi=300)
plt.show()
print('plot done')