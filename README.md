<a name="readme-top"></a>

[![LinkedIn][linkedin-shield]][linkedin-url]

### REC Platform - gRPC Protobuf Repo

The Renewable Energy Community Platform consists in a microservices API to enable and enhance Peer-to-Peer energy Transactions between Prosumers and consumers of a community.

This Repo contains the Protobuf files nto enable the communication between the different microservices.

Why building a REC Platform using microservices:
* The project was developed together with other devs
* Changes in one particular module forced to shutdown/reboot the whole API.
* This is part of a research program, therefore multiple experimental ideas, frameworks, and scripts were used. 


<p align="right">(<a href="#readme-top">Back to Top</a>)</p>



### Built With

This repo was built using:

* [gRPC](https://grpc.io/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Getting Started

For the microservices to work, it is necessary to define the message structure of the communications.

*Note: The gRPC repo import is missing in all the microservices. Do not forget to add it!*

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AnBapDan/REC-Platform-grpc.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Deployment


* To convert from proto to typescript, check the script on `package.json` 
    ```sh
    npm run proto:all
    ```


* To convert from proto to python
    ```sh
    python3 -m grpc_tools.protoc -I ./proto --python_out=python --pyi_out=python --grpc_python_out=python proto/market.proto
    ```

## Contact

Daniel Andrade - dani.andrade@ua.pt

Project Link: [https://github.com/AnBapDan/REC-Platform-grpc.git](https://github.com/AnBapDan/REC-Platform-grpc.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Acknowledgments

Below are the other devs that helped during the development of the RECPlatform :smile:

* [Eduardo Almeida](https://github.com/eapsa)
* [Francisco Monteiro](https://github.com/franciscomonteiro85)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/anbapdan/