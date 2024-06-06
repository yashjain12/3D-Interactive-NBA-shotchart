#CANVAS UPON WHICH BASKETBALL COURT/HOOP/NET/BACKBOARD/ETC is drawn

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import scipy.signal as spSig
from matplotlib import cm
import mpl_toolkits.mplot3d.art3d as art3d

import matplotlib
matplotlib.use('agg')

def ax_base(ax):
    def floor():
        x = np.arange(-8.948 + 14 - 47, -8.948 + 14 + 47, 47)
        y = np.arange(-25, 25 + 50, 50)
        z = np.zeros((len(x), len(y)))
        x, y = np.meshgrid(x, y)
        return [x, y, z]

    def threePointLine():
        x_corner = np.arange(-8.948, -8.948 + 14, 1/1000)
        y_corner = 22 * np.ones(len(x_corner))
        z_corner = np.zeros(len(x_corner))

        thetas = np.arange(0.388653505 + np.pi/2, 3 * np.pi/2 - 0.388653505, 1/1000)
        x_main = 23.75 * np.cos(thetas)
        y_main = 23.75 * np.sin(thetas)
        z_main = np.zeros(len(thetas))

        x = np.concatenate((x_corner, x_main, x_corner))
        y = np.concatenate((y_corner, y_main, -y_corner))
        z = np.concatenate((z_corner, z_main, z_corner))
        return [x, y, z]

    def logo():
        theta_logo = np.arange(-np.pi/2, np.pi/2, 1/1000)
        x = -42 + 6 * np.cos(theta_logo)
        y = 6 * np.sin(theta_logo)
        z = np.zeros(len(theta_logo))
        return [x, y, z]

    def interiorLines():
        #x = np.arange(-9.948, 5.052 + 14, 14)
        x = np.arange(-13.75, -13.75 + 19 * 2, 19)
        y = np.arange(-8, 8 + 16, 16)
        z = np.zeros((len(x), len(y)))
        x, y = np.meshgrid(x,y)
        return [x, y, z]

    def floorCircle():
        theta = np.arange(-np.pi/2, 3 * np.pi/2, 1/1000)
        x = -13.75 + 6 * np.cos(theta)
        y = 6 * np.sin(theta)
        z = np.zeros(len(theta))
        return [x, y, z]

    def StanchionBottom():
        y_back = np.arange(-4.4587/2, 4.4587/2 + 4.4587, 4.4587)
        z_back = np.arange(0, 2 + 2, 2)
        x_back = (1.25 + 10.666 + 6.3125) * np.ones((len(y_back), len(z_back)))
        y_back, z_back = np.meshgrid(y_back, z_back)

        x_bottom = np.arange((1.25 + 10.666), (1.25 + 10.666 + 2 * 6.3125), 6.3125)
        y_bottom = np.arange(-4.4587/2, 4.4587/2 + 4.4587, 4.4587)
        z_bottom = np.zeros((len(x_bottom), len(y_bottom)))
        x_bottom, y_bottom = np.meshgrid(x_bottom, y_bottom)

        y_front = np.arange(-4.4587/2, 4.4587/2 + 4.4587, 4.4587)
        z_front = np.arange(0, 3.5 + 3.5, 3.5)
        x_front = (1.25 + 10.666) * np.ones((len(y_front), len(z_front)))
        y_front, z_front = np.meshgrid(y_front, z_front)

        x_poly = [1.25 + 10.666 + 6.3125,1.25 + 10.666 + 6.3125,1.25 + 10.666,1.25 + 10.666]
        z_poly = [0,2,3.5,0]
        poly = patches.Polygon(xy=list(zip(x_poly, z_poly)), fill = True, color = 'black')
        poly2 = patches.Polygon(xy=list(zip(x_poly, z_poly)), fill = True, color = 'black')
        return [[x_back, y_back, z_back], [x_front, y_front, z_front], [x_bottom, y_bottom, z_bottom], poly, poly2]

    def StanchionMiddle():
        x_poly = [1.25 + 10.666 + 2.5, 1.25 + 10.666 + 2.5, 1.25 + 10.666, 1.25 + 10.666]
        z_poly = [0, 8.5, 10, 0]

        poly = patches.Polygon(xy=list(zip(x_poly, z_poly)), fill = True, color = 'black')
        poly2 = patches.Polygon(xy=list(zip(x_poly, z_poly)), fill = True, color = 'black')

        y_poly2 = [-4.4587/2,-4.4587/2,4.4587/2,4.4587/2]
        z_poly2 = [0,10,10,0]
        poly3 = patches.Polygon(xy=list(zip(y_poly2, z_poly2)), fill = True, color = 'black')
        return [poly, poly2, poly3]

    def StanchionFront():
        x_r1 = np.arange(1.25, 1.25 + 10.666 * 2, 10.666)
        y_r1 = np.arange(-1,1 + 2,2)
        z_r1 = np.arange(9.5, 10 + 0.5, 0.5)

        x_bottomst, y_bottomst = np.meshgrid(x_r1, y_r1)
        z_bottomst = 10 * np.ones((len(x_bottomst), len(y_bottomst)))

        x_topst, y_topst = np.meshgrid(x_r1, y_r1)
        z_topst = 10 * np.ones((len(x_topst), len(y_topst)))

        x_leftst, z_leftst = np.meshgrid(x_r1, z_r1)
        x_rightst, z_rightst = np.meshgrid(x_r1, z_r1)
        y_leftst = np.ones((len(x_r1), len(z_r1)))
        y_rightst = -1 * np.ones((len(x_r1), len(z_r1)))

        y_frontst, z_frontst = np.meshgrid(y_r1, z_r1)
        y_backst, z_backst = np.meshgrid(y_r1, z_r1)
        x_frontst = 1.25 * np.ones((len(y_r1), len( z_r1)))
        x_backst = (1.25 + 10.666) * np.ones((len(y_r1), len( z_r1)))
        return [[x_bottomst, y_bottomst, z_bottomst],
                [x_topst, y_topst, z_topst],
                [x_leftst, y_leftst, z_leftst],
                [x_rightst, y_rightst, z_rightst],
                [x_frontst, y_frontst, z_frontst],
                [x_backst, y_backst, z_backst]]

    def Backboard():
        x_b1 = np.arange(1, 1.25 + 0.25, 0.25)
        y_b1 = np.arange(-3,3 + 6,6)
        z_b1 = np.arange(9, 13 + 4, 4)

        x_bottomb, y_bottomb = np.meshgrid(x_b1, y_b1)
        z_bottomb = 9 * np.ones((len(x_bottomb), len(y_bottomb)))

        x_topb, y_topb = np.meshgrid(x_b1, y_b1)
        z_topb = 13 * np.ones((len(x_topb), len(y_topb)))

        x_leftb, z_leftb = np.meshgrid(x_b1, z_b1)
        x_rightb, z_rightb = np.meshgrid(x_b1, z_b1)
        y_leftb = -3 * np.ones((len(x_b1), len(z_b1)))
        y_rightb = 3 * np.ones((len(x_b1), len(z_b1)))

        y_frontb, z_frontb = np.meshgrid(y_b1, z_b1)
        y_backb, z_backb = np.meshgrid(y_b1, z_b1)
        x_frontb = 1 * np.ones((len(y_b1), len( z_b1)))
        x_backb = (1.25) * np.ones((len(y_b1), len( z_b1)))
        return [[x_bottomb, y_bottomb, z_bottomb],
                [x_topb, y_topb, z_topb],
                [x_leftb, y_leftb, z_leftb],
                [x_rightb, y_rightb, z_rightb],
                [x_frontb, y_frontb, z_frontb],
                [x_backb, y_backb, z_backb]]

    def rimFront():
        x_br = np.arange(0.75, 1 + 0.25, 0.25)
        y_br = np.arange(-0.3,0.3 + 0.6,0.6)
        z_br = np.arange(10 - 0.166666, 10 + 0.166666, 0.166666)

        x_bottombr, y_bottombr = np.meshgrid(x_br, y_br)
        z_bottombr = (10 - 0.166666) * np.ones((len(x_bottombr), len(y_bottombr)))

        x_topbr, y_topbr = np.meshgrid(x_br, y_br)
        z_topbr = 10 * np.ones((len(x_topbr), len(y_topbr)))

        x_leftbr, z_leftbr = np.meshgrid(x_br, z_br)
        x_rightbr, z_rightbr = np.meshgrid(x_br, z_br)
        y_leftbr = -0.3 * np.ones((len(x_br), len(z_br)))
        y_rightbr = 0.3 * np.ones((len(x_br), len(z_br)))

        y_frontbr, z_frontbr = np.meshgrid(y_br, z_br)
        y_backbr, z_backbr = np.meshgrid(y_br, z_br)
        x_frontbr = 1 * np.ones((len(y_br), len( z_br)))
        x_backbr = (0.75) * np.ones((len(y_br), len( z_br)))

        return [[x_bottombr, y_bottombr, z_bottombr],
                [x_topbr, y_topbr, z_topbr],
                [x_leftbr, y_leftbr, z_leftbr],
                [x_rightbr, y_rightbr, z_rightbr],
                [x_frontbr, y_frontbr, z_frontbr],
                [x_backbr, y_backbr, z_backbr]]

    def Hoop():
        freq = 10
        times = np.arange(0, 2 * np.pi + 2 * np.pi/freq, 2 *np.pi/freq)
        z_list = np.arange(8.5, 10.1, 0.3)
        radii = -(99/32)/((11/16) * z_list - 11)
        xhoop, yhoop = np.array([]), np.array([])

        for radius in radii:
            xhoop = np.append(xhoop, radius * np.cos(times))
            yhoop = np.append(yhoop, radius * np.sin(times))

        zhoop = np.repeat(z_list, len(times))
        times2 = np.arange(0, 2 * np.pi, 2 *np.pi/freq)
        xhoop2, yhoop2 = np.array([]), np.array([])

        for radius in radii:
            xhoop2 = np.append(xhoop2, radius * np.cos(times2))
            yhoop2 = np.append(yhoop2, radius * np.sin(times2))

        zhoop2 = np.repeat(z_list, len(times2))

        x_star, y_star, z_star = np.array([]), np.array([]), np.array([])

        for i in range(10):
            x_star = np.append(x_star, xhoop2[i:][0::freq])
            y_star = np.append(y_star, yhoop2[i:][0::freq])
            z_star = np.append(z_star, zhoop2[i:][0::freq])
        return [[xhoop2, yhoop2, zhoop2], [x_star, y_star, z_star]]
    """
    def HoopLines():
        y_bb3 = np.arange(-2.75, 2.75 + 2.75 * 2, 2.75 * 2)
        z_bb3 = np.arange(9.25, 12.75 + 3.5, 3.5)
        y_bb3, z_bb3 = np.meshgrid(y_bb3, z_bb3)
        x_bb3 = np.ones((len(y_bb3), len(z_bb3)))

        y_bb2 = np.arange(-1, 1 + 2, 2)
        z_bb2 = np.arange(9.8333, 11.3333 + 1.5, 1.5)
        y_bb2, z_bb2 = np.meshgrid(y_bb2, z_bb2)
        x_bb2 = np.ones((len(y_bb2), len(z_bb2)))

        y_bb1 = np.arange(-0.8333, 0.8333 + 1.6666, 1.6666)
        z_bb1 = np.arange(10, 11.1666 + 1.1664, 1.1666)
        y_bb1, z_bb1 = np.meshgrid(y_bb1, z_bb1)
        x_bb1 = np.ones((len(y_bb1), len(z_bb1)))

        return [[x_bb1, y_bb1, z_bb1], [x_bb2, y_bb2, z_bb2], [x_bb3, y_bb3, z_bb3]]
    """
    ax.grid(False)
    ax.axis('off')

    x_dim = [-50, 10]
    y_dim = [-26, 26]
    z_dim = [0, 13]

    ax.set_xlim(-50, 10)
    ax.set_ylim(-30, 30)
    ax.set_zlim(0, 13)

    ax.set_box_aspect((np.ptp(x_dim), np.ptp(y_dim), np.ptp(z_dim)))

    ax.plot(*threePointLine(), color = 'purple')
    ax.plot(*logo(), color = 'purple')

    circX, circY, circZ = floorCircle()
    lenInnerCirc = int(len(circX)/2)

    ax.plot(circX[-lenInnerCirc:], circY[-lenInnerCirc:], circZ[-lenInnerCirc:], color = 'gold', zorder = 4)

    rangeLen = 13
    for i in range(rangeLen):
        if i%2 == 0:
            ax.plot(circX[int(i * lenInnerCirc/rangeLen): int((i+1)/rangeLen * lenInnerCirc)], circY[int(i * lenInnerCirc/rangeLen): int((i+1)/rangeLen * lenInnerCirc)], circZ[int(i * lenInnerCirc/rangeLen): int((i+1)/rangeLen * lenInnerCirc)], color = 'gold', zorder = 4)
    #ax.plot(circX[0:lenInnerCirc], circY[0:lenInnerCirc], circZ[0:lenInnerCirc], color = 'gold', zorder = 4, linestyle = '--', dashes = (18.8495559/8.5, 18.8495559/8.5))
    ax.plot_surface(*floor(), zorder = -1, color = 'bisque', edgecolors = 'purple')
    ax.plot_surface(*interiorLines(), zorder = -1, color = 'purple', edgecolors = 'darkgoldenrod', linewidth = 1)

    stanchBack, stanchFront, stanchBottom, poly1, poly2 = StanchionBottom()

    ax.plot_surface(*stanchBack, zorder = 11, color = 'black')
    ax.plot_surface(*stanchFront, zorder = 11, color = 'black')
    ax.plot_surface(*stanchBottom, zorder = 11, color = 'black')

    ax.add_patch(poly1)
    ax.add_patch(poly2)
    art3d.pathpatch_2d_to_3d(poly1, z = 2.22916667, zdir = "y")
    art3d.pathpatch_2d_to_3d(poly2, z = -2.22916667, zdir = "y")

    poly3, poly4, poly5 = StanchionMiddle()
    ax.add_patch(poly3)
    ax.add_patch(poly4)
    ax.add_patch(poly5)
    art3d.pathpatch_2d_to_3d(poly3, z = 2.22916667, zdir = "y")
    art3d.pathpatch_2d_to_3d(poly4, z = -2.22916667, zdir = "y")
    art3d.pathpatch_2d_to_3d(poly5, z = 1.25 + 10.666, zdir = "x")

    s1, s2, s3, s4, s5, s6 = StanchionFront()
    ax.plot_surface(*s1, zorder = 11, color = 'black')
    ax.plot_surface(*s2, zorder = 11, color = 'black')
    ax.plot_surface(*s3, zorder = 11, color = 'black')
    ax.plot_surface(*s4, zorder = 11, color = 'black')
    ax.plot_surface(*s5, zorder = 11, color = 'black')
    ax.plot_surface(*s6, zorder = 11, color = 'black')

    b1, b2, b3, b4, b5, b6 = Backboard()
    ax.plot_surface(*b1, zorder = 11, color = 'black')
    ax.plot_surface(*b2, zorder = 11, color = 'black')
    ax.plot_surface(*b3, zorder = 11, color = 'black')
    ax.plot_surface(*b4, zorder = 11, color = 'black')
    ax.plot_surface(*b5, zorder = 11, color = 'black')
    ax.plot_surface(*b6, zorder = 11, color = 'black')

    r1, r2, r3, r4, r5, r6 = rimFront()
    ax.plot_surface(*r1, zorder = 11, color = 'black')
    ax.plot_surface(*r2, zorder = 11, color = 'black')
    ax.plot_surface(*r3, zorder = 11, color = 'black')
    ax.plot_surface(*r4, zorder = 11, color = 'black')
    ax.plot_surface(*r5, zorder = 11, color = 'black')
    ax.plot_surface(*r6, zorder = 11, color = 'black')

    y_bb3 = np.arange(-2.75, 2.75 + 2.75 * 2, 2.75 * 2)
    z_bb3 = np.arange(9.25, 12.75 + 3.5, 3.5)
    y_bb3, z_bb3 = np.meshgrid(y_bb3, z_bb3)
    x_bb3 = np.ones((len(y_bb3), len(z_bb3)))

    y_bb2 = np.arange(-1, 1 + 2, 2)
    z_bb2 = np.arange(9.8333, 11.3333 + 1.5, 1.5)
    y_bb2, z_bb2 = np.meshgrid(y_bb2, z_bb2)
    x_bb2 = np.ones((len(y_bb2), len(z_bb2)))

    y_bb1 = np.arange(-0.8333, 0.8333 + 1.6666, 1.6666)
    z_bb1 = np.arange(10, 11.1666 + 1.1664, 1.1666)
    y_bb1, z_bb1 = np.meshgrid(y_bb1, z_bb1)
    x_bb1 = np.ones((len(y_bb1), len(z_bb1)))


    ax.plot_surface(x_bb1, y_bb1, z_bb1, zorder = 15, color = 'white')
    ax.plot_surface(x_bb2, y_bb2, z_bb2, zorder = 14, color = 'black')
    ax.plot_surface(x_bb3, y_bb3, z_bb3, zorder = 13, color = 'white')

    thetaHoops = np.linspace(0, 2*np.pi, 24)
    hoopCircleY = 3/4 * np.sin(thetaHoops)
    hoopCircleX = 3/4 * np.cos(thetaHoops)

    ax.plot(hoopCircleX, hoopCircleY, 10 * np.ones(len(thetaHoops)), color = 'darkorange', zorder = 20, lw = 1)


    h1, h2 = Hoop()
    for i in range(10):
        ax.plot(h2[0][6*i:6*i + 6], h2[1][6*i:6*i + 6], h2[2][6*i:6*i+6], color = 'lightgray', zorder = 17)

    for i in range(6):
        ax.plot(h1[0][11*i:11*i + 11], h1[1][11*i:11*i + 11], h1[2][11*i:11*i + 11], color = 'lightgray', zorder = 17)
    
    ax.view_init(40, -112, 0)

def ax_base2(fig, ax, shotchart): #Responsible for creating the 3D Intensity Chart
    ax_base(ax)
    x_linspace = np.linspace(-35, -shotchart['LOC_Y'].min(), 20)
    y_linspace = np.linspace(shotchart['LOC_X'].min(), shotchart['LOC_X'].max(), 20)
    xx, yy = np.meshgrid(x_linspace, y_linspace, indexing = 'xy')
    z_kde = np.zeros(np.shape(xx))
    percentage = np.zeros(np.shape(xx))
    #spline = sp.interpolate.Rbf(x,y,z, function = 'thin_plate')

    xmin, ymin = x_linspace[0], y_linspace[0]
    xinterval = x_linspace[1] - x_linspace[0]
    yinterval = y_linspace[1] - y_linspace[0]
    for i, j, k in zip(-shotchart['LOC_Y'], shotchart['LOC_X'], shotchart['SHOT_MADE_FLAG']):
        if abs(i) < 26 and abs(j) < 35:
            xindex = int((i - xmin)/xinterval)
            yindex = int((j - ymin)/yinterval)
            z_kde[yindex, xindex] += 1
            percentage[yindex, xindex] += k

    percentage = np.divide(percentage,z_kde)#, out = np.zeros_like(percentage), where=z_kde!=0)
    percentage_mean = np.nanmean(percentage)
    percentage = np.nan_to_num(percentage, nan = percentage_mean)
    averagedVals = spSig.correlate2d(z_kde**(1/2), np.ones((2,2))/4, mode = 'same')
    averagedVals = (averagedVals - averagedVals.min()) * (13/averagedVals.max())

    ax.plot_surface(xx, yy, averagedVals, antialiased=True, facecolors = cm.get_cmap('cool')(3 * (spSig.correlate2d(percentage, np.ones((2,2))/4, mode = 'same') - 0.5) + 0.5), alpha = 0.8, linewidth = 2)# cmap = cm.get_cmap('cool')) #cmap = cm.coolwarm
    m = cm.ScalarMappable(cmap = cm.cool)
    cbar = fig.colorbar(m, ax = ax, shrink = 0.8, aspect = 5)
    cbar.set_label("Field Goal Percentage", rotation = 270, labelpad = 15)
    ax.view_init(40, -112, 0)
    plt.savefig('static/shotchart_intensity.png', bbox_inches = 'tight', pad_inches = 0.05)
