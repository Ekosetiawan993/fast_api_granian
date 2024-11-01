# def main():
#     print("Hello from fast-api-granian!")


# if __name__ == "__main__":
#     main()



from hello import app
from granian import Granian
from granian.constants import HTTPModes, Interfaces, Loops, ThreadModes
from granian.log import LogLevels


# def serve_with_granian():
#     Granian(
#         app,
#         address="127.0.0.1",
#         port=8086,
#         interface="asgi",
#         workers=1,
#         threads=1,
#         # pthreads=1,
#         # threading_mode=ThreadModes.workers.value,
#         # loop=Loops.auto.value,
#         # http=HTTPModes.auto.value,
#         # websockets=True,
#         # backlog=1024,
#         # log_level=LogLevels.info.value,
#         # ssl_cert=None,
#         # ssl_key=None,
#     ).serve()


# if __name__ == "__main__":
#     serve_with_granian()

# Create an instance of the Granian server
server = Granian(
    target=app,           # Pass the FastAPI app
    interface="asgi",  # Use ASGI interface
    address="0.0.0.0",    # Host address
    port=8086          # Port number
)

# Run the server, still error AttributeError: Can't pickle local object 'FastAPI.setup.<locals>.openapi'
if __name__ == "__main__":
    server.serve()
