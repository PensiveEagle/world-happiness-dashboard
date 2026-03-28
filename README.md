<a id="readme-top"></a>


<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/PensiveEagle">
    <img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/main/readme_assets/general_assets/pensiveeagle-logo-green.svg" alt="Pensive Eagle Logo" width="200" height="auto">
  </a>

<h3 align="center">World Happiness Dashboard</h3>

  <p align="center">
    A simple dashboard to display world happiness data, where the user can select the axes of the chart.
    <br />
  <!--  <a href="https://github.com/pensiveeagle/world-happiness-dashboard"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
  <!--  <a href="https://github.com/pensiveeagle/world-happiness-dashboard">View Demo</a>
    &middot;
    <a href="https://github.com/pensiveeagle/world-happiness-dashboard/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/pensiveeagle/world-happiness-dashboard/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A simple learning project of a Streamlit web interface that presents a dashboard showing World Happiness data from a .csv

<img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/main/readme_assets/world-happiness-dashboard/world-happiness-dashboard-screenshot.png" alt="project_capture" width="100%" height="auto">

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Docker][docker-shield]][docker-url]
[![Python][python-shield]][python-url]
[![Streamlit][streamlit-shield]][streamlit-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Docker

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/pensiveeagle/world-happiness-dashboard.git
   ```
2. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin pensiveeagle/world-happiness-dashboard
   git remote -v # confirm the changes
   ```
3. Build the docker image
   ```sh
   docker build -t world-happiness-dash .
   ```
4. Run the docker image
   ```sh
   docker run --rm -d -p 8080:8080 --name happiness-dash-1 world-happiness-dash

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The dashboard should be available at http://localhost:8080

To use it:
1. Choose your x and y axes
2. The chart should automatically update to reflect your choices

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<div align="center"><img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/869e68466915785fdc1c44c324f2d84de119e5f1/readme_assets/general_assets/makers_mark_circle.svg" width="50"></div>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/pensiveeagle/world-happiness-dashboard.svg?style=for-the-badge
[contributors-url]: https://github.com/pensiveeagle/world-happiness-dashboard/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/pensiveeagle/world-happiness-dashboard.svg?style=for-the-badge
[forks-url]: https://github.com/pensiveeagle/world-happiness-dashboard/network/members
[stars-shield]: https://img.shields.io/github/stars/pensiveeagle/world-happiness-dashboard.svg?style=for-the-badge
[stars-url]: https://github.com/pensiveeagle/world-happiness-dashboard/stargazers
[issues-shield]: https://img.shields.io/github/issues/pensiveeagle/world-happiness-dashboard.svg?style=for-the-badge
[issues-url]: https://github.com/pensiveeagle/world-happiness-dashboard/issues
[license-shield]: https://img.shields.io/github/license/pensiveeagle/world-happiness-dashboard.svg?style=for-the-badge
[license-url]: https://github.com/pensiveeagle/world-happiness-dashboard/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jameshall-profile
[docker-shield]: https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/
[streamlit-shield]: https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[streamlit-url]: https://streamlit.io/
[python-shield]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.org/