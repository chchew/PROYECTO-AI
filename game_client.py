import socketio
from game_functions import *
from board import humanBoard

tournament_data = {
    'user_name': 'carlos_chew',
    'tournament_id': 12
}

server_address = 'http://localhost:4000'

socket = socketio.Client()

@socket.on('connect')
def connection_event():
    data = tournament_data
    if('user_name' in data.keys() and 'tournament_id' in data.keys()):
        data.update({'user_role':'player'})
        print(f'Iniciando sesion: {data}')
        socket.emit('signin', data)

@socket.on('ok_signin')
def signin_event():
    print(f'Sesion iniciada')

@socket.on('ready')
def move_event(data):
    print(f'Nuevo tablero recibido: {data}')

    data.update({
        'movement': get_new_move(),
        'tournament_id': tournament_data['tournament_id']
    })

    print(f'Enviando nuevo movimiento: {data}')
    socket.emit('play', data)

@socket.on('finish')
def ended_event(data):
    print(f'Juego terminado resultado: {data}')

    data.update({
        'tournament_id': tournament_data['tournament_id']
    })

    print(f'Listo para siguiente partida: {data}')
    socket.emit('player_ready', data)
    

def get_new_move():
    return []


if __name__ == "__main__":
    socket.connect(server_address)
