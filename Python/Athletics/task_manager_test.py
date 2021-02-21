import logging
import time

logging.basicConfig(level=logging.INFO, filename="task_manager_test.log",
                    filemode='a',
                    format='%(levelname)s - %(name)s - %(message)s')


def main():

    current_time = time.ctime(time.time())
    logging.info(f'Task completed. {current_time}')


if __name__ == "__main__":
    main()
