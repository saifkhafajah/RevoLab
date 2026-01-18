# RevoLab Simulator v5.0 🦾

![Version](https://img.shields.io/badge/version-1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-stable-success)
![Powered By](https://img.shields.io/badge/AI-Gemini-purple)

> **An advanced, browser-based industrial robotics simulator featuring real-time kinematics, AI-powered scripting, and workspace analysis.**

## 📖 Description
**RevoLab** is a high-fidelity, open-source 3D robotic arm simulator designed for engineers, researchers, and students. Built with Three.js, it provides a seamless industrial-grade environment to design, test, and analyze robotic configurations using the **Denavit-Hartenberg (DH)** convention.

Unlike traditional simulators, RevoLab features an **AI Copilot powered by Google Gemini**, allowing users to program complex robot movements using natural language commands.

---

## 🚀 Key Features

* **Dynamic Kinematics Engine:** Gradient-descent based Inverse Kinematics (IK) and Forward Kinematics (FK) for any DOF configuration.
* **✨ Gemini AI Copilot:** Instantly translate English commands like *"Pick up the crate and move it to the center"* into executable RevoScript.
* **📊 MATLAB-Style Plotting:** Real-time floating trajectory window to monitor TCP (Tool Center Point) coordinates.
* **🛡️ Workspace Analysis:** Generate smooth, volumetric 3D Convex Hulls to visualize the robot's physical reach.
* **🖥️ Industrial Visualization:** High-performance 3D rendering with path tracing, ghost targets, and joint coordinate frames.
* **🛠️ Embedded Export:** Generate production-ready **C++** and **Python (NumPy)** driver code directly from your custom DH parameters.
* **🕹️ Interactive Control:** Precision jogging, joint overrides, and smooth interpolation for realistic mechanical motion.

## 🛠️ Built With
* **Three.js** (WebGL 3D Engine)
* **Google Gemini API** (LLM Integration)
* **JavaScript** (ES6+)
* **HTML5/CSS3** (Cyber-Industrial Theme)

---

## 🏁 Getting Started

You can run RevoLab instantly in your browser via GitHub Pages or host it locally.

### Installation
1.  **Clone the repo:**
    ```bash
    git clone https://github.com/saifkhafajah/RevoLab.git
    ```

2.  **Run the simulator:**
    * Simply open `index.html` in any modern browser.
    * *(Optional)* Run the Python launcher for a dedicated local server experience:
        ```bash
        python launcher.py
        ```

## 📜 License
Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 👤 Created By
**Saif Khafajah** *Engineer & Developer*
