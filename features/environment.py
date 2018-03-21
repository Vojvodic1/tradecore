from program import TradeCoreTester
from time import sleep


def before_all(context):
    context.tester = TradeCoreTester()

def before_step(a, b):
    sleep(1)