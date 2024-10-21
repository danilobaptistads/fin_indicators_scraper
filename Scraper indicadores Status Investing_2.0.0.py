import os
import  logging
import pandas as pd
from lxml import etree
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import MoveTargetOutOfBoundsException

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)

#tikers = ['aesb3', 'agxy3', 'alld3', 'alpk3', 'ambp3', 'aper3', 'arml3', 'asai3', 'aure3', 'azev3', 'azev4', 'azul4', 'b3sa3', 'bbas3', 'beef3', 'biom3', 'blau3', 'blut3', 'blut4', 'bmeb4', 'bmgb4', 'bmob3', 'boas3', 'bobr4', 'bpan4', 'brit3', 'brml3', 'camb3', 'caml3', 'cash3', 'cbav3', 'ceab3', 'ciel3', 'clsa3', 'cmig4', 'cmin3', 'cogn3', 'cple3', 'crfb3', 'csed3', 'csud3', 'cury3', 'cvcb3', 'cxse3', 'desk3', 'dexp3', 'dmmo3', 'dmvf3', 'dotz3', 'elmd3', 'emae4', 'enbr3', 'enev3', 'enju3', 'espa3', 'eter3', 'fesa4', 'fher3', 'fiqe3', 'gfsa3', 'ggps3', 'gmat3', 'grnd3', 'hapv3', 'hbre3', 'hbsa3', 'hype3', 'ifcm3', 'igbr3', 'inep3', 'inep4', 'intb3', 'irbr3', 'jall3', 'jfen3', 'jslg3', 'krsa3', 'land3', 'lavv3', 'ljqq3', 'logg3', 'logn3', 'lpsb3', 'lupa3', 'lvtc3', 'lwsa3', 'matd3', 'mbly3', 'mdne3', 'mega3', 'melk3', 'merc3', 'mils3', 'mlas3', 'mnpr3', 'moar3', 'modl3', 'movi3', 'mtre3', 'mult3', 'ngrd3', 'ninj3', 'odpv3', 'ofsa3', 'oibr3', 'oibr4', 'onco3', 'opct3', 'orvr3', 'pard3', 'pdgr3', 'pdtc3', 'petz3', 'pgmn3', 'plpl3', 'prio3', 'prnr3', 'pssa3', 'ptbl3', 'raiz4', 'rani3', 'rapt4', 'rcsl3', 'rcsl4', 'rdor3', 'recv3', 'rnew3', 'rnew4', 'rrrp3', 'rsul4', 'sbfg3', 'scar3', 'seql3', 'show3', 'sled4', 'smft3', 'soja3', 'soma3', 'sqia3', 'telb4', 'tfco4', 'tgma3', 'trad3', 'tris3', 'tten3', 'vamo3', 'vbbr3', 'vitt3', 'viva3', 'vivr3', 'vlid3', 'vulc3', 'vveo3', 'west3', 'wizc3', 'wlmm4', 'zamp3']
tikers =['mglu3']

sucesso = []
falha = []

logging.basicConfig(filename='Full.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

def CreateDir(dirName):
    if not os.path.isdir(dirName):
        logging.info(f'[INFO] Criando pasdas {dirName}')
        os.makedirs(dirName)

def get_dados_din(n_indicador):
    btn_grafbar = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="main-modal"]/div[2]/div[1]/div/div[2]/button[2]')))
    driver.execute_script("arguments[0].click();", btn_grafbar)
    
    sleep(1)
    
    divdy = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[12]')))
    sleep(1)
    
    action.move_to_element_with_offset(divdy, 400, 0)
    
   
    indicador = {}
    indicador['Indicador'] = n_indicador
    try:
        while True:
            action.move_by_offset(-30, 0).perform()
            data  = driver.find_element(By.XPATH,'/html/body/div[12]/div[2]/div[2]/div/div/div/div[2]/span[1]').text
            dado = driver.find_element(By.XPATH,'/html/body/div[12]/div[2]/div[2]/div/div/div/div[2]/span[2]/span[2]/span').text
            indicador[data] = dado
            if data == '2014':
                print(f'Dicionario populado, com {len(indicador)},entradas')
                break
    except MoveTargetOutOfBoundsException:
        print(f'Dicionario populado, com {len(indicador)},entradas')
           
    btn_xgraf = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[12]/div[1]/button')))
    driver.execute_script("arguments[0].click();", btn_xgraf)
    
    return indicador

def convert_numbers(i, coluna):
    if type(i) == str:
        if i[-1] == 'M':
            tmp = dfind[coluna][dfind[coluna] == i].str.rstrip('M')
            logging.info(f'Removendo M de {i} fica assim {tmp} , na coluna {coluna}')
            tmp = tmp.astype('float64')
            logging.info(f'Convertendo {i} para {tmp} float, na coluna {coluna}')
            tmp = tmp * 1000000
            dfind[coluna][dfind[coluna] == i] = tmp
            logging.info(f'Original {i} para {tmp}, na coluna {coluna}')
        
        elif i[-1] == 'K':
            tmp = dfind[coluna][dfind[coluna] == i].str.rstrip('k')
            tmp = tmp.astype(float)
            tmp = tmp * 1000
            dfind[coluna][dfind[coluna] == i] = tmp
        
        elif i[-1] == 'B':
            tmp = dfind[coluna][dfind[coluna] == i].str.rstrip('B')
            tmp = tmp.astype(float)
            tmp = tmp * 1000000000
            dfind[coluna][dfind[coluna] == i] = tmp
  
CreateDir("Dados_Ativos")

for papel in tikers:
    try:
        
        url = f'https://statusinvest.com.br/acoes/{papel}'
        driver.get(url)

        errors = [NoSuchElementException, StaleElementReferenceException]
        wait = WebDriverWait(driver, timeout=60, ignored_exceptions= errors)

        sleep(1)
        logging.info(f'[INFO] Inciando Scraping indicadores de {papel}')
        
        div_stop = driver.find_element(By.XPATH, '//*[@id="contabil-section"]/div[1]/div/div[1]')
        wait.until(lambda d : div_stop.is_displayed())

        driver.execute_script('arguments[0].scrollIntoView();',div_stop)

        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="contabil-section"]/div[1]/div/div[2]/header/div[2]/div[4]/div[1]/input')))
        try:
            dropdown1 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="contabil-section"]/div[1]/div/div[2]/header/div[2]/div[4]/div[1]/input')))
            driver.execute_script("arguments[0].click();", dropdown1)

            data_select = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/main/div[7]/div[1]/div/div[2]/header/div[2]/div[4]/div[1]/ul/li[10]')))
            driver.execute_script("arguments[0].click();", data_select)
        except Exception as erro:
            logging.info(f'[ERRO] Dados de 10 anos não disponíveis para {papel}')

            data_max = []
            ul = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/div[7]/div[1]/div/div[2]/header/div[2]/div[4]/div[1]/ul')))
            listali=ul.find_elements(By.TAG_NAME,"li");
            
            for li in listali:
                data_max.append(li.get_attribute('id'))

            select_max = wait.until(EC.presence_of_element_located((By.ID,data_max[-1])))
            driver.execute_script("arguments[0].click();", select_max)

        sleep(1)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        estrutura = etree.HTML(str(soup))

        tabelas = soup.find_all('table')
        
        tabela = []
        colunas = []

        for col in tabelas[3].find_all('th'):
            colunas.append(col.text)

        for lin in tabelas[3].find_all('tr'):
            linha = []
            for col in lin.find_all('td'):
                linha.append(col.text)
            tabela.append(linha)

        action = webdriver.ActionChains(driver)

        btn_dy = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[1]/div/div/div/button')))
        driver.execute_script("arguments[0].click();", btn_dy)
        dicionario_dy = get_dados_din('DIVIDEND YIELD')

        btn_grafpl = driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[2]/div/div/div/button')
        driver.execute_script("arguments[0].click();", btn_grafpl)
        dicionario_pl = get_dados_din('P/L')

        btn_grafpvp = driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[4]/div/div/div/button')
        driver.execute_script("arguments[0].click();", btn_grafpvp)
        dicionario_pvp = get_dados_din('P/VP')

        btn_grafpvp = driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[5]/div/div/div/button')
        driver.execute_script("arguments[0].click();", btn_grafpvp)
        dicionario_evebitda = get_dados_din('EV/EBITIDA')

        driver.quit()
        
        logging.info(f'[INFO] Finalizando Scraping indicadores de {papel}')
        
        logging.info(f'[INFO] Iniciando Tratamendo dos dados de {papel}')

        pd.options.display.float_format = '{:.2f}'.format
        
        dy = pd.DataFrame(dicionario_dy, index=[0])
        dy.rename(columns={'ATUAL':'Últ. 12M'}, inplace=True)

        pl = pd.DataFrame(dicionario_pl, index=[0])
        pl.rename(columns={'ATUAL':'Últ. 12M'}, inplace=True)

        pvp = pd.DataFrame(dicionario_pvp, index=[0])
        pvp.rename(columns={'ATUAL':'Últ. 12M'}, inplace=True)

        evebitda = pd.DataFrame(dicionario_evebitda, index=[0])
        evebitda.rename(columns={'ATUAL':'Últ. 12M'}, inplace=True)

        df = pd.DataFrame(tabela, columns=colunas)
        df.drop(['AH %','AV %'], axis=1, inplace=True)
        df.drop(df.index[0], inplace=True)
        df['#'] = df['#'].str.rstrip('format_quote show_chart ')
        df.rename(columns={'#':'Indicador'}, inplace=True)
        columnName = df.columns[1]
        df.rename(columns={columnName:'Últ. 12M'}, inplace=True)

        dfind = pd.concat([df,dy, pl, pvp, evebitda], ignore_index=True)
        
        dfind = dfind.apply(lambda x: x.str.rstrip('%'))

        colunas_2float = list(dfind.iloc[:,1:].columns)

        dfind[colunas_2float]= dfind[colunas_2float].apply(lambda x: x.str.replace(' ',''))
        dfind[colunas_2float]= dfind[colunas_2float].apply(lambda x: x.str.replace('.',''))
        dfind[colunas_2float]= dfind[colunas_2float].apply(lambda x: x.str.replace(',','.'))
        dfind[dfind[colunas_2float] == '-'] = dfind[dfind[colunas_2float] == '-'].apply(lambda x: x.str.replace('-','0'))
       
        dfind.dropna(axis=1)
        for coluna in colunas_2float:
          dfind[coluna].apply(lambda i: convert_numbers(i, coluna))
          logging.info(f'coluna {coluna}, tratada com sucesso') 
        
           
        try:
            logging.info('Convertendo para float')
            
            dfind[colunas_2float] = dfind[colunas_2float].astype('float')
            logging.info(f'[INFO] Tratamendo dos dados de {papel} Finalizado')
            dfind.dropna
            dfind.to_parquet(f'Dados_Ativos\\indicadores_{papel}.parquet')
            logging.info(f'[INFO] Dados salvos com sucesso em indicadores_{papel}.parquet')

            sucesso.append(papel)
        except Exception as erro:
            logging.error(f'[ERROR] - Não foi possivel completar o trataento dos dados de {papel}')
            logging.error(erro)
            dfind.to_parquet(f'Dados_Ativos\\indicadores_Nao_tratado_{papel}.parquet')
            logging.info(f'[INFO] Dados salvos com sucesso em indicadores_Nao_tratado_{papel}.parquet')
            sucesso.append(papel)
        
    except Exception as erro:
        logging.error(f'[ERRO] - Não foi possivel importar dados de {papel}')
        logging.error(erro)
        falha.append(papel)
    


logging.info(f'[INFO] Ativos com sucesso {len(sucesso)}')
logging.info(f'[INFO] Lista Ativos com Sucesso:\n {sucesso}\n')
logging.info(f'[INFO] Ativos com falha {len(falha)}')
logging.info(f'[INFO] Lista Ativos com Falha:\n{falha}')