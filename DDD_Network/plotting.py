"""
Script for plotting networks in the syle of the cover
of the 2nd Edition of Andy Kirk’s Data Visualisation:
A Handbook for Data Driven Design.

M Garrod, March 2021
"""
import bezier
import numpy as np
from pylab import cm
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib


def DDD_plot(G) :

    pos = nx.circular_layout(G)
    edges = [p for p in G.edges()]

    # plt.style.use('dark_background')

    cmap = cm.get_cmap('Dark2', 20)
    codes = [ matplotlib.colors.rgb2hex(cmap(i)) for i in range(cmap.N) ]

    # hand picked colour hexes online using: https://imagecolorpicker.com/en
    codes=["#e6a97f","#cbb4aa","#6d90b2","#bd585c","#7c5450","#82b4c1","#e1ad83"]

    #plt.rcParams['axes.facecolor'] = 'blue'
    fig, ax = plt.subplots(figsize=(8, 8),facecolor='#313745')

    peturbed_pos = {}
    for index, values in pos.items():
        peturbed_pos[index] = np.array(
            [values[0] + np.random.uniform(-0.1, 0.1), values[1] + np.random.uniform(-0.1, 0.1)])

    pos = peturbed_pos
    for edge in edges:
        pos_1 = pos[edge[0]]
        pos_1_x, pos_1_y = pos_1

        pos_2 = pos[edge[1]]
        pos_2_x, pos_2_y = pos_2

        #pos_1_x = pos_1_x + np.random.uniform(-0.1, 0.1)
        #pos_1_y = pos_1_y + np.random.uniform(-0.1, 0.1)

        # randomly add in nodes which spawn close to their neighbours
        coin_toss = np.random.uniform(0, 1)
        if coin_toss > 1.0:
            pos_2_x = pos_1_x + np.random.uniform(-0.1, 0.1)
            pos_2_y = pos_1_y + np.random.uniform(-0.1, 0.1)

            nodes_x = [pos_1_x, pos_1_x + np.random.uniform(-0.1, 0.1), pos_2_x]
            nodes_y = [pos_1_y, pos_1_y + np.random.uniform(-0.1, 0.1), pos_2_y]

        else:
            #pos_2_x = pos_2_x + np.random.uniform(-0.1, 0.1)
            #pos_2_y = pos_2_y + np.random.uniform(-0.1, 0.1)
            nodes_x = [pos_1_x, 0.0, pos_2_x]
            nodes_y = [pos_1_y, 0.0, pos_2_y]


        nodes1 = np.asfortranarray([
            nodes_x,
            nodes_y,
        ])
        curve1 = bezier.Curve(nodes1, degree=2)
        x_vals = [curve1.evaluate(p)[0][0] for p in np.linspace(0, 1, 100)]
        y_vals = [curve1.evaluate(p)[1][0] for p in np.linspace(0, 1, 100)]

        plt.plot(x_vals, y_vals, np.random.choice(codes), lw=1.8, alpha=0.9)
        plt.plot([pos_1_x], [pos_1_y], 'wo', markersize=6, alpha=1.0)
        plt.plot([pos_2_x], [pos_2_y], 'wo', markersize=6, alpha=1.0)

    plt.axis('off')