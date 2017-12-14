import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX='fbc0b6db'.decode('hex') # same as litecoin
P2P_PORT=9401
ADDRESS_VERSION=50 # M
RPC_PORT=9402
RPC_CHECK=lambda bitcoind: True
SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//1051200
POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('lyra2re2_hash').getPoWHash(data))
BLOCK_PERIOD=90 # s
SYMBOL='MONA'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Monacoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Monacoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.monacoin'), 'monacoin.conf')
BLOCK_EXPLORER_URL_PREFIX='https://bchain.info/MONA/block/'
ADDRESS_EXPLORER_URL_PREFIX='https://bchain.info/MONA/addr/'
TX_EXPLORER_URL_PREFIX='https://bchain.info/MONA/tx/'
SANE_TARGET_RANGE=(2**256//1000000000000000000 - 1, 2**256//100000 - 1)
DUMB_SCRYPT_DIFF=256
DUST_THRESHOLD=0.03e8
