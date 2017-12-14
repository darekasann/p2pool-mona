from p2pool.bitcoin import networks

# https://bitcointalk.org/index.php?topic=457574.0

PARENT=networks.nets['monacoin']
SHARE_PERIOD=18 # seconds
CHAIN_LENGTH=24*60*60//10 # shares
REAL_CHAIN_LENGTH=24*60*60//10 # shares
TARGET_LOOKBEHIND=200 # shares
SPREAD=20 # blocks
IDENTIFIER='d318e805888566e0'.decode('hex')
PREFIX='a81ce503af0a9734'.decode('hex')
P2P_PORT=9444
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=9456
BOOTSTRAP_ADDRS=''.split(' ')
ANNOUNCE_CHANNEL='#p2pool-mona'
VERSION_CHECK=lambda v: True
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
SEGWIT_ACTIVATION_VERSION = 16
