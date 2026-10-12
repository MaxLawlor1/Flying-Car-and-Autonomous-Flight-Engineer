import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./FCND-Estimation-CPP/config/log/Graph2.txt', header=0)

data_rounded = data.copy()
data_rounded['time'] = data_rounded['time'].apply(lambda x: round(x, 3))
data = data.loc[data_rounded['time'].eq(0.).idxmin():]


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


fig1 = plt.figure(figsize=(10,8))
ax = fig1.add_subplot(1,1,1)
plt.plot(
    time, 
    data[' Quad.Ref.X'],
    c='lightcoral',
    linestyle='--'
)
plt.plot(
    time, 
    data[' Quad.Ref.Y'],
    c='chartreuse',
    linestyle='--'
)
plt.plot(
    time, 
    data[' Quad.Ref.Z'],
    c='skyblue',
    linestyle='--'
)
plt.plot(
    time, 
    data[' Quad.Pos.X'],
    c='r',
    linewidth=2,
)
plt.plot(
    time, 
    data[' Quad.Pos.Y'],
    c='g',
    linewidth=2,
)
plt.plot(
    time, 
    data[' Quad.Pos.Z'],
    c='b',
    linewidth=2,
)
ax.set_title('Position Tracking Over Time')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Position in Global Frame')
ax.legend(['$x_{ref}$', '$y_{ref}$', '$z_{ref}$', '$x$', '$y$', '$z$'])

plt.show()
fig1.savefig('position_tracking.png')