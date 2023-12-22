## Socket Programming Project  

This project consists of three programs:

1. Client Program
2. Interface Program
3. Server Program

The user inputs a word in the client program, for example, in Persian, such as "سلام" (hello), which is then sent to the interface. The interface translates this word into English, sending "hello" to the server. The server is programmed to respond to "hello" with, for instance, "?hello, how are you?". The interface translates the server's response back into Persian and sends it to the client.

Communication between the client and the interface is implemented using UDP, while communication between the interface and the server is implemented using TCP.


## Getting Started

Prerequisites

    Python 3.x
    Pip (Python package installer)


## Setup Virtual Environment

Open a terminal and navigate to the project directory.

Create a virtual environment:

~~~bash  
python3 -m venv venv
~~~  

Activate the virtual environment:

On Windows:
~~~bash  
python3 -m venv venv
~~~  

On macOS/Linux:

~~~bash  
source venv/bin/activate
~~~  

## Install Dependencies
Install the required packages using pip:

~~~bash  
pip install -r requirements.txt
~~~  


## How to Run

1. Start the server program by executing:
~~~ bash 
python3 server.py
~~~

2. Run the interface program using:
~~~ bash 
python3 interface.py
~~~

3. Finally, execute the client program with:
~~~ bash 
python3 client.py
~~~

Feel free to customize the words and sentences in the dictionary in the utils.py file.


