from flask import Flask, render_template, request
from drawer import *
from animator import *
from ShotData import *

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():
    args = request.args
    if len(args) == 2:
        fig = plt.figure()
        fig.set_size_inches(9, 6)
        fig.subplots_adjust(left=-0.3, bottom=-0.3, right=1.3, top=1.3, wspace=None, hspace=None)
        ax = fig.add_subplot(projection = '3d', computed_zorder = False)
        ax_base(ax = ax)
        
        player_shotchart = shotchart(args['nbaplayer'], args['nbaseason'])
        walks = []
        for x,y in zip(player_shotchart['LOC_X'], player_shotchart['LOC_Y']):
            walks.append(getParabola(-y, -x))
        lines = [ax.plot([], [], [])[0] for _ in walks]
        total_shots = len(walks)
        reps = int(total_shots**(2/5) / 2) + 1
        shotsPerRep = int(total_shots/reps) + 1
        num_steps = 30 * reps
        
        ani = animation.FuncAnimation(
            fig, update_lines, num_steps, fargs=(walks, lines, shotsPerRep, player_shotchart['SHOT_MADE_FLAG']), interval=30, repeat = False)
        ani_saved = ani.to_jshtml()
        
        fig = plt.figure()
        fig.set_size_inches(9, 6)
        fig.subplots_adjust(left=0, bottom=0, right=1.3, top=1.3, wspace=None, hspace=None)
        ax = fig.add_subplot(projection = '3d', computed_zorder = False)
        with open("Output.txt", "w") as text_file:
            text_file.write(ani_saved)
        ax_base2(fig, ax, player_shotchart)
        return render_template("base2.html", playerName = args['nbaplayer'], playerSZN = args['nbaseason'], rendered_anim = ani_saved)
        

    else:
        return render_template("base.html", sec = "ten")

if __name__ == '__main__':
    app.run(debug=True)