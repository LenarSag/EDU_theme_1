from typing import Optional


class Data:
    def __init__(self, data: str, ip: int) -> None:
        self.data: str = data
        self.ip: int = ip

    def __str__(self) -> str:
        return self.data


class Server:
    _id_counter: int = 1

    def __init__(self) -> None:
        self.ip: int = Server._id_counter
        Server._id_counter += 1
        self.buffer: list[Data] = []
        self.router: Optional["Router"] = None

    def send_data(self, data: Data):
        if self.router is None:
            raise ValueError("Server not connected to a router")
        self.router.buffer.append(data)

    def get_data(self):
        data = self.buffer
        self.buffer = []
        return data

    def get_ip(self):
        return self.ip


class Router:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.connected_servers: list[Server] = []
        self.buffer: list[Data] = []

    def link(self, server: Server):
        if server not in self.connected_servers:
            self.connected_servers.append(server)
            server.router = self

    def unlink(self, server: Server):
        if server in self.connected_servers:
            self.connected_servers.remove(server)
            server.router = None

    def send_data(self):
        for data in self.buffer:
            for server in self.connected_servers:
                if server.get_ip() == data.ip:
                    server.buffer.append(data)


# router = Router()
# sv_from = Server()
# sv_from2 = Server()


# router.link(sv_from)
# router.link(sv_from2)
# router.link(Server())
# router.link(Server())

# sv_to = Server()

# router.link(sv_to)

# sv_from.send_data(Data("Hi1", sv_to.get_ip()))
# sv_from2.send_data(Data("Hi2", sv_to.get_ip()))
# sv_to.send_data(Data("Hi3", sv_from.get_ip()))

# router.send_data()

# message_from = sv_from.get_data()
# message_to = sv_to.get_data()

# print(*message_from)
# print(*message_to)
