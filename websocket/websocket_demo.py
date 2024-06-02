# -*- coding: utf-8 -*-
import asyncio
import websockets
import logging

logging.basicConfig(level=logging.INFO)

websocket_users = set()

async def check_user_permit(websocket):
    logging.info("New connection: %s", websocket)
    websocket_users.add(websocket)
    logging.info("Current websocket users: %s", websocket_users)
    try:
        while True:
            recv_str = await websocket.recv()
            cred_list = recv_str.split(":")
            if len(cred_list) == 2 and cred_list[0] == "admin" and cred_list[1] == "123456":
                response_str = "Congratulations, you have connected with the server..."
                await websocket.send(response_str)
                logging.info("Password is correct.")
                return True
            else:
                response_str = "Sorry, please input the correct username or password..."
                logging.warning("Incorrect password attempt.")
                await websocket.send(response_str)
    except websockets.ConnectionClosed:
        logging.warning("Connection closed during authentication.")
        websocket_users.remove(websocket)
        return False
    except Exception as e:
        logging.error("Exception during authentication: %s", e)
        websocket_users.remove(websocket)
        return False

async def recv_user_msg(websocket):
    try:
        while True:
            recv_text = await websocket.recv()
            logging.info("Received text: %s", recv_text)
            response_text = f"Server return: {recv_text}"
            await websocket.send(response_text)
    except websockets.ConnectionClosed:
        logging.info("Connection closed by client.")
    except Exception as e:
        logging.error("Exception in recv_user_msg: %s", e)

async def run(websocket, path):
    authenticated = await check_user_permit(websocket)
    if authenticated:
        await recv_user_msg(websocket)
    websocket_users.remove(websocket)
    logging.info("Connection ended: %s", websocket)

if __name__ == '__main__':
    logging.info("Starting WebSocket server on 127.0.0.1:8181...")
    loop = asyncio.get_event_loop()
    server = websockets.serve(run, "127.0.0.1", 8181)
    loop.run_until_complete(server)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("Server shutdown initiated.")
    finally:
        loop.close()
        logging.info("Event loop closed.")
