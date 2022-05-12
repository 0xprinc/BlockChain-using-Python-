import hashlib
from block import Block

class Chain():
    def __init__(self,difficulty):
        self.difficulty = difficulty
        self.blocks = []
        self.pool = []

    def proof_of_work(self,block):
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        return block.hash.hexdigest() == hash.hexdigest() and int(hash.hexdigest(), 16) < 2**(256-self.difficulty) and block.previous_hash == self.block[-1].hash

    def add_to_chain(self,block):
        if self.proof_of_work(block):
            self.blocks.append()block
    def add_to_pool(self,data):
        self.pool.append(data)

    def create_origin_block(self):
        origin =

    def mine(self):
        if len(self.pool) > 0:
            data = self.pool.pop()
            block = Block(data, self.blocks[-1].hash)
            block.mine(self.difficulty)
            self.add_to_chain(block)