#############
#   Notes   #
# Lesson 30 #
#############
'''
Quiz: Gamer's Network
'''
# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure
def create_data_structure(string_input):
    network = {}
    string_input = string_input.split('.')[0:-1]
    for line in string_input:
        if (' is connected ' in line):
            keyword = ' is connected to '
            user = line[0: line.index(keyword)]
            connections = line[len(user) + len(keyword):].split(', ')
            if(user in network):
                network[user]['connections'] = connections
            else:
                network[user] = {'connections' : connections}
        elif (' likes to play' in line):
            keyword = ' likes to play '
            user = line[0: line.index(keyword)]
            games_liked = line[len(user) + len(keyword):].split(', ')
            if(user in network):
                network[user]['games_liked'] = games_liked
            else:
                network[user] = {'games_liked' : games_liked}
    return network

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
    if (user in network):
        if('connections' in network[user]):
            return network[user]['connections']
        return []
    return None

# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    if(user in network):
        if ('games_liked' in network[user]):
            return network[user]['games_liked']
        return []
    return None

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    if(user_A in network and user_B in network):
        if ('connections' in network[user_A]):
            if (user_B in network[user_A]['connections']):
                return network
            else:
                network[user_A]['connections'].append(user_B)
                return network
        else:
            network[user_A]['connections'] = [user_B]
            return network
    else:
        return False

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    if (user not in network):
        network[user] = {}
        network[user]['games_liked'] = games
    return network
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    if (user in network):
        res = []
        if ('connections' in network[user]):
            if (len(network[user]['connections'])!=0):
                for connection in network[user]['connections']:
                    if 'connections' in network[connection]:
                        for secondary_connection in network[connection]['connections']:
                            if (secondary_connection not in res):
                                res.append(secondary_connection)
        return res
    else:
        return None
	

# ----------------------------------------------------------------------------- 	
# count_common_connections(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def count_common_connections(network, user_A, user_B):
    if(user_A in network and user_B in network):
        count = 0
        if ('connections' in network[user_A] and 'connections' in network[user_B]):
            for connection in network[user_A]['connections']:
                if connection in network[user_B]['connections']:
                    count = count +1
        return count
    return False

# ----------------------------------------------------------------------------- 
# find_path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print find_path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.
def possible_path(network, user_A, user_B, searched, tocheck):
    if ('connections' not in network[user_A]):
        return []
    if (len(network[user_A]['connections'])==0):
        return []
    else:
        if (user_A not in tocheck):
            tocheck.append(user_A)
        searched.append(user_A)
        if (user_B in network[user_A]['connections']):
            searched.append(user_B)
            return searched
        else:
            friends = network[user_A]['connections']
            for friend in friends:
                if(friend not in tocheck):
                    tocheck.append(friend)
            check = ''
            for i in range (0, len(friends)):
                if (network[user_A]['connections'][i] not in searched):
                    check = network[user_A]['connections'][i]
            if (check == ''):
                return []
            return possible_path(network, check, user_B, searched, tocheck)

def find_path_to_friend(network, user_A, user_B):
	if(network == {}):
		return None
	if ((user_A not in network) or (user_B not in network)):
		return None
	elif ('connections' not in network[user_A]):
		return None
	if (len(network[user_A]['connections'])==0):
		return None
	if (user_B in network[user_A]['connections']):
		return [user_A, user_B]
	else:
		for friend in network[user_A]['connections']:
			print friend
			result = possible_path(network, friend, user_B, [user_A], [])
			print result
			if ((result == []) and (network[user_A]['connections'][-1]==friend)):
				return None
			if (user_B in result):
				finalResult = []
				for i in range (-1, (-1*(len(result))), -1):
					print i
					if (result[i] in network[result[0]]['connections']):
						finalResult = [result[0],result[i]] + finalResult
						return finalResult
					elif result[i] in network[result[i-1]]['connections']:
						finalResult = [result[i]] + finalResult
	return None