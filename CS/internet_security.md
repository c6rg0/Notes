# Internet security

## Firewall
- A firewall is either software or hardware that controls access to and from a network.
- Numbered doors called ports are opened so that only certain traffic is allowed to pass through.

## Packet filtering
- Packets of data are inspected by the firewall to check which port they are attempting to access.
- Different network protocols use different port numbers for example, HTTP traffic, used to transfer web page data, uses port
  80 or 8080.
- If this traffic is to be allowed through, the port must be opened for the duration of the connnection, otherwise the firewall
  will automatically reject it.

## Stateful inspection
- Rather than relying on port numbers, and IP adresses to determine passage, stateful inspection examines the payload of a packet
  before allowing access and remembers actions for future decisions.
    - When data are expected from a destination they are allowed through as the details of conversation are maintained by the
      firewall.

## Proxy server
- Proxy means on behalf of.
  - A proxy server makes a web request on behalf of your own computer, hiding the true request IP address from the recipient.

- It:
  - Enables anonymous surfing,
  - Can be used to filter undesirable content,
  - Logs user data with their requests,
  - Provides a cache of previously visited sites for speed access.

## Encryption
- The act of encoding a plaintext message so that it cannot be deciphered unless you have a numerical key to decrypt it.
  - If the message is understood, it cannot be understood,
  - If the key is intercepted, the encryption process is rendered useless.

## Symmetric encryption
- Uses the same key to encrypt and then decrypt the data being transferred.
- The key has to be transferred between the communicating devices so that they both understand how to pass messages.

- A relatively fast form of encrpytion.
- Key exchange - the communicating devices have to transfer the key between them so that they both understand how to pass 
  messages.
  - Home and small office Wi-Fi networks usually use a pre-shared key (PSK).
  - How can the devices share a private key securely if they are distant from each other.

## Man in the middle attack
- Once they have the key, all that is required if for an attacker to sit in the middle of the conversation and pretend to be 
  the other party. 

## Asymetric encryption
- Also known as private/public key encryption,
- Used to initiate TLS connections
- Slower than symmetric encrpytion, so a secure communication session often uses 'hybrid' encryption.
  - The beginning of the session uses asymmetric encryption to share a private key for symmetric encryption.
  - Symmetric encrpytion speeds up the rest of the secure session.

## Digital signatures 
- In order to verify the integrity of a message, the sender can add a digital signature to a message.
- The sender creates the digital signature by:
  - Irreversibly reducing the unencrypted messages to produce a hash.
  - Encrypting the hash using their private key.
- The sender bundles the digital signature with the message and encrypts the bundle using the recipient's public key.

- The recipient of the digitally-signed, encrypted message:
  - Uses their private key to decrypt the bundle of digital signature and message.
  - Uses the sender's public key to decrypt the signature.
  - Compares the hash recieved in the decrypted signature with 

- So that people won't be able to intercept confidential data
- Becuse symmetric encryption is useless because of the man 
  in the middle attack.
- Because the reciever won't be able to decrypt it, since they
  don't have any private key but their own
- Because everyone has access to your public key
- By using a hash, you can verify that nobody has altered
  the packets in transmision?

- A firewall is a piece of software or hardware that restricts
  all incomming packets for closed ports (which by default is
  all ports).
- Firewalls that use stateful inspection have the capablity 
  of inspecting the payload sent in the packet so the content
  of the transmited data can be analysed?

- A trojan is malware that is designed to act like an ordinary
  application and make its way onto the hosts computer
  by thinking it's a safe application. A virus is harmful
  software that makes its way onto a computer, but doesn't 
  disguise itself. A worm is a self replicating virus that 
  spreads its way through networks.

- By not downloading random software, especially if sketchy.
  Downloading the software in the most safest way (from the 
  main website, and not from random links). If needed, a 
  virtual machine can be used to try out risky software.



