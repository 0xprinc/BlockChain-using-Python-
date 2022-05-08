import hashlib

class BlockChain():

    def __init__(self,previousBlockHash,transactionList):
        self.previousBlockHash = previousBlockHash
        self.transactionList = transactionList

        self.blockData = '-'.join(transactionList)+'-'+previousBlockHash
        self.blockHash = hashlib.sha256(self.blockData.encode()).hexdigest()

t1 = 'a -> b 2btc'
t2 = 'b -> c 1btc'
t3 = 'c -> d 2.1btc'
t4 = 'd -> e 6btc'
t5 = 'e -> f 9.4btc'
t6 = 'f -> g 1.1btc'

genesisBlock = BlockChain('zeroHash',[t1, t2])

print(genesisBlock.blockData)
print(genesisBlock.blockHash)

