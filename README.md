# udacity_flying_car_and_autonomous_flight_engineer

This repository contains my implementations and exercises from the Udacity Flying Car and Autonomous Flight Engineer Nanodegree. The work spans the full autonomous flight stack: vehicle dynamics, controls, estimation, planning, and mission execution in simulation.

The projects in this repository demonstrate how a quadrotor is modeled, controlled, estimated, and navigated from raw sensor inputs to autonomous behavior. The focus is on practical implementation of the algorithms used in autonomous aerospace systems.

## Technical Skills Demonstrated

This repository highlights the following technical capabilities:

- controls design and tuning
- PID and cascaded control loop tuning
- quadrotor physics and vehicle dynamics modeling
- translational and rotational motion modeling
- state estimation and sensor fusion
- extended Kalman filtering (EKF) and UKF techniques
- GPS-denied navigation
- route planning and trajectory generation
- waypoint-based mission execution
- autonomous flight behavior and state-machine logic

## Repository Structure

The repository is organized around the core topics of the nanodegree:

### Introduction to Autonomous Flight

- `Introduction to Autonomous Flight/Backyard Flyer` — introductory autonomous flight behavior, including takeoff, waypoint navigation, and landing logic

### Backyard Flyer

- `Backyard Flyer/backyard_flyer.py` — a basic drone state machine that arms, takes off, flies a box-shaped route, lands, and returns control

### Controls

- `Controls/Vehicle Dynamics` — modeling of the quadrotor and its physical behavior
- `Controls/Introduction to Vehicle Control` — fundamentals of feedback control and flight control design
- `Controls/Control Architecture` — control architecture and signal flow for autonomous vehicle behavior
- `Controls/Full 3D Control` — full 3D attitude and position control for multirotor flight
- `Controls/project_building_a_controller` — practical controller design and tuning exercises

### Estimation

- `Estimation/Introduction to Estimation` — basic estimation concepts and state tracking
- `Estimation/Introduction to Sensors` — sensor modeling and measurement interpretation
- `Estimation/Extended Kalman Filters` — implementation of EKF-based state estimation
- `Estimation/GPS Denied Navigation` — navigation approaches when global positioning is unavailable
- `Estimation/The 3D EKF and UKF` — higher-dimensional estimation for 3D flight dynamics
- `Estimation/Estimation Project` — end-to-end estimation task integrating sensor data and state updates

### Planning

- `Planning/Motion Planning` — route planning, trajectory design, and path-following logic for autonomous navigation

## Project Focus

Across these modules, the repository demonstrates an end-to-end autonomous flight workflow:

1. model the vehicle's dynamics and physics
2. tune and implement flight controllers
3. estimate position, velocity, and attitude from sensor data
4. plan safe, feasible paths and trajectories
5. execute autonomous mission logic in a simulator

This work reflects the core engineering challenges in autonomous UAV systems: balancing dynamics, estimation uncertainty, control performance, and route feasibility.

## Course Credit

This project was completed as part of the Udacity Flying Car and Autonomous Flight Engineer Nanodegree.

Udacity provided the project prompt, simulator environment, and course materials. The implementations in this repository represent my original work developed during the program.
