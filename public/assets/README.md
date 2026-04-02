import logging
from payment_processor.config import Config

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

    try:
        config = Config()
        logging.info('Payment processor started')
        # code to start payment processor here
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        # handle the exception here
    finally:
        # code to handle the finally block here
        pass

if __name__ == '__main__':
    main()