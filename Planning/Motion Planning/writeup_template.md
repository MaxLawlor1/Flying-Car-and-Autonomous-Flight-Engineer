## Project: 3D Motion Planning
![Quad Image](./misc/enroute.png)

---


# Required Steps for a Passing Submission:
1. Load the 2.5D map in the colliders.csv file describing the environment.
2. Discretize the environment into a grid or graph representation.
3. Define the start and goal locations.
4. Perform a search using A* or other search algorithm.
5. Use a collinearity test or ray tracing method (like Bresenham) to remove unnecessary waypoints.
6. Return waypoints in local ECEF coordinates (format for `self.all_waypoints` is [N, E, altitude, heading], where the drone’s start location corresponds to [0, 0, 0, 0].
7. Write it up.
8. Congratulations!  You're Done!

## [Rubric](https://review.udacity.com/#!/rubrics/1534/view) Points
### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---
### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  

You're reading it! Below I describe how I addressed each rubric point and where in my code each point is handled.

### Explain the Starter Code

#### 1. Explain the functionality of what's provided in `motion_planning.py` and `planning_utils.py`
These scripts contain a basic planning implementation that includes state transitions and callbacks, as well as local waypoints.

`motion_planning.py` contains two additional functions:

* `send_waypoints()`
    * This simply sends the list `self.waypoints` to the simulator.

* `plan_path()`
    * In short, this writes the path for the drone to follow. It does this by:
        1. Reading starting lat and long from `colliders.csv`
        2. Reading in the obstacle map from `colliders.csv`
        3. Defining a grid at target altitude and safety margin
        4. Using an A* search to find an initial path
        5. Pruning the path to remove redundant collinear points
        6. Creating waypoints and sending these to the drone/simulator

And here's a lovely image of my results (ok this image has nothing to do with it, but it's a nice example of how to include images in your writeup!)
![Top Down View](./misc/high_up.png)

Here's | A | Snappy | Table
--- | --- | --- | ---
1 | `highlight` | **bold** | 7.41
2 | a | b | c
3 | *italic* | text | 403
4 | 2 | 3 | abcd

### Implementing Your Path Planning Algorithm

#### 1. Set your global home position
Here students should read the first line of the csv file, extract lat0 and lon0 as floating point values and use the self.set_home_position() method to set global home. Explain briefly how you accomplished this in your code.

Code:
```
with open('colliders.csv', 'r') as f:
            reader = csv.reader(f)
            lat0, lon0, *_ = next(reader)
            lat0 = float(lat0.split()[-1])
            lon0 = float(lon0.split()[-1])
```

And here is a lovely picture of our downtown San Francisco environment from above!
![Map of SF](./misc/map.png)

#### 2. Set your current local position
Here as long as you successfully determine your local position relative to global home you'll be all set. Explain briefly how you accomplished this in your code.

I used the `global_to_local` function from `udacidrone.frame_utils`:

```
current_local_position = global_to_local(current_global_pos, global_home)
```

Meanwhile, here's a picture of me flying through the trees!
![Forest Flying](./misc/in_the_trees.png)

#### 3. Set grid start position from local position
This is another step in adding flexibility to the start location. As long as it works you're good to go!

Code: 
```
grid_start = (
            int(self.current_local_position[0] - north_offset),
            int(self.current_local_position[1] - east_offset)
        )
grid_start = (
            max(0, min(grid.shape[0] - 1, grid_start[0])),
            max(0, min(grid.shape[1] - 1, grid_start[1]))
        )
```

#### 4. Set grid goal position from geodetic coords
This step is to add flexibility to the desired goal location. Should be able to choose any (lat, lon) within the map and have it rendered to a goal location on the grid.

```
grid_goal = (
            int(self.target_position[0]+10 - north_offset),
            int(self.target_position[1]+10 - east_offset)
        )
grid_goal = (
            max(0, min(grid.shape[0] - 1, grid_goal[0])),
            max(0, min(grid.shape[1] - 1, grid_goal[1]))
        )
```

#### 5. Modify A* to include diagonal motion (or replace A* altogether)
Minimal requirement here is to modify the code in planning_utils() to update the A* implementation to include diagonal motions on the grid that have a cost of sqrt(2), but more creative solutions are welcome. Explain the code you used to accomplish this step.

I added additional actions to `planning_utils.Action`, with cost `sqrt(2)
```
    NORTHWEST = (-1, -1, np.sqrt(2))
    NORTHEAST = (-1, 1, np.sqrt(2))
    SOUTHWEST = (1, -1, np.sqrt(2))
    SOUTHEAST = (1, 1, np.sqrt(2))
```

#### 6. Cull waypoints 
For this step you can use a collinearity test or ray tracing method like Bresenham. The idea is simply to prune your path of unnecessary waypoints. Explain the code you used to accomplish this step.

I defined a function `are_collinear` which returns True if the 3 input points are collinear beyond a certain threshold epsilon.
```
def are_collinear(p1, p2, p3, epsilon=1e-6):
            x_1 = [p2[0] - p1[0], p2[1] - p1[1]]
            x_2 = [p3[0] - p2[0], p3[1] - p2[1]]
            return np.dot(x_1, x_2) < epsilon
```

### Execute the flight
#### 1. Does it work?
It works!

### Double check that you've met specifications for each of the [rubric](https://review.udacity.com/#!/rubrics/1534/view) points.
  
# Extra Challenges: Real World Planning

For an extra challenge, consider implementing some of the techniques described in the "Real World Planning" lesson. You could try implementing a vehicle model to take dynamic constraints into account, or implement a replanning method to invoke if you get off course or encounter unexpected obstacles.


