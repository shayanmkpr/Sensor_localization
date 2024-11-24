# Distributed Optimization for Sensor Placement

This repository implements a **distributed optimization framework** for optimal sensor placement in a 2D space. The project explores various algorithms, including **strongly connected networks**, **periodically connected networks**, and the **gossip algorithm**. The goal is to minimize a cost function under specific constraints while ensuring effective collaboration between sensors.

---

## Problem Description

### Objective
Optimize the positions of **N sensors** to accurately cover **5 points** in a 2D space by minimizing a cost function while satisfying the following constraints:
1. **Coverage Constraint**: Each point must be covered by at least 3 sensors.
2. **Threshold Constraint**: The distance between each sensor and the covered point must not exceed a threshold.
3. **Binary Sensor Activity**: Each sensor can either be active (`1`) or inactive (`0`).

---

## Mathematical Formulation

### Distance Calculation
The Euclidean distance between sensor k and point i is given as:  
Distance_ik = sqrt((x_i - x_k)^2 + (y_i - y_k)^2)

### Cost Function
The cost function J is defined as:  
J = sum (from i=1 to 5) sum (from k=1 to N) exp(-sqrt((x_i - x_k)^2 + (y_i - y_k)^2))  
The goal is to minimize J.

### Constraints
1. **Coverage Constraint**:  
   Each point i must be covered by at least 3 sensors:  
   sum (from k=1 to N) BinaryVar_ik >= 3  
   where BinaryVar_ik = 1 if sensor k covers point i, otherwise 0.

2. **Threshold Distance Constraint**:  
   Ensure the distance between sensor k and point i is within the threshold:  
   Distance_ik <= Threshold, for all i, k

3. **Binary Sensor Activity**:  
   Each sensor is either active or inactive:  
   SensorVar_k is in {0, 1}

---

## Algorithm Overview

### Steps for Distributed Optimization

1. **Initialization**:  
   - Randomly initialize each sensor's position in a 2D space.  
   - Create a **strongly connected network graph** to represent communication between agents.

2. **Distributed Consensus**:  
   For any pair of connected agents i and j:  
   - If connected:  
     AssumedPosition(t+1)_ij = ActualPosition(t)_i  
   - Otherwise:  
     AssumedPosition(t+1)_ij = AssumedPosition(t)_i  

3. **Cost Function Optimization**:  
   Each agent minimizes its local cost function:  
   J_i = -sum (from k=1 to N) exp(-sqrt((x_i - x_k)^2 + (y_i - y_k)^2))  
   Using **gradient descent**, the positions are updated as:  
   ActualPosition(t+1)_i = ActualPosition(t)_i - gamma * gradient(J_i)  
   where gamma is the step size.

4. **Constraint Satisfaction**:  
   If constraints are violated, adjust the positions to the nearest feasible values:  
   ActualPosition(t+1)_i = NearestFeasiblePosition(ActualPosition(t+1)_i)

5. **Convergence Check**:  
   Repeat steps 2–4 until the system converges.

---

## Periodically Connected Network Graph

### Features
1. **Grid Graph Generation**:  
   - Create a 2D grid graph to represent sensor connectivity.
2. **Periodic Connections**:  
   - Wrap edges to form a toroidal structure using `periodic=True`.
3. **Adjustable Parameters**:  
   - Modify grid size and connection probabilities to balance local and periodic links.

---

## Gossip Algorithm

### Overview
The gossip algorithm facilitates decentralized information exchange to collaboratively optimize sensor positions.

### Steps
1. **Initialization**: Sensors start with random positions.
2. **Network Graph Creation**: Use a periodically connected graph for sensor communication.
3. **Information Exchange**:  
   - At each iteration, sensors exchange information (positions, gradients) with random neighbors.
4. **Objective Function Update**:  
   - Update local objectives using exchanged data.
5. **Convergence Check**:  
   - Monitor changes in the global objective function to determine convergence.

---
