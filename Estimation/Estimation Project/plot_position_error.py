import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('./scenario_11_position_data.csv', header=0)
melted = data.melt('time', var_name='Variable', value_name='Value')

time = data['time']
err_x = data[' Quad.Ref.X'] - data[' Quad.Pos.X']
err_y = data[' Quad.Ref.Y'] - data[' Quad.Pos.Y']
err_z = data[' Quad.Ref.Z'] - data[' Quad.Pos.Z']
err_tot = (err_x**2 + err_y**2 + err_z**2)**0.5

# ax = sns.lineplot(
#     data=melted,
#     x='time',
#     y='Value',
#     hue='Variable'
# )
# plt.show()

fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(2,1,1)
plt.plot(
    time,
    err_x
)
plt.plot(
    time,
    err_y
)
plt.plot(
    time,
    err_z
)
ax1.set_title('Position Error over Time')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Positional Error (m)')
ax1.legend(['$x$', '$y$', '$z$'])

ax2 = fig.add_subplot(2,1,2)
plt.plot(
    time,
    err_tot,
    c='r',
    linewidth=2,
)
# ax2.hlines(y=1.0, xmin=min(time), xmax = max(time), linestyle='--', color='r')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Absolute Positional Error (m)')
ax2.legend(['Total Error'])

plt.show()

fig.savefig('position_error.png')