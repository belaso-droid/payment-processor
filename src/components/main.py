from payment_processor.config import Config
from payment_processor.strategies import StrategyFactory
from payment_processor.gateways import GatewayFactory

def main():
    config = Config()

    strategy_factory = StrategyFactory(config)
    gateway_factory = GatewayFactory(config)

    strategy = strategy_factory.create_strategy()
    gateway = gateway_factory.create_gateway()

    result = strategy.process_payment(gateway)

    if result:
        print("Payment successful")
    else:
        print("Payment failed")

if __name__ == "__main__":
    main()