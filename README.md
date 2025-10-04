# webot-simulation

# 🤖 Webots Obstacle Detecting Robot

This project simulates an **autonomous obstacle detecting robot** using the **Webots robot simulator**.  
The robot moves forward and automatically avoids obstacles using distance sensors.

---

## 🚀 Project Overview

The robot is equipped with:
- **Two DC motors** (left and right wheels)
- **Distance sensors** (for obstacle detection)
- **Basic control logic** written in Python

When an obstacle is detected in front of the robot, it stops and turns until the path is clear, then continues moving forward.

---

## 🧰 Technologies Used

- **Webots** (Robot simulation software)
- **Python** (controller programming)
- **Robot Nodes:** `DifferentialWheels` or `Motor` + `DistanceSensor`

---

## 🧠 How It Works

1. The robot continuously reads values from the front distance sensors.
2. If an obstacle is detected (sensor value above threshold):
   - The robot stops.
   - Turns right or left.
3. If the path is clear:
   - The robot moves forward again.
---

## 🎥 Demo Video

You can view the demonstration video here:  
[Watch Demo on Google Drive](https://drive.google.com/file/d/1LZKTGbIgM7ZLZP07Pz6UBKgCg1w989Hn/view?usp=sharing)

---


