# TCP/IP, standard application layer protocols

## TCP/IP protocol stack
- The TCP/IP stack is a set of rules used in turn, to format a message so it can be sent over a network.
- TCP/IP uses four connected layers to allow network communication to take place.
- Each layer wraps the packets with its own header data.

## Aplication layer
- Used to provide services for applications that want to communicate across a network, often the internet.
  - Uses high-level protocols that set an agreed standard between the communicating end points.
  - For example, HTTP for the web.
  - Does not determine how dat is transmitter, rather what should be sent.

## Transport layer
- Uses the Transmission control protocol (TCP) to establish an end-to-end connection with the recipient computer.
  - Splits data into packets and numbers them sequentially.
  - Adds the port number based on the protocl.
  - At the recieving end this layer confirms that packets have been recieved and requests any missing packets to be resent.

## Network layer
- Uses the internet protocol (IP) to address packets with the source and destination addresses.
  - A router forwards each packet towards an endpoint called a socket, defined by the combination of IP address and port number.
  - Each router uses a routing table to instruct the next hop.

## Link layer
- The link layer operates acrooss a physical connection
  - Adds the MAC address of the physical NIC that packets should be sent to based on the destination IP address.
  - MAC addresses change with each hop.

## Recieving data
- At the destination, the message is passed back up through the layers:
  - The link layer removed the MAC address from each packet and passes it to the network layer.
  - The network layer removed the IP address from each packet and passes it to the transport layer.
  - The transport layer removes the port number from each packet, reassembles the packets in the correct order and passes it 
    to the application layer.
  - The application layer presents the image data for the user in the browser.

## Media Access Control
- A MAC address uniquely identifies a physical device with a network interface card (NIC)



