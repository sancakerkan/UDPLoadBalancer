# UDP Load Balancer

This project implements a simple UDP Load Balancer that distributes incoming UDP messages to a pool of backend servers using a round-robin scheduling algorithm.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Description

The UDP Load Balancer receives messages from a client and forwards them to one of the available servers in a round-robin manner. It then waits for the server's response and forwards the response back to the client.

## Features

- Round-robin load balancing
- Timeout handling for server responses
- Error handling for communication issues

### Example Output
![Load Balancer](https://i.imgur.com/ILT9TYq.png)
(Click image to enlarge)

## Installation

1. Clone the repository

2. Ensure you have Python installed (preferably Python 3.6+).

## Usage

1. Start the load balancer:
    ```bash
    python UDPLoadBalancer.py
    ```

2. Run your servers (Server1, Server2, Server3) on the specified ports.

3. Use the client to send messages to the load balancer:
    ```bash
    python Client.py 127.0.0.1 12345
    ```

## Configuration

- **Load Balancer Address and Port:**
    - The load balancer listens on `127.0.0.1:12345` by default.
    - Modify `LB_IP` and `LB_PORT` in `UDPLoadBalancer.py` to change the address and port.

- **Server Addresses:**
    - The server addresses are specified in `SERVER_ADDRESSES` in `UDPLoadBalancer.py`.
    - Add or remove server addresses as needed.
 


## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
