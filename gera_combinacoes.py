from itertools import combinations
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from read_sequences import read_sequences
import os

if not os.path.exists("./resultado_combinacoes/"):
    os.makedirs("./resultado_combinacoes/")

options = Options()
options.headless = True

sequences, sequences_names = read_sequences("./combinacoes_input/sequences.txt")

driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
url = "https://www.ebi.ac.uk/Tools/psa/emboss_stretcher/"
results = list()
done = False
while not done:
    try:
        for c_names, c_sequences in zip(combinations(sequences_names, 2), combinations(sequences, 2)):
            if not os.path.exists("./resultado_combinacoes/" + " ".join(c_names) + ".txt"):
                driver.get(url)
                inputElementA = driver.find_element_by_xpath("//*[@id=\"asequence\"]")
                inputElementB = driver.find_element_by_xpath("//*[@id=\"bsequence\"]")
                submit = driver.find_element_by_xpath("//*[@id=\"jd_submitButtonPanel\"]/input")
                inputElementA.send_keys(c_sequences[0])
                inputElementB.send_keys(c_sequences[1])
                submit.send_keys("\n")
                time.sleep(5)
                contentElement = None
                for i in range(10):
                    try:
                        contentElement = driver.find_element_by_xpath("//*[@id=\"alignmentContent\"]")
                        if contentElement is not None and contentElement.text != "" and contentElement.text is not None:
                            f = open("./resultado_combinacoes/" + " ".join(c_names) + ".txt", "w")
                            f.write(contentElement.text)
                            f.close()
                            break
                    except:
                        time.sleep(5)
                        continue
        done = True
        for c_names, c_sequences in zip(combinations(sequences_names, 2), combinations(sequences, 2)):
            if not os.path.exists("./resultado_combinacoes/" + " ".join(c_names) + ".txt"):
                done = False
    except:
        continue
