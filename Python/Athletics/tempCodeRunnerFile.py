    # # Opening the basic GP's
    # n_basic = button_text(
    #         driver, f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{basic_id}]/div[1]')
    # logging.info(f'Number of basic GPs: {n_basic}')

    # if len(sys.argv) > 1:
    #     n_basic = sys.argv[1]
    
    # basic_xpath = f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{basic_id}]/div[6]/div[1]/div'
    # for x in range(int(n_basic)):
    #     logging.info(f'Opening the {x}th basic reward')
    #     try:
    #         open_gp(driver, basic_xpath)
    #     except:
    #         logging.warning("Couldn't open basic GP")
    

    # # Opening the bronze GP's
    # n_bronze = button_text(
    #     driver, f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{bronze_id}]/div[1]')
    # logging.info(f'Number of bronze GPs: {n_bronze}')

    # if len(sys.argv) > 2:
    #     n_bronze = sys.argv[2]

    # bronze_xpath = f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{bronze_id}]/div[6]/div[1]/div'
    # for x in range(int(n_bronze)):
    #     logging.info(f'Opening the {x}th bronze reward')
    #     try:
    #         open_gp(driver, bronze_xpath)
    #     except:
    #         logging.warning("Couldn't open bronze GP")


    # # Opening the silver GP's
    # n_silver = button_text(
    #     driver, f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{silver_id}]/div[1]')
    # logging.info(f'Number of silver GPs: {n_silver}')

    # if len(sys.argv) > 3:
    #     n_silver = sys.argv[3]

    # silver_xpath = f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{silver_id}]/div[6]/div[1]/div'
    # for x in range(int(n_silver)):
    #     logging.info(f'Opening the {x}th silver reward')
    #     try:
    #         open_gp(driver, silver_xpath)
    #     except:
    #         logging.warning("Couldn't open silver GP")

    # # Opening the gold GP's
    # n_gold = button_text(
    #     driver, f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{gold_id}]/div[1]')
    # logging.info(f'Number of gold GPs: {n_gold}')

    # if len(sys.argv) > 4:
    #     n_gold = sys.argv[4]

    # gold_xpath = f'//*[@id="m-ui"]/div/div[4]/div[5]/div[2]/div[{gold_id}]/div[6]/div[1]/div'
    # for x in range(int(n_gold)):
    #     logging.info(f'Opening the {x}th gold reward')
    #     try:
    #         open_gp(driver, gold_xpath)
    #     except:
    #         logging.warning("Couldn't open gold GP")