class Node:
    """ base class """
    def __init__(self, name, cost, health):
        """
        :param name: name of this node
        :param cost: cost of this node
        """
        self.name = name
        self.cost = cost
        self.health = health

    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_expected_health(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class ChanceNode(Node):

    def __init__(self, name, cost, health, future_nodes, probs):
        """
        :param future_nodes: future nodes connected to this node
        :param probs: probability of the future nodes
        """
        Node.__init__(self, name, cost, health)
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        """
        exp_cost = self.cost  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1
        return exp_cost

    def get_expected_health(self):
        """
        :return: expected cost of this chance node
        """
        exp_health = self.health  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_health += self.probs[i]*node.get_expected_health()
            i += 1
        return exp_health



class TerminalNode(Node):

    def __init__(self, name, cost, health):
        Node.__init__(self, name, cost, health)

    def get_expected_cost(self):
        """
        :return: cost of this chance node
        """
        return self.cost

    def get_expected_health(self):
        """
        :return: cost of this chance node
        """
        return self.health


class DecisionNode(Node):

    def __init__(self, name, cost, health, future_nodes):
        Node.__init__(self, name, cost, health)
        self.futureNode = future_nodes

    def get_expected_cost(self):
        """ returns the expected costs of future nodes"""
        costoutcomes = dict() # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            costoutcomes[node.name] = node.get_expected_cost()

        return costoutcomes

    def get_expected_health(self):
        """ returns the expected costs of future nodes"""
        healthoutcomes = dict() # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            healthoutcomes[node.name] = node.get_expected_health()

        return healthoutcomes


#######################
# See figure DT3.png (from the project menu) for the structure of this decision tree
########################

# create the terminal nodes
T1 = TerminalNode('T1', 10, 0.9)
T2 = TerminalNode('T2', 20, 0.8)
T3 = TerminalNode('T3', 30, 0.7)
T4 = TerminalNode('T4', 40, 0.6)
T5 = TerminalNode('T5', 50, 0.5)

# create C2
C2 = ChanceNode('C2', 35, 0, [T1, T2], [0.7, 0.3])
# create C1
C1 = ChanceNode('C1', 25, 0, [C2, T3], [0.2, 0.8])
# create C3
C3 = ChanceNode('C3', 45, 0, [T4, T5], [0.1, 0.9])

# create D1
D1 = DecisionNode('D1', 0, 0, [C1, C3])

print(D1.get_expected_cost())

# print the expect cost of C1
print(D1.get_expected_health())
