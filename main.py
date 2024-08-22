import socket
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
# Define the UDP IP address and port to listen on
UDP_IP = "0.0.0.0"
UDP_PORT = 4210
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xs = []
ys = []
def animate(i, xs, ys, val):
    xs.append(i)
    ys.append(val)
    xs = xs[-20:]
    ys = ys[-20:]
    ax.clear()
    ax.plot(xs,ys)
 
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
 
print(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}")
while True:
    # Receive data from the socket
    data, addr = sock.recvfrom(1024)
    dcd = data.decode('utf-8')
    ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys,dcd), interval=1)
    dcd = dcd
    plt.show()
    print(dcd)