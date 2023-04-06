<a name="Say it Aint Genes (Gene Nomenclature)"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/TreyGower7/coe332-trey">
  <img src=https://user-images.githubusercontent.com/70235944/227821572-ac1783f5-d1cc-42f2-a38c-007b76707e18.jpg alt="Logo" width="80" height="80">

<h3 align="center">Say it Aint Genes (Gene Nomenclature)</h3>

  <p align="center">
    Project Objective

The goal of this gene data mini project is to use python requests to store gene data from https://www.genenames.org/download/archive/ into a redis database.



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a>
    <li><a href="#Paths & Routes">Paths & Routes</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#Kubernetes Deployment">Kubernetes Deployment</a></li>
    <li><a href="#What the data says">What the data says</a></li>
    <li><a href="#Contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Gene Project
The Gene Project was mainly about learning to use redis with big sets of data integrated with Flask. The big data used is from The Human Genome Organization (HUGO) and the commitee within HUGO, being HGNC, “approves a unique and meaningful name for every gene.” This data is imported with python requests then Flask apps excute http requests to get the data and returns the data.
    
### The Files In This Repo
    
`gene_api.py`
the python script contains and executes the `Flask`, `redis`, and python `requests` libraries functions. The script retrieves the data from the web at https://www.genenames.org/download/archive/, then can be displayed with different paths that send http requests.
    
`docker-compose.yml`
saves the user (you) from having to type in tricky commands to run the docker image. Instead it wraps the information for the docker image into one file and runs it with a simple command.
    
`Dockerfile`
is used to capture the docker image, the file specifies the Python version, and installs any libraries used in the python script to run the application. For the `gene_api.py` script the Dockerfile installs: `redis`, `requests`, `Flask`, and `yaml`.

`Kubernetes Files:`
    
  `tagower-test-flask-service.yml` - Used to run the flask cluster (Runs all pods associated with the ip)
    
  `tagower-test-flask-deployment.yml` - Provides declartive updates for flask pods
    
  `tagower-test-redis-service.yml` - Used to run the redis cluster (Runs all pods associated with the ip)
    
  `tagower-test-redis-deployment.yml` - Provides declartive updates for redis pods
    
  `tagower-test-pvc.yml` - Persitant Volume Claim to store our data in the redis database

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
  <img src=https://user-images.githubusercontent.com/70235944/227825420-7601d2a1-d92f-4a0c-9726-92f4e65e7699.png alt="Logo" width="80" height="80">
  <img src=https://user-images.githubusercontent.com/70235944/227826270-c253f2a4-c294-4146-bb7d-17f9cf0e4f24.png alt="Logo" width="80" height="80">
  <img src=https://user-images.githubusercontent.com/70235944/227825491-6821ba07-4561-4f6b-8b72-62d53eab346b.png alt="Logo" width="80" height="80">

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Running this script is extremely easy using the docker files provided to you in this repository. Breaking it into two parts, we can either pull an already created image or build our own image.

### Prerequisites
***Docker must be installed on your machine in order to run the files provided in this repo***
1. Since most use Ubuntu here is a link to get docker up and running on your machine using Ubuntu: https://docs.docker.com/engine/install/ubuntu/

2. Clone the repo
   ```sh
   git clone https://github.com/TreyGower7/coe332-trey/tree/main/homework06
   ```
3. Make a data directory to store your data with redis
    ```sh
    mkdir data
    ```
    
## Pulling a docker image
1. docker pull request
   ```sh
   docker pull tagower/gene_api:hw07   
   ```
    Output: <img width="627" alt="Screenshot 2023-03-27 at 8 14 47 PM" src="https://user-images.githubusercontent.com/70235944/228101377-198115c8-3448-4efc-8094-e9f5476b130b.png">

2. Run Redis and Flask on ports 6379 and 5000 respectively
   ```sh
   docker-compose up -d
   ```
    Ouput: <img width="627" alt="Screenshot 2023-03-27 at 8 16 20 PM" src="https://user-images.githubusercontent.com/70235944/228101604-7d796aae-8c44-420f-9362-88d95fbae69d.png">

3. Run <a href="#Paths & Routes">Paths & Routes</a></li> or stop containers
  ```sh
  docker-compose down
  ```
    
## Building a docker image
1. Build the image using included docker file
```sh  
docker build -t <username>/gene_api:<yourtag> .
```
2. Check image was created
```sh  
docker images
```
3. Run your new image
```sh  
docker-compose up
```
4. Run <a href="#Paths & Routes">Paths & Routes</a></li> or stop containers
  ```sh
  docker-compose down
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Paths & Routes -->
## Paths & Routes

- /data (POST's (loads), GET's (returns), or DELETE's the data from HGNC from the redis database)
- /genes (Returns a json formated list named hgnc_ids of all gene identifiers in the data set)
- /genes/<hgnc_id> (Gets the gene data from a specific gene given an identifier key)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
 

<!-- USAGE EXAMPLES -->
## Usage
1. Post the data to the redis database
    ```sh
    curl -X POST localhost:5000/data
    ```
      Output: Gene Data Posted
2. Get the data from redis in json format
    ```sh
    curl localhost:5000/data
    ```
      Output: ***Outputs same as curl localhost:5000/genes/hgnc_id except returns all ids***
3. Delete the data from the redis database
    ```sh
    curl -X DELETE localhost:5000/data
    ```
      Output: Gene Data Deleted
4. Get all hgnc_ids 
    ```sh
    curl localhost:5000/genes
    ```
      Output: <img width="500" alt="Screenshot 2023-03-27 at 9 23 48 PM" src="https://user-images.githubusercontent.com/70235944/228111676-a901004f-2ee2-4f89-a981-d294d412620f.png">
5. Get all data pertaining to a specific hgnc id
    ```sh
    curl localhost:5000/genes/hgnc_id
    ```
      Output: <img width="500" alt="Screenshot 2023-03-27 at 9 24 13 PM" src="https://user-images.githubusercontent.com/70235944/228111861-7970c198-8c78-4428-bf78-5dfb36abbcc7.png">

<p align="right">(<a href="#readme-top">back to top</a>)</p>
  
  <!-- Kubernetes -->
## Kubernetes Deployment
***IMPORTANT: You must be in a kubernetes cluster for these steps***

***In the github repository you can find 5 .yml files beginning with tagower-test to run the docker image***

### Using The Provided Image
1. docker pull request
  ```sh
   docker pull tagower/gene_api:hw07  
   ```
2. Refer below to 'Running Deployments' Section
  
### Building Your Own Image and Adapting The yml
***if building your own image it must be a docker image, which you can create following the steps in the 'Building a docker image' section***

1. Adapt the flask deployment file by changing this to the name of your image <your_username>/<image>:<image_tag>
<img width="401" alt="Screenshot 2023-04-06 at 12 17 00 AM" src="https://user-images.githubusercontent.com/70235944/230278377-85d42405-58f2-422a-a1f1-d76b70fa83d3.png">

2. Everything else remains the same. Now refer to 'Running The Deployments' section below
  
  
### Running The Deployments
***For both Using and Building sections we need to make sure the files are up and running*** 

1. Find your python debugger in kubernetes and ensure its running
<img width="529" alt="Screenshot 2023-04-05 at 8 40 33 PM" src="https://user-images.githubusercontent.com/70235944/230251539-ea530e8a-510e-4c7e-a8e0-56e6a0b034aa.png">

2. To run the other containers taken from this github repo
  ```sh
  kubectl apply -f tagower-test-flask-service.yml
  kubectl apply -f tagower-test-flask-deployment.yml
  kubectl apply -f tagower-test-redis-service.yml
  kubectl apply -f tagower-test-redis-deployment.yml
  kubectl apply -f tagower-test-pvc.yml
  ```

3. Check that they are running 
  ```sh
  kubectl get pods
  ```
<img width="529" alt="Screenshot 2023-04-05 at 8 48 12 PM" src="https://user-images.githubusercontent.com/70235944/230252049-f0a0d87e-c2cb-49d0-88b1-9251d8bbab89.png">

4. Get the Cluster ip for the flask service and use it to run curl commands
  ```sh
  kubectl get services
  ```
  
  <img width="390" alt="Screenshot 2023-04-05 at 8 52 30 PM" src="https://user-images.githubusercontent.com/70235944/230252605-08abd1b5-0ee4-4eb4-95ec-eccbdaccfac6.png">

5. Exec into your python debugger
  ```sh
  kubectl exec -it <your_python_debugger> -- /bin/bash
  ```
6. Run the curl commands provided in the 'Paths & Routes' or 'Usage Section' using your cluster ip
  ```sh
  curl <cluster_ip>:5000/<a_path>
  ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>
    
<!-- What the data says -->
## What the Important data says
* hgnc_id = HGNC ID. A unique ID created by the HGNC for every approved symbol. 
* locus_group = A group name for a set of related locus types as defined by the HGNC (e.g. non-coding RNA)
* locus_type = The locus type as defined by the HGNC (e.g. RNA, transfer)
* location = Cytogenetic location of the gene (e.g. 2q34)
* gene_family = Name given to a gene family or group
    
***Most other data is a form of id type for specific identification within data bases***



<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Trey Gower - goweryert@gmail.com

Project Link: https://github.com/TreyGower7/coe332-trey/tree/main/homework06

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* The Human Genome Organization: [https://www.genenames.org/download/archive/]()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
