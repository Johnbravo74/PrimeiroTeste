import requests
token =
url = "https://www.sintegraws.com.br/api/v1/consulta-saldo.php?token=" + token
response = requests.request("GET", url)
print(response.text)