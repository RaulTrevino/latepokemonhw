class Move_Tutor(Pokemon):
    def __init__(self, pokemon):
        super().__init__(pokemon)
        self.move_list = []
    def poke_api(self):
        while True:
            response = get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
            if res.ok:
                data_move = response.json()
                self.name = data_move['name']
                break
            else:
                print(f'Invalid Request, status code {response.status_code}, Please enter valid pokemon')
                self.update_pokemon()
    def add_move(self):
        if len(self.move_list) < 4:
            select_add_move = input("Enter your new move: ")
            self.move_list.append(select_add_move)
            print(f'You have updated your move list.')
            self.view_moves()
        elif len(self.move_list) > 4:
            print("You already have 4 moves, this is the max amount.")
    def delete_move(self):
        select_delete_move = input("Enter your the move you want to delete: ")
        if select_delete_move.lower() in self.move_list:
            self.move_list.remove(select_delete_move)
            print(f'You have updated your move list.')
            self.view_moves()
        else:
            print("Please enter a move that is already in your move list.")
    def update_move(self):
        old_move = input("Enter the move you want to replace: ")
        select_update_move = input("Enter your updated move: ")
        if old_move in self.move_list:
            index = self.move_list.index(old_move)
            self.move_list[index] = select_update_move
            print(f'You have updated your move list.')
            self.view_moves()
        else:
            print("Please enter a move that is already in your move list.")
    def view_moves(self):
        for move in self.move_list:
            print(move)
def driver_method(pokemon):
    while True:
        decide = input('What do you want to do?: \n [1] Add a move, \n [2] Remove a move or \n [3] Update a move \n [4] View your moves \n [5] quit?: ')
        if decide == '1':
            pokemon.add_move()
        elif decide == '2':
            pokemon.delete_move()
        elif decide == '3':
            pokemon.update_move()
        elif decide == '4':
            pokemon.view_moves()
        elif decide == '5':
            break
        else:
            print("Please select a valid option, enter a number.")
pokemon = Move_Tutor('pikachu')
driver_method(pokemon)