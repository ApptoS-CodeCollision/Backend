import json
import re
import requests

def parse_and_get_tx_hash(output: str) -> str:
  json_match = re.search(r'\{.*\}', output, re.DOTALL)
  tx_hash = ''

  if json_match:
      # 추출한 JSON 문자열
      json_str = json_match.group(0)
      
      # JSON 파싱
      parsed_output = json.loads(json_str)
      print(parsed_output)
      if parsed_output["Result"]:
        # transaction_hash 값 추출
        tx_hash = parsed_output["Result"]["transaction_hash"]
      elif parsed_output["Error"]:
        tx_hash = "Error"
  else:
      print("JSON 부분을 찾을 수 없습니다.")

  return tx_hash

def get_transaction_by_hash(tx_hash: str):
    url = f'https://api.testnet.aptoslabs.com/v1/transactions/by_hash/{tx_hash}'

    response = requests.get(url)
    return response
