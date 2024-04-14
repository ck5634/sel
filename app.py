from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask ,request,jsonify
from flask_cors import CORS

app=Flask(__name__)


def download():
    options=webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver=webdriver.Chrome(options=options)
    driver.get("https://google.com")
    title=driver.title
    language=driver.find_element(By.XPATH,"//div[id=SIvCob]").text
    data={'Page Title':title,'Language':language}
    return data

@app.route("/",methods=['GET','POST'])
def Home():
    if(request.method=='GET'):
        return download()
if __name__=="__main__":
    app.run(debug=True,port=3000)
    
    
